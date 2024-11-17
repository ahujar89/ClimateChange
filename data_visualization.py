import folium
from folium.plugins import HeatMap
import matplotlib.pyplot as plt
import pandas as pd

def plot_visualizations(data):
    try:
        # Temperature Trend Plot
        plt.figure()
        data.groupby("City Name")["Temperature (current)"].mean().plot(kind="line", marker="o")
        plt.title("Average Temperature (Current) by City")
        plt.xlabel("City")
        plt.ylabel("Temperature (°C)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # Relative Humidity Distribution
        plt.figure()
        data["Relative Humidity"].plot(kind="hist", bins=15, color="skyblue")
        plt.title("Relative Humidity Distribution")
        plt.xlabel("Relative Humidity (%)")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()

        # Soil Moisture vs. Drought Index
        plt.figure()
        plt.scatter(data["Soil Moisture (current)"], data["Drought Index"], alpha=0.6, c="darkorange")
        plt.title("Soil Moisture vs Drought Index")
        plt.xlabel("Soil Moisture (current)")
        plt.ylabel("Drought Index")
        plt.tight_layout()
        plt.show()

        # Interactive Heat Map for Wildfire Risk
        map_center = [data["Latitude"].mean(), data["Longitude"].mean()]
        wildfire_map = folium.Map(location=map_center, zoom_start=6)
        heat_data = [[row["Latitude"], row["Longitude"], row["Predicted Wildfire Risk"]] for index, row in data.iterrows() if not pd.isna(row["Predicted Wildfire Risk"])]

        HeatMap(heat_data, radius=25, blur=15, max_val=1.0, gradient={0.2: "blue", 0.5: "lime", 0.7: "orange", 1.0: "red"}).add_to(wildfire_map)
        
        # Add detailed popups for each city
        for _, row in data.iterrows():
            popup_content = f"""
            <div style="width: 200px; font-family: Arial; font-size: 12px;">
                <h4 style="margin: 0; font-size: 16px; color: darkblue;">{row['City Name']}</h4>
                <p style="margin: 0;"><strong>Latitude:</strong> {row['Latitude']}</p>
                <p style="margin: 0;"><strong>Longitude:</strong> {row['Longitude']}</p>
                <p style="margin: 0;"><strong>Predicted Wildfire Risk:</strong> {row['Predicted Wildfire Risk']:.2f}</p>
                <p style="margin: 0;"><strong>Soil Moisture (current):</strong> {row['Soil Moisture (current)']:.3f}</p>
                <p style="margin: 0;"><strong>Temperature (current):</strong> {row['Temperature (current)']:.3f} °C</p>
                <p style="margin: 0;"><strong>Relative Humidity:</strong> {row['Relative Humidity']:.3f}%</p>
                <p style="margin: 0;"><strong>Wind Speed:</strong> {row['Wind Speed']:.3f} km/h</p>
                <p style="margin: 0;"><strong>Precipitation:</strong> {row['Precipitation']:.3f} mm</p>
                <p style="margin: 0;"><strong>Drought Index:</strong> {row['Drought Index']}</p>
            </div>
            """
            
            folium.CircleMarker(
                location=(row["Latitude"], row["Longitude"]),
                radius=5,
                color="black",
                fill=True,
                fill_color="red" if row["Predicted Wildfire Risk"] > 0.7 else "blue",
                fill_opacity=0.7,
                popup=folium.Popup(popup_content, max_width=250)
            ).add_to(wildfire_map)

        # Save the map with enhanced popups
        wildfire_map.save("enhanced_wildfire_risk_heatmap.html")
        print("Enhanced interactive wildfire heat map saved as 'enhanced_wildfire_risk_heatmap.html'.")

    except Exception as e:
        print(f"Error during data visualization: {e}")