import pandas as pd

def clean_data(raw_data):
    # Drop columns with a high percentage of missing values (e.g., >20%)
    threshold = 20
    missing_percentage = raw_data.isnull().mean() * 100
    columns_to_drop = missing_percentage[missing_percentage > threshold].index
    cleaned_data = raw_data.drop(columns=columns_to_drop)
    
    # Drop rows with any remaining NaN values
    cleaned_data = cleaned_data.dropna()
    
    # Select essential columns
    essential_columns = ['Longitude (x)', 'Latitude (y)', 'Date/Time', 'Year', 'Month', 'Day', 
                         'Max Temp (°C)', 'Min Temp (°C)', 'Mean Temp (°C)', 'Heat Deg Days (°C)']
    cleaned_data = cleaned_data[essential_columns]
    
    print("Data cleaned successfully.")
    return cleaned_data