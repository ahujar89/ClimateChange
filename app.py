from data_collection import collect_data
from data_cleaning import clean_data
from WildfirePrediction import train_and_predict
from data_visualization import plot_risk_over_time, generate_interactive_map,plot_temperature_trends,plot_temperature_distribution,plot_temp_vs_heat_degree_days,plot_monthly_avg_temperature

def main():
    print("Starting data collection...")
    raw_data = collect_data()
    
    print("Cleaning data...")
    cleaned_data = clean_data(raw_data)
    
    print("Training model and predicting risk levels...")
    prediction_data = train_and_predict(cleaned_data)
    
    print("Generating visualizations...")
    plot_risk_over_time(prediction_data)
    plot_temperature_trends(prediction_data)
    plot_monthly_avg_temperature(prediction_data)
    plot_temp_vs_heat_degree_days(prediction_data)
    plot_temperature_distribution(prediction_data)
    generate_interactive_map(prediction_data)
    
    print("All steps completed. Check the output files for visualizations.")

if __name__ == "__main__":
    main()