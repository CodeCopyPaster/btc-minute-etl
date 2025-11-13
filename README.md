# Crypto ETL

Simple ETL toolkit for working with minute-level BTC/USD market data.

The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data).

## Overview
- `extract` loads the raw CSV into a `pandas` DataFrame.
- `src/extract`,`src/transform`, `src/load` are steps of ETL pipeline.
- Configuration is managed through `src/config.ini`.

## Project Layout
- `src/` – ETL scripts and utilities
  - `config.ini` – defines `path` and `filename`, `output path` and `database settings`
  - `transform.py`, `load.py`, `extract.py` – placeholders for upcoming stages
- `data/raw/` – location for raw data files (`btcusd_1-min_data.csv`)
- `data/processed` - location for processed data files (`transformed_data.csv`)

## How it works
1. **Load data**: The source `.csv` file is read into a pandas DataFrame for further manipulation.
2. **Transform data**: Unnecessary columns are removed, and derived columns (e.g., calculated metrics or formatted fields) are added.
3. **Export and store**: The resulting dataset is saved as a new `.csv` file and loaded into a PostgreSQL database using `psycopg2`.

## Used stack
- **Python 3.x** (*libraries: Pandas, psycopg2, configparser*, *OS*)
- **PostgreSQL 18** (*pgAdmin 4*) 
    

```
_First csv update 01/01/2012 10:01_
_Last csv update: 12/11/2025 23:57_