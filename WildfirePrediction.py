import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.cluster import DBSCAN

def train_lstm_model(data, scaler):
    try:
        # Only use the exact features needed for LSTM
        features = ["Soil Moisture (current)", "Temperature (current)", "Relative Humidity", "Wind Speed", "Precipitation"]
        
        # Prepare scaled data for LSTM
        X = data[features].values
        X_scaled = scaler.transform(X)  # Scale features using the same scaler
        X_seq = np.array([X_scaled[i:i+5] for i in range(len(X_scaled) - 5)])

        # Define the LSTM model
        model = Sequential([
            LSTM(50, activation="relu", input_shape=(X_seq.shape[1], X_seq.shape[2])),
            Dense(1)
        ])
        model.compile(optimizer="adam", loss="mse")
        model.fit(X_seq, X[5:, 0], epochs=5, batch_size=1)

        # Predict wildfire risks
        predictions = model.predict(X_seq)
        data["Predicted Wildfire Risk"] = np.concatenate(([np.nan] * 5, predictions.flatten()))
        print("LSTM prediction completed.")
        return data
    except Exception as e:
        print(f"Error during LSTM prediction: {e}")
        return data

def apply_dbscan_clustering(data):
    try:
        features = ["Soil Moisture (current)", "Temperature (current)", "Relative Humidity", "Wind Speed", "Precipitation"]
        clustering_features = data[features]
        dbscan = DBSCAN(eps=0.5, min_samples=5)
        data["Risk Cluster"] = dbscan.fit_predict(clustering_features)
        data["Risk Cluster"] = data["Risk Cluster"].replace(-1, np.nan)
        print("DBSCAN clustering applied.")
        return data
    except Exception as e:
        print(f"Error during DBSCAN clustering: {e}")
        data["Risk Cluster"] = np.nan
        return data