# import pandas as pd
# from pymongo import MongoClient
# import os

# def load_wildfire_data(use_mongodb=False):
#     if use_mongodb:
#         try:
#             # Connect to MongoDB
#             client = MongoClient("mongodb://localhost:27017/")
#             db = client["WildfirePredictionDB"]
#             weather_data_collection = db["weather_data"]
            
#             # Load data from MongoDB into a DataFrame
#             weather_data = pd.DataFrame(list(weather_data_collection.find()))
#             print("Data collected successfully from MongoDB.")
#             return weather_data
#         except Exception as e:
#             print(f"Error connecting to MongoDB: {e}")
#             return pd.DataFrame()
#     else:
#         try:
#             file_path = "ontario_wildfire_data_all_cities.csv"
#             data = pd.read_csv(file_path)
#             if data.empty:
#                 raise ValueError("Ontario wildfire data file is empty.")
#             print("Ontario wildfire data loaded successfully from CSV.")
#             return data
#         except FileNotFoundError:
#             print("Error: Ontario wildfire data file not found.")
#             return pd.DataFrame()
#         except pd.errors.ParserError:
#             print("Error: Failed to parse Ontario wildfire data file.")
#             return pd.DataFrame()

# # Usage
# data = load_wildfire_data(use_mongodb=True)

import pandas as pd
from pymongo import MongoClient

def load_ontario_wildfire_data():
    try:
        # Connect to MongoDB
        client = MongoClient("mongodb://localhost:27017/")
        db = client["WildfirePredictionDB"]
        collection = db["ontario_wildfire_cities"]
        
        # Load data from MongoDB into a DataFrame
        data = pd.DataFrame(list(collection.find()))
        
        # Drop the MongoDB unique identifier column if it exists
        if "_id" in data.columns:
            data = data.drop(columns=["_id"])
        
        print("Data loaded from MongoDB successfully.")
        return data
    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()