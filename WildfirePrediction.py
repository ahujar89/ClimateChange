from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def train_and_predict(cleaned_data):
    # Define features and target
    features = cleaned_data[['Mean Temp (°C)', 'Max Temp (°C)', 'Heat Deg Days (°C)']]
    target = (cleaned_data['Mean Temp (°C)'] > 25).astype(int)  # Example binary target

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)

    # Train the Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Predict probabilities for the entire cleaned_data to assign risk levels
    cleaned_data['Risk Probability'] = model.predict_proba(features)[:, 1]

    # Map probabilities to human-readable risk levels
    def assign_risk_level(prob):
        if prob < 0.3:
            return "Low Risk"
        elif prob < 0.7:
            return "Moderate Risk"
        else:
            return "High Risk"

    cleaned_data['Risk Level'] = cleaned_data['Risk Probability'].apply(assign_risk_level)
    
    print("Model trained and predictions made successfully.")
    return cleaned_data