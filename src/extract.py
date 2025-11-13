import os
import configparser
import pandas as pd

def extract_data():
    try:
        config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
        config.read(config_path)

        print(f"Extracting data from {config.get('data', 'path')}")
        data_path = config.get('data', 'path')

        data_filename = config.get('data', 'filename')
        
        file_path = os.path.join(data_path, data_filename)
        print(f"Reading file: {file_path}")

        df = pd.read_csv(file_path)
        print(f"Extracted {len(df)} rows from .csv")
        return df

    except Exception as e:
        print(f"Error extracting data: {e}")
        return None
