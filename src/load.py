import os
import configparser
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

def load_data(df: pd.DataFrame) -> bool:
    if df is None or df.empty:
        print("No data to load.")
        return False

    try:
        
        config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
        config.read(config_path)
        
        try:
            output_dir = config.get('output', 'dir', fallback='output')
            output_filename = config.get('output', 'filename', fallback='transformed_data.csv')
            os.makedirs(output_dir, exist_ok=True)
            csv_path = os.path.join(output_dir, output_filename)
            df.to_csv(csv_path, index=False)
            print(f"Data saved to CSV: {csv_path}")
        except Exception as e:
            print(f"Saving is ruined.")

        
        db_config = {
            'host': config.get('database', 'host', fallback='localhost'),
            'port': config.get('database', 'port', fallback='5432'),
            'dbname': config.get('database', 'dbname'),
            'user': config.get('database', 'user'),
            'password': config.get('database', 'password')
        }

        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        table_name = config.get('database', 'table', fallback='crypto_data')

        df_to_insert = df[['Timestamp', 'High', 'Low', 'Avg_price']].copy()
        df_to_insert = df_to_insert.where(pd.notnull(df_to_insert), None)
        tuples = [tuple(x) for x in df_to_insert.to_numpy()]

        insert_query = f"""
                        INSERT INTO {table_name} (Timestamp, High, Low, Avg_price)
                         VALUES %s
                        """


        execute_values(cur, insert_query, tuples, template=None, page_size=1000)
        conn.commit()
        print(f"Successfully loaded {len(tuples)} rows into table '{table_name}'.")

        cur.close()
        conn.close()
        return True

    except Exception as e:
        print("Error during loading data:", e)
        return False
