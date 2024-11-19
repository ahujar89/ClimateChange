import pandas as pd

def load_ontario_wildfire_data():
    try:
        file_path = "ontario_wildfire_data_all_cities.csv"
        data = pd.read_csv(file_path)
        if data.empty:
            raise ValueError("Ontario wildfire data file is empty.")
        print("Ontario wildfire data loaded successfully.")
        return data
    except FileNotFoundError:
        print("Error: Ontario wildfire data file not found.")
        return pd.DataFrame()
    except pd.errors.ParserError:
        print("Error: Failed to parse Ontario wildfire data file.")
        return pd.DataFrame()