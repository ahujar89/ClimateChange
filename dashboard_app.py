import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import folium_static
from folium.plugins import HeatMap
from pymongo import MongoClient
from data_collection import load_ontario_wildfire_data
from data_cleaning import clean_ontario_wildfire_data
from WildfirePrediction import train_lstm_model, apply_dbscan_clustering
from data_visualization import plot_visualizations
import plotly.figure_factory as ff

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["WildfirePredictionDB"]
collection = db["ontario_wildfire_cities"]

# Set up Streamlit page configuration
st.set_page_config(layout="wide", page_title="Ontario Wildfire Prediction Dashboard")

# Sidebar for user options
st.sidebar.header("Dashboard Options")
data_source = st.sidebar.selectbox("Select Data Source", ["MongoDB"])

# Load data
st.header("1. Data Collection")
if data_source == "MongoDB":
    # Fetch data from MongoDB
    data = pd.DataFrame(list(collection.find()))
    if "_id" in data.columns:
        data = data.drop(columns=["_id"])
    st.write("Data loaded from MongoDB.")
    st.write("Data shape:", data.shape)
    st.write("Full Data Collection:", data)  # Display the full dataset

# Data Cleaning Section
st.header("2. Data Cleaning")
if st.button("Clean Data"):
    data, scaler = clean_ontario_wildfire_data(data)
    st.session_state["cleaned_data"] = data
    st.session_state["scaler"] = scaler
    st.success("Data cleaned successfully.")
    st.write("Cleaned Data:")
    st.dataframe(data)  # Display the cleaned dataset

# Wildfire Prediction Section
st.header("3. Wildfire Prediction")
if st.button("Run Wildfire Risk Prediction"):
    if "scaler" in st.session_state:
        data = train_lstm_model(data, st.session_state["scaler"])
        st.session_state["predicted_data"] = data  # Store the data with predictions in session state
        st.success("Wildfire risk prediction completed.")
        if 'Wildfire Risk' in data.columns:
            st.write("Data with Wildfire Risk Predictions:")
            st.dataframe(data)  # Display the dataset with predictions
        else:
            st.error("Prediction did not produce 'Wildfire Risk' column.")
    else:
        st.error("Please clean the data first.")

# Retrieve predicted data from session state
if "predicted_data" in st.session_state:
    data = st.session_state["predicted_data"]

# Clustering Section
st.header("4. Clustering Analysis")
if st.button("Apply DBSCAN Clustering"):
    data = apply_dbscan_clustering(data)
    st.session_state["clustered_data"] = data  # Store the data with clusters in session state
    st.success("DBSCAN clustering applied.")
    st.write("Data with Clustering Results:")
    st.dataframe(data)  # Display the dataset with clustering results

# Retrieve clustered data from session state
if "clustered_data" in st.session_state:
    data = st.session_state["clustered_data"]

# Data Visualizations
st.header("5. Data Visualizations")

# Wildfire Risk Heatmap using Folium
if st.checkbox("Show Interactive Wildfire Risk Heatmap"):
    st.subheader("Interactive Wildfire Risk Heatmap")
    
    # Initialize the folium map
    folium_map = folium.Map(location=[44.0, -79.0], zoom_start=6, tiles="OpenStreetMap")
    
    # Prepare data for the heatmap
    if 'Wildfire Risk' in data.columns:
        heat_data = [
            [row['Latitude'], row['Longitude'], row['Wildfire Risk']]
            for index, row in data.dropna(subset=['Wildfire Risk']).iterrows()
        ]
        # Add heatmap layer
        HeatMap(heat_data, radius=15, blur=10, max_zoom=1).add_to(folium_map)
        # Display the map
        folium_static(folium_map)
    else:
        st.error("Wildfire Risk column is missing. Please run the prediction step first.")

# Scatter Plot of Temperature vs Drought Index
if st.checkbox("Show Temperature vs Drought Index Scatter Plot"):
    st.subheader("Temperature vs Drought Index")
    if 'Wildfire Risk' in data.columns:
        fig = px.scatter(data, x="Temperature (current)", y="Drought Index", color="Wildfire Risk")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Please run the Wildfire Risk Prediction first to view this plot.")

# Bar Chart: Average Wildfire Risk by City
if st.checkbox("Show Average Wildfire Risk by City"):
    st.subheader("Average Wildfire Risk by City")
    avg_risk_by_city = data.groupby("City Name")["Wildfire Risk"].mean().reset_index()
    fig = px.bar(
        avg_risk_by_city, x="City Name", y="Wildfire Risk",
        title="Average Wildfire Risk by City",
        labels={"City Name": "City", "Wildfire Risk": "Average Wildfire Risk"},
        color="Wildfire Risk",
        color_continuous_scale="Reds"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Scatter Plot: Temperature vs Soil Moisture
if st.checkbox("Show Temperature vs Soil Moisture Density Plot"):
    st.subheader("Temperature vs Soil Moisture (Density Plot)")
    fig = px.density_heatmap(
        data, x="Temperature (current)", y="Soil Moisture (current)",
        z="Wildfire Risk", histfunc="avg",
        title="Temperature vs Soil Moisture (Density Plot)",
        labels={
            "Temperature (current)": "Temperature",
            "Soil Moisture (current)": "Soil Moisture",
            "Wildfire Risk": "Avg Wildfire Risk"
        },
        color_continuous_scale="Viridis"  # Attractive color gradient
    )
    st.plotly_chart(fig, use_container_width=True)

   

# Heatmap: Correlation between features
if st.checkbox("Show Correlation Heatmap"):
    st.subheader("Correlation Heatmap")
    
    # Ensure numeric data and drop 'Risk Cluster'
    numeric_data = data.select_dtypes(include=["float64", "int64"])
    if "Risk Cluster" in numeric_data.columns:
        numeric_data = numeric_data.drop(columns=["Risk Cluster"])  # Exclude Risk Cluster

    if numeric_data.empty:
        st.error("No numeric data available for correlation heatmap.")
    else:
        # Calculate correlation matrix
        correlation_matrix = numeric_data.corr()
        
        # Create the heatmap using Plotly
        fig = ff.create_annotated_heatmap(
            z=correlation_matrix.values,
            x=list(correlation_matrix.columns),
            y=list(correlation_matrix.index),
            annotation_text=correlation_matrix.round(2).values,
            colorscale="Viridis"
        )
        st.plotly_chart(fig, use_container_width=True)