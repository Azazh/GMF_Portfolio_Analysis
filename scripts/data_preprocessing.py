# scripts/data_preprocessing.py

import yfinance as yf
import pandas as pd
from pathlib import Path

def fetch_and_save_raw_data():
    """
    Fetch historical financial data for TSLA, BND, and SPY using YFinance.
    Save the raw data to the 'data/raw_data.csv' file.
    """
    # Define assets and date range
    assets = ["TSLA", "BND", "SPY"]
    start_date = "2015-01-01"
    end_date = "2025-01-31"

    # Fetch data
    data = yf.download(assets, start=start_date, end=end_date)

    # Flatten multi-level columns
    data.columns = [f"{col[0]}_{col[1]}" for col in data.columns]

    # Save raw data to CSV
    data_path = Path("../data/raw_data.csv")
    data.to_csv(data_path)

    print(f"Raw data saved to {data_path}")

def clean_and_save_data():
    """
    Load raw data, clean it, and save the processed data to 'data/processed_data.csv'.
    """
    # Load raw data
    data_path = Path("../data/raw_data.csv")
    data = pd.read_csv(data_path, parse_dates=True, index_col=0)

    # Inspect raw data structure
    # print("Raw Data Columns:")
    # print(data.columns)
    # print("\nFirst Few Rows of Raw Data:")
    # print(data.head())

    # Flatten multi-level columns if they exist
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [f"{col[0]}_{col[1]}" for col in data.columns]
        print("Flattened Columns:", data.columns)
    else:
        print("Columns are already flattened:", data.columns)

    # Replace spaces in column names with underscores
    data.columns = data.columns.str.replace(" ", "_")
    # print("Final Column Names:", data.columns)

    # Strip any leading/trailing spaces in column names
    data.columns = data.columns.str.strip()

    # Check for missing values
    missing_values = data.isnull().sum()
    # print("Missing Values:\n", missing_values)

    # Handle missing values
    data.fillna(method="ffill", inplace=True)  # Forward fill missing values
    data.dropna(inplace=True)  # Drop rows with remaining missing values

    # Verify column names before astype()
    # print("Final Columns Before astype():", data.columns)

    # Ensure appropriate data types
    data = data.astype({
        "Open_BND": float,
        "High_BND": float,
        "Low_BND": float,
        "Close_BND": float,
        "Volume_BND": int,
        "Open_SPY": float,
        "High_SPY": float,
        "Low_SPY": float,
        "Close_SPY": float,
        "Volume_SPY": int,
        "Open_TSLA": float,
        "High_TSLA": float,
        "Low_TSLA": float,
        "Close_TSLA": float,
        "Volume_TSLA": int,
    })

    # Save cleaned data to CSV
    processed_path = Path("../data/processed_data.csv")
    data.to_csv(processed_path)

    print(f"Processed data saved to {processed_path}")
def main():
    """
    Main function to execute data preprocessing tasks.
    """
    # Step 1: Fetch and save raw data
    fetch_and_save_raw_data()

    # Step 2: Clean and save processed data
    clean_and_save_data()


if __name__ == "__main__":
    # Execute the main function when the script is run directly
    main()