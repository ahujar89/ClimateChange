import folium
from folium.plugins import HeatMap
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def create_graphs(row):
    """
    Generates multiple large graphs with proper formatting, meaningful y-axis labels,
    and encodes them as base64 images.
    """
    # Metrics and their values
    metrics = ["Soil Moisture (current)", "Temperature (current)", "Relative Humidity", "Wind Speed", "Precipitation"]
    values = [row[metric] for metric in metrics]

    # Creating a figure with larger subplots
    fig, axs = plt.subplots(1, 3, figsize=(24, 10), constrained_layout=True)

    # Bar Chart
    bars = axs[0].bar(metrics, values, color="dodgerblue")
    axs[0].set_title("Environmental Metrics", fontsize=22, fontweight="bold")
    axs[0].set_xticklabels(metrics, rotation=45, ha="right", fontsize=16)
    axs[0].set_ylabel("Metric Values", fontsize=18)  # Corrected meaningful label
    axs[0].grid(True, linestyle="--", linewidth=0.5, alpha=0.7)

    # Adding data labels to bars
    for bar in bars:
        yval = bar.get_height()
        axs[0].text(bar.get_x() + bar.get_width() / 2, yval + 0.02, f"{yval:.2f}", ha="center", fontsize=16, color="black")

    # Line Chart (e.g., trends)
    time_values = [1, 2, 3, 4, 5]  # Dummy time data; replace with actual time series
    trend_values = [row[metric] * 0.9 + i * 0.01 for i, metric in enumerate(metrics)]  # Example trend
    axs[1].plot(time_values, trend_values, marker="o", color="green", linestyle="-", linewidth=3)
    axs[1].set_title("Trend Over Time", fontsize=22, fontweight="bold")
    axs[1].set_xlabel("Time (Days)", fontsize=18)  # Clear x-axis label
    axs[1].set_ylabel("Trend Value", fontsize=18)  # Corrected y-axis label
    axs[1].grid(True, linestyle="--", linewidth=0.5, alpha=0.7)

    # Adding data labels to the line chart
    for i, txt in enumerate(trend_values):
        axs[1].text(time_values[i], trend_values[i] + 0.02, f"{txt:.2f}", fontsize=16, color="black")

    # Scatter Plot
    axs[2].scatter(row["Soil Moisture (current)"], row["Drought Index"], color="darkorange", s=150, alpha=0.9)
    axs[2].set_title("Soil Moisture vs Drought", fontsize=22, fontweight="bold")
    axs[2].set_xlabel("Soil Moisture", fontsize=18)
    axs[2].set_ylabel("Drought Index", fontsize=18)
    axs[2].grid(True, linestyle="--", linewidth=0.5, alpha=0.7)

    # Adding data labels to scatter plot
    axs[2].text(row["Soil Moisture (current)"], row["Drought Index"] + 0.02,
                f"({row['Soil Moisture (current)']:.2f}, {row['Drought Index']:.2f})", fontsize=16, color="black")

    # Saving figure to a BytesIO stream and encode as base64
    buffer = BytesIO()
    plt.savefig(buffer, format="png", bbox_inches="tight")
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.read()).decode("utf-8")
    buffer.close()
    plt.close(fig)
    return f'<img src="data:image/png;base64,{img_base64}" style="width:1100px;">'

def plot_visualizations(data):
    """
    Generates an enhanced wildfire risk heatmap with interactive popups containing graphs.
    """
    try:
        # Center of the map to pop on screen
        map_center = [data["Latitude"].mean(), data["Longitude"].mean()]
        wildfire_map = folium.Map(location=map_center, zoom_start=6)

        # Heat map data
        heat_data = [[row["Latitude"], row["Longitude"], row["Predicted Wildfire Risk"]]
                     for index, row in data.iterrows() if not pd.isna(row["Predicted Wildfire Risk"])]

        # Adding HeatMap
        HeatMap(heat_data, radius=25, blur=15, max_val=1.0, 
                gradient={0.2: "blue", 0.5: "lime", 0.7: "orange", 1.0: "red"}).add_to(wildfire_map)

        # Adding Circle Markers with graphs in popups
        for _, row in data.iterrows():
            graph_html = create_graphs(row)  # Generate multiple graphs for each city
            popup_content = f"""
            <div style="font-family: Arial; font-size: 14px; width: 1100px;">
                <h4 style="margin: 0; font-size: 16px; color: darkblue;">{row['City Name']}</h4>
                <p style="margin: 0;"><strong>Latitude:</strong> {row['Latitude']}</p>
                <p style="margin: 0;"><strong>Longitude:</strong> {row['Longitude']}</p>
                <p style="margin: 0;"><strong>Predicted Wildfire Risk:</strong> {row['Predicted Wildfire Risk']:.2f}</p>
                {graph_html} <!-- Embed the graphs as a single image -->
            </div>
            """

            folium.CircleMarker(
                location=(row["Latitude"], row["Longitude"]),
                radius=5,
                color="black",
                fill=True,
                fill_color="red" if row["Predicted Wildfire Risk"] > 0.7 else "blue",
                fill_opacity=0.7,
                popup=folium.Popup(popup_content, max_width=1200)  # Dimensions to adjust for user readability
            ).add_to(wildfire_map)

        # Saving the enhanced map
        wildfire_map.save("enhanced_wildfire_risk_heatmap_with_graphs.html")
        print("Enhanced interactive wildfire heat map saved as 'enhanced_wildfire_risk_heatmap_with_graphs.html'.")
    
    except Exception as e:
        print(f"Error during data visualization: {e}")



