import os
import configparser
import pandas as pd
import subprocess
import zipfile


def extract_data():
    try:

        config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
        config.read(config_path)

        output_dir = config.get('data', 'path')
        output_dir = os.path.abspath(os.path.normpath(output_dir))

        csv_files = [f for f in os.listdir(output_dir) if f.endswith('.csv')]
        
        if csv_files:
            csv_file = os.path.join(output_dir, csv_files[0])
            print(f'Reading data from {csv_file}')
            df = pd.read_csv(csv_file)
            return df
        

        print("Downloading dataset from Kaggle...")
        result = subprocess.run([
            "kaggle", "datasets", "download",
            "-d", "mczielinski/bitcoin-historical-data",
            "-p", output_dir
        ], capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Kaggle download failed: {result.stderr}")
            return None


        zip_files = [f for f in os.listdir(output_dir) if f.endswith('.zip')]
        if zip_files:
            zip_path = os.path.join(output_dir, zip_files[0])
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(output_dir)
            os.remove(zip_path)


        csv_files = [f for f in os.listdir(output_dir) if f.endswith('.csv')]
        if not csv_files:
            return None

        csv_file = os.path.join(output_dir, csv_files[0])
        df = pd.read_csv(csv_file)
        return df

    except Exception as e:
        print(f"Error extracting data: {e}")
        import traceback
        traceback.print_exc()
        return None
