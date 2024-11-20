import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

def train_lstm_model(data, scaler):
    try:
        # Define the features used for prediction
        features = ["Soil Moisture (current)", "Temperature (current)", "Relative Humidity", "Wind Speed", "Precipitation"]
        
        # Scale the data
        X = data[features].values
        X_scaled = scaler.transform(X)
        
        # Define the sequence length for the LSTM
        sequence_length = 10
        
        # Create sequences of fixed length by padding shorter sequences as needed
        X_seq = []
        for i in range(len(X_scaled)):
            start_idx = max(0, i - sequence_length + 1)
            sequence = X_scaled[start_idx:i+1]
            
            # Pad sequence with the first row if it's shorter than sequence_length
            if len(sequence) < sequence_length:
                pad = np.tile(sequence[0], (sequence_length - len(sequence), 1))
                sequence = np.vstack((pad, sequence))
            
            X_seq.append(sequence)

        X_seq = np.array(X_seq)
        
        # Define and compile the LSTM model
        model = Sequential([
            LSTM(50, activation="relu", input_shape=(X_seq.shape[1], X_seq.shape[2])),
            Dense(1)
        ])
        model.compile(optimizer="adam", loss="mse")
        
        # Train the model (reduce epochs for testing)
        model.fit(X_seq[:-1], X[1:, 0], epochs=5, batch_size=1, verbose=1)

        # Generate predictions
        predictions = model.predict(X_seq).flatten()

        # Ensure the predictions cover all records by padding if needed
        if len(predictions) < len(data):
            data["Wildfire Risk"] = np.concatenate((predictions, np.full(len(data) - len(predictions), predictions.mean())))
        else:
            data["Wildfire Risk"] = predictions

        print("LSTM prediction completed.")
        return data
    except Exception as e:
        print(f"Error during LSTM prediction: {e}")
        data["Wildfire Risk"] = np.nan  # In case of error, set default to NaN
        return data

def apply_dbscan_clustering(data, eps=3, min_samples=5):
    try:
        # Define the features for clustering
        features = ["Soil Moisture (current)", "Temperature (current)", "Relative Humidity", "Wind Speed", "Precipitation"]
        clustering_features = data[features].values

        # Scale the features
        scaler = StandardScaler()
        clustering_features_scaled = scaler.fit_transform(clustering_features)

        # Apply DBSCAN with the specified parameters
        dbscan = DBSCAN(eps=eps, min_samples=min_samples)
        clusters = dbscan.fit_predict(clustering_features_scaled)

        # Debugging: Output unique cluster values and their counts
        unique_clusters, counts = np.unique(clusters, return_counts=True)
        print("Unique clusters:", unique_clusters)
        print("Cluster counts:", dict(zip(unique_clusters, counts)))

        # Assign clusters to a new column in the DataFrame
        data["Risk Cluster"] = clusters
        data["Risk Cluster"] = data["Risk Cluster"].replace(-1, np.nan)  # Set noise points to NaN

        print("DBSCAN clustering applied with eps =", eps, "and min_samples =", min_samples)
        return data
    except Exception as e:
        print(f"Error during DBSCAN clustering: {e}")
        data["Risk Cluster"] = np.nan
        return data
