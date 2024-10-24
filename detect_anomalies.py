import pandas as pd

def detect_anomalies(sensor_data):
    # Load anomaly data
    anomaly_data = pd.read_csv('anomaly_data.csv')

    # Merge sensor data with anomaly data based on conditions
    def find_anomaly(row):
        for index, anomaly in anomaly_data.iterrows():
            if row['food_temperature'] > 10 and anomaly['anomaly_type'] == 'High Food Temperature':
                return anomaly
            if row['humidity'] > 80 and anomaly['anomaly_type'] == 'High Humidity':
                return anomaly
            if row['pH'] < 4.0 and anomaly['anomaly_type'] == 'Low pH':
                return anomaly
        return pd.Series({
            'anomaly_id': 'No Anomaly', 
            'anomaly_type': 'No Anomaly', 
            'threshold': 'N/A', 
            'actual_value': 'N/A', 
            'description': 'No issues detected', 
            'severity': 'Normal', 
            'action_required': 'No action required'
        })

    # Apply the anomaly detection function row by row
    anomaly_detected_data = sensor_data.apply(find_anomaly, axis=1)

    # Combine the sensor data and anomaly detection result
    final_data = pd.concat([sensor_data, anomaly_detected_data], axis=1)

    return final_data
