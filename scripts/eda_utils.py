# scripts/eda_utils.py

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from pathlib import Path

def visualize_closing_prices(data):
    """
    Visualize the closing prices of TSLA, BND, and SPY over time.
    Save the plot to 'visualizations/closing_prices.png'.
    """
    plt.figure(figsize=(12, 6))
    for asset in ["TSLA", "BND", "SPY"]:
        data[f"Close_{asset}"].plot(label=asset)

    plt.title("Closing Prices Over Time")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.legend()
    plt.savefig(Path("../visualizations/closing_prices.png"))
    plt.show()

    # Print summary statistics for closing prices
    print("\nSummary Statistics for Closing Prices:")
    for asset in ["TSLA", "BND", "SPY"]:
        close_prices = data[f"Close_{asset}"]
        print(f"{asset}:")
        print(f"  Mean: {close_prices.mean():.2f}")
        print(f"  Median: {close_prices.median():.2f}")
        print(f"  Min: {close_prices.min():.2f}")
        print(f"  Max: {close_prices.max():.2f}")

def analyze_daily_returns(data):
    """
    Calculate and visualize daily percentage changes for TSLA, BND, and SPY.
    Save the plot to 'visualizations/daily_returns.png'.
    """
    daily_returns = data[[f"Close_{asset}" for asset in ["TSLA", "BND", "SPY"]]].pct_change()

    plt.figure(figsize=(12, 6))
    for asset in ["TSLA", "BND", "SPY"]:
        daily_returns[f"Close_{asset}"].plot(label=asset)

    plt.title("Daily Percentage Change in Close Prices")
    plt.xlabel("Date")
    plt.ylabel("Daily Returns")
    plt.legend()
    plt.savefig(Path("../visualizations/daily_returns.png"))
    plt.show()

    # Print summary statistics for daily returns
    print("\nSummary Statistics for Daily Returns:")
    for asset in ["TSLA", "BND", "SPY"]:
        returns = daily_returns[f"Close_{asset}"]
        print(f"{asset}:")
        print(f"  Mean: {returns.mean():.4f}")
        print(f"  Std Dev: {returns.std():.4f}")
        print(f"  Min: {returns.min():.4f}")
        print(f"  Max: {returns.max():.4f}")

def analyze_volatility(data):
    """
    Analyze volatility by calculating rolling means and standard deviations for Tesla.
    Save the plot to 'visualizations/tesla_volatility.png'.
    """
    rolling_mean = data["Close_TSLA"].rolling(window=30).mean()
    rolling_std = data["Close_TSLA"].rolling(window=30).std()

    plt.figure(figsize=(12, 6))
    rolling_mean.plot(label="Rolling Mean (30 days)")
    rolling_std.plot(label="Rolling Std Dev (30 days)")

    plt.title("Tesla Rolling Mean and Standard Deviation")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.savefig(Path("../visualizations/tesla_volatility.png"))
    plt.show()

    # Print summary statistics for Tesla's rolling metrics
    print("\nSummary Statistics for Tesla's Volatility:")
    print(f"  Average Rolling Mean: {rolling_mean.mean():.2f}")
    print(f"  Average Rolling Std Dev: {rolling_std.mean():.2f}")

def decompose_time_series(data):
    """
    Decompose Tesla's close price into trend, seasonal, and residual components.
    Save the plot to 'visualizations/tesla_decomposition.png'.
    """
    result = seasonal_decompose(data["Close_TSLA"], model="additive", period=365)
    result.plot()
    plt.savefig(Path("../visualizations/tesla_decomposition.png"))
    plt.show()

    # Print summary statistics for decomposition components
    print("\nSummary Statistics for Tesla's Time Series Decomposition:")
    print(f"  Trend Mean: {result.trend.mean():.2f}")
    print(f"  Seasonal Mean: {result.seasonal.mean():.2f}")
    print(f"  Residual Mean: {result.resid.mean():.2f}")