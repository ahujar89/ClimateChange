import pandas as pd
from pymongo import MongoClient

def collect_data():
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["WildfirePredictionDB"]
    weather_data_collection = db["weather_data"]
    
    # Load data from MongoDB into a DataFrame
    weather_data = pd.DataFrame(list(weather_data_collection.find()))
    print("Data collected successfully.")
    return weather_data