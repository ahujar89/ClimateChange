from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def clean_ontario_wildfire_data(data):
    try:
        # Defining the essential numeric columns required for LSTM and DBSCAN
        essential_numeric_columns = [
            "Soil Moisture (current)", "Temperature (current)", "Relative Humidity", 
            "Wind Speed", "Precipitation"
        ]
        
        additional_columns = ["Latitude", "Longitude", "Drought Index", "City Name"]

        # Checking for missing essential columns
        missing_columns = set(essential_numeric_columns + additional_columns) - set(data.columns)
        if missing_columns:
            raise ValueError(f"Missing essential columns: {missing_columns}")

        # Extracting only the essential numeric data and filling missing values with 0
        numeric_data = data[essential_numeric_columns].fillna(0)

        # Scaling only the numeric features needed for LSTM
        scaler = MinMaxScaler()
        scaled_numeric_data = scaler.fit_transform(numeric_data)
        
        # Reconstructing the DataFrame with the scaled values and keeping additional columns
        scaled_data = pd.DataFrame(scaled_numeric_data, columns=essential_numeric_columns)
        for col in additional_columns:
            scaled_data[col] = data[col]
            
        print("Data cleaned and scaled.")
        return scaled_data, scaler
    except ValueError as e:
        print(f"Error during data cleaning: {e}")
        return pd.DataFrame(), None
    except Exception as e:
        print(f"Unexpected error during data cleaning: {e}")
        return pd.DataFrame(), None