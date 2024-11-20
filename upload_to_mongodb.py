import pandas as pd
from pymongo import MongoClient

def upload_csv_to_mongodb(csv_path, db_name, collection_name):
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    collection = db[collection_name]

    # Load CSV data into a DataFrame
    data = pd.read_csv(csv_path)
    if not data.empty:
        # Clear the collection before inserting new data
        collection.delete_many({})
        # Insert data into MongoDB
        collection.insert_many(data.to_dict("records"))
        print("Data uploaded to MongoDB successfully.")
    else:
        print("CSV file is empty. Please provide a valid file.")

# Usage
upload_csv_to_mongodb("ontario_wildfire_data_all_cities.csv", "WildfirePredictionDB", "ontario_wildfire_cities")