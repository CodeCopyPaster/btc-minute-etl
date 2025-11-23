from extract import extract_data
from transform import transform_data
from load import load_data
from analytics import graph

def main():
    print("Starting ETL pipeline\n")

    df_raw = extract_data()
    if df_raw is None:
        print("Extraction failed. Exiting.")
        return

    df_transformed = transform_data(df_raw)
    if df_transformed is None or df_transformed.empty:
        print("Transformation failed or resulted in empty data. Exiting.")
        return

    success = load_data(df_transformed)
    if success:
        print("\nETL pipeline completed successfully!")
    else:
        print("\nETL pipeline failed during loading.")

    graph(df_transformed)
    

if __name__ == "__main__":
    main()