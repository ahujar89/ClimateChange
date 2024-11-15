import matplotlib.pyplot as plt
import folium
import pandas as pd

def plot_risk_over_time(prediction_data):
    # Prepare data for time-based visualization
    prediction_data['Date'] = pd.to_datetime(prediction_data['Date/Time']).dt.date
    daily_risk_counts = prediction_data.groupby(['Date', 'Risk Level']).size().unstack(fill_value=0)
    
    # Plot a stacked bar chart of risk levels over time
    daily_risk_counts.plot(kind='bar', stacked=True, figsize=(14, 7), color=['green', 'orange', 'red'])
    plt.xlabel("Date")
    plt.ylabel("Count of Risk Levels")
    plt.title("Daily Wildfire Risk Levels Over Time")
    plt.legend(title="Risk Level")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    plt.close()
    print("Time-based risk level plot generated.")

def plot_temperature_trends(prediction_data):
    # Convert 'Date/Time' to datetime and sort
    prediction_data['Date'] = pd.to_datetime(prediction_data['Date/Time'])
    prediction_data = prediction_data.sort_values(by="Date")
    
    # Plot mean temperature over time
    plt.figure(figsize=(12, 6))
    plt.plot(prediction_data['Date'], prediction_data['Mean Temp (°C)'], label='Mean Temperature (°C)')
    plt.xlabel("Date")
    plt.ylabel("Mean Temperature (°C)")
    plt.title("Mean Temperature Trends Over Time")
    plt.legend()
    plt.show()
    plt.close()
    print("Temperature trends over time plot generated.")

def plot_monthly_avg_temperature(prediction_data):
    # Calculate average monthly temperature
    prediction_data['Month'] = pd.to_datetime(prediction_data['Date/Time']).dt.month
    monthly_avg_temp = prediction_data.groupby('Month')['Mean Temp (°C)'].mean()
    
    # Plot monthly average temperatures
    plt.figure(figsize=(10, 5))
    plt.bar(monthly_avg_temp.index, monthly_avg_temp.values, color='orange')
    plt.xlabel("Month")
    plt.ylabel("Average Mean Temperature (°C)")
    plt.title("Average Monthly Mean Temperature")
    plt.xticks(range(1, 13))  # Label months from 1 to 12
    plt.show()
    plt.close()
    print("Monthly average temperature plot generated.")

def plot_temp_vs_heat_degree_days(prediction_data):
    # Scatter plot of Max Temperature vs Heat Degree Days
    plt.figure(figsize=(10, 6))
    plt.scatter(prediction_data['Max Temp (°C)'], prediction_data['Heat Deg Days (°C)'], alpha=0.6, color='purple')
    plt.xlabel("Max Temperature (°C)")
    plt.ylabel("Heat Degree Days (°C)")
    plt.title("Max Temperature vs. Heat Degree Days")
    plt.show()
    plt.close()
    print("Max Temperature vs. Heat Degree Days plot generated.")

def plot_temperature_distribution(prediction_data):
    # Create a box plot for temperature distribution by month
    prediction_data['Month'] = pd.to_datetime(prediction_data['Date/Time']).dt.month
    plt.figure(figsize=(12, 6))
    prediction_data.boxplot(column='Mean Temp (°C)', by='Month', grid=False)
    plt.xlabel("Month")
    plt.ylabel("Mean Temperature (°C)")
    plt.title("Monthly Temperature Distribution")
    plt.suptitle('')  # Remove the default title for a cleaner look
    plt.show()
    plt.close()
    print("Temperature distribution by month plot generated.")

def generate_interactive_map(prediction_data):
    # Filter a sample of data points for faster visualization
    sample_data = prediction_data.sample(500)
    
    # Center the map on the mean latitude and longitude of the sample data
    map_center = [sample_data['Latitude (y)'].mean(), sample_data['Longitude (x)'].mean()]
    wildfire_map = folium.Map(location=map_center, zoom_start=6)
    
    # Create feature groups for different layers
    weather_layer = folium.FeatureGroup(name="Weather Data")
    wildfire_layer = folium.FeatureGroup(name="Wildfire Risk Data")
    
    # Define colors for wildfire risk levels
    risk_colors = {
        "Low Risk": "green",
        "Moderate Risk": "orange",
        "High Risk": "red"
    }

    # Add Weather Data Markers
    for _, row in sample_data.iterrows():
        # Check if wildfire risk data is available
        if 'Risk Level' in row and 'Risk Probability' in row:
            # Add wildfire risk data marker with color coding
            wildfire_popup = folium.Popup(
                f"<b>Wildfire Risk Data:</b><br>"
                f"<b>Risk Level:</b> {row['Risk Level']}<br>"
                f"<b>Risk Probability:</b> {row['Risk Probability']:.2f}<br>"
                f"<b>Mean Temperature:</b> {row['Mean Temp (°C)']} °C<br>"
                f"<b>Location:</b> ({row['Latitude (y)']}, {row['Longitude (x)']})",
                max_width=250
            )
            folium.CircleMarker(
                location=[row['Latitude (y)'], row['Longitude (x)']],
                radius=6,
                color=risk_colors[row['Risk Level']],
                fill=True,
                fill_color=risk_colors[row['Risk Level']],
                fill_opacity=0.7,
                popup=wildfire_popup
            ).add_to(wildfire_layer)

        # Add weather data marker
        weather_popup = folium.Popup(
            f"<b>Weather Data:</b><br>"
            f"<b>Mean Temperature:</b> {row['Mean Temp (°C)']} °C<br>"
            f"<b>Max Temperature:</b> {row['Max Temp (°C)']} °C<br>"
            f"<b>Min Temperature:</b> {row['Min Temp (°C)']} °C<br>"
            f"<b>Heat Degree Days:</b> {row['Heat Deg Days (°C)']} °C",
            max_width=250
        )
        folium.Marker(
            location=[row['Latitude (y)'], row['Longitude (x)']],
            popup=weather_popup,
            icon=folium.Icon(color='blue', icon='cloud')
        ).add_to(weather_layer)

    # Add layers to the map
    weather_layer.add_to(wildfire_map)
    wildfire_layer.add_to(wildfire_map)
    
    # Add layer control to toggle between weather and wildfire layers
    folium.LayerControl().add_to(wildfire_map)

    # Save the map as an HTML file
    wildfire_map.save("enhanced_wildfire_weather_map.html")
    print("Enhanced interactive map saved as enhanced_wildfire_weather_map.html.")