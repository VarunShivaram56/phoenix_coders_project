import pandas as pd
import os
from detect_anomalies import detect_anomalies

def generate_report():
    # Load sensor data
    sensor_data = pd.read_csv('sensor_data.csv')

    # Load production records data
    production_data = pd.read_csv('production_records.csv')

    # Detect anomalies
    anomaly_data = detect_anomalies(sensor_data)

    # Merge with production data
    merged_data = pd.merge(anomaly_data, production_data, left_index=True, right_index=True, how='left')

    # Create output directory if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    # Save the final report as CSV
    final_report_path = os.path.join('output', 'final_report.csv')
    merged_data.to_csv(final_report_path, index=False)

    print(f"Report generated at {final_report_path}")
