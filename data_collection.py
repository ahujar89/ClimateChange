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