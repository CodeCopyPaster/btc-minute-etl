import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:

    if df is None or df.empty:
        return df


    df = df.drop(columns=['Open'], errors='ignore')
    df = df.drop(columns=['Close'], errors='ignore')
    df = df.drop(columns=['Volume'], errors='ignore')

    df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s', errors='coerce')
    df['Avg_price'] = (df['High'] + df['Low']) / 2
    print(df.columns)

    return df