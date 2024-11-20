from data_collection import load_ontario_wildfire_data  # Adjusted function name
from data_cleaning import clean_ontario_wildfire_data
from WildfirePrediction import train_lstm_model, apply_dbscan_clustering
from data_visualization import plot_visualizations

def main():
    try:
        # Decide data source (set to True if MongoDB is preferred)
        use_mongodb = True  # Set to True to use MongoDB, False to fall back to CSV

        print("Loading Ontario wildfire data...")
        data = load_ontario_wildfire_data() if use_mongodb else load_ontario_wildfire_data_from_csv()
        if data.empty:
            raise ValueError("Data loading failed.")

        print("Cleaning data...")
        data, scaler = clean_ontario_wildfire_data(data)
        if scaler is None:
            raise ValueError("Data cleaning failed.")

        print("Predicting wildfire risk with LSTM...")
        data = train_lstm_model(data, scaler)

        print("Applying DBSCAN clustering...")
        data = apply_dbscan_clustering(data)

        print("Generating data visualizations...")
        plot_visualizations(data)

        print("All steps completed successfully.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()