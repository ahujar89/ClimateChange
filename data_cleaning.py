from sklearn.preprocessing import MinMaxScaler
import pandas as pd


def clean_ontario_wildfire_data(data):
    try:
        # Defining here all the columns that needs to be used for our algorithm LSTM and DBSCAN
        essential_numeric_columns = [
            "Soil Moisture (current)", "Temperature (current)", "Relative Humidity", 
            "Wind Speed", "Precipitation"
        ]
        
        additional_columns = ["Latitude", "Longitude", "Drought Index", "City Name"]

        # Checking in case of any missing essential numeric columns
        missing_columns = set(essential_numeric_columns + additional_columns) - set(data.columns)
        if missing_columns:
            raise ValueError(f"Missing essential columns: {missing_columns}")

        # Extracting only the essential numeric data and fill missing values
        numeric_data = data[essential_numeric_columns].fillna(0)

        # Scaling only the LSTM-required numeric features
        scaler = MinMaxScaler()
        scaled_numeric_data = scaler.fit_transform(numeric_data)
        
        # Reconstructing all DataFrame with the scaled values and keeping additional columns
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