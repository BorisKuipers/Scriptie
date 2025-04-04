import requests
import pandas as pd
from datetime import datetime
import time

def load_fear_greed_data(limit=0):
    """
    Load Fear & Greed Index data from the API
    Args:
        limit (int): Number of results to return. Use 0 for all available data
    Returns:
        DataFrame with Fear & Greed Index data
    """
    # API endpoint
    url = f"https://api.alternative.me/fng/?limit={limit}"
    
    try:
        # Make API request
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse JSON response
        data = response.json()
        
        # Extract the data points
        data_points = data['data']
        
        # Convert to DataFrame
        df = pd.DataFrame(data_points)
        
        # Convert timestamp to datetime
        df['date'] = pd.to_datetime(df['timestamp'].astype(int), unit='s')
        
        # Convert value to numeric
        df['value'] = df['value'].astype(int)
        
        # Reorder columns
        df = df[['date', 'value', 'value_classification']]
        
        # Sort by date
        df = df.sort_values('date')
        
        return df
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    # Load all available data
    df = load_fear_greed_data(limit=0)
    
    if df is not None:
        # Save to CSV
        df.to_csv('fear_greed_data.csv', index=False)
        print("Data successfully saved to fear_greed_data.csv")
        print("\nFirst few rows of the data:")
        print(df.head()) 