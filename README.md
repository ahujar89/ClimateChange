# Climate Change and Wildfire Prediction Dashboard

This project provides tools and visualizations to analyze and predict the impact of climate change on wildfires. It includes data collection, cleaning, visualization, and machine learning prediction models.


## Features

- **Data Collection**: Scripts to aggregate and upload data.
- **Data Cleaning**: Preprocessing tools for datasets.
- **Dashboard**: Interactive visualizations using Streamlit.
- **Prediction Model**: Wildfire risk predictions based on weather data.
- **MongoDB Integration**: For storing and managing datasets.

---

## Project Setup Instructions

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/ahujar89/ClimateChange.git
cd ClimateChange
```

### 2. Install Dependencies

Install all necessary Python libraries using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 3. Set Up MongoDB
#### Step 1: Install MongoDB and `mongosh`
1.	Download MongoDB and MongoDB Shell from https://www.mongodb.com/try/download/shell.
2.	Install and ensure the MongoDB service is running.
3.	Add the path to `mongosh` in your system's PATH:
    - Path to add:
        ```bash
        C:\Program Files\MongoDB\mongosh-<version>\bin
        ```
    - Verify installation:
        ```bash
        mongosh --version
        ```

#### Step 2: Configure MongoDB
1. Use the script `upload_to_mongodb.py` to upload datasets to MongoDB:
    ```bash
    python upload_to_mongodb.py
    ```
2. Update the `.env` file with your MongoDB URI:
    ```bash
    MONGODB_URI="mongodb://localhost:27017"
    ```


### 4. Download and Unzip Weather Data
Unzip the `ON_combined_weather_data.csv.zip` file:
``` bash
unzip ON_combined_weather_data.csv.zip 
```

### 5. Run the Streamlit Dashboard
Start the dashboard application:

```bash
streamlit run dashboard_app.py
```

### 6. File Descriptions

- `app.py`: Main script for backend processing.

- `dashboard_app.py`: Creates the interactive dashboard.

- `data_cleaning.py`: Handles cleaning of raw data.

- `data_visualization.py`: Visualizes data for analysis.

- `WildfirePrediction.py`: Implements wildfire prediction models.

- `upload_to_mongodb.py`: Uploads datasets to MongoDB.
 
---
 
### 7. Dependencies

Install these tools before running the project:

- *Python 3.8+*

- *Streamlit*

- *MongoDB*

- Additional libraries listed in `requirements.txt`.
 
---
 
### 8. Verify Installation
 
1. Run a sample query in MongoDB:

   ```bash

   mongosh

   use <database_name>

   show collections

   ```
 
2. Test the dashboard in a browser at `http://localhost:8501`.
 
### 9. Known Issues

Ensure Streamlit and MongoDB are correctly added to `PATH`.

Restart your terminal after any `PATH` updates.
 
