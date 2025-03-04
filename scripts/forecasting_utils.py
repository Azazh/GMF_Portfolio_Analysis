# scripts/forecasting_utils.py

import pandas as pd
from pathlib import Path
from pmdarima import auto_arima
import matplotlib.pyplot as plt

from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def load_tesla_data():
    """
    Load processed data and extract Tesla's closing prices.
    """
    data_path = Path("../data/processed_data.csv")
    data = pd.read_csv(data_path, parse_dates=True, index_col="Date")
    
    # Extract Tesla's closing prices
    tesla_close = data["Close_TSLA"]
    
    return tesla_close
# scripts/forecasting_utils.py (continued)

def split_train_test(data):
    """
    Split the data into training and testing sets.
    """
    train_size = int(len(data) * 0.8)
    train, test = data[:train_size], data[train_size:]
    
    print(f"Training set size: {len(train)}")
    print(f"Testing set size: {len(test)}")
    
    return train, test
# scripts/forecasting_utils.py (continued)



def train_arima_model(train):
    """
    Train an ARIMA model using auto_arima to find optimal parameters.
    """
    # Use auto_arima to find the best (p, d, q) parameters
    model = auto_arima(
        train,
        seasonal=False,  # No seasonality in this case
        trace=True,      # Show optimization process
        error_action="ignore",
        suppress_warnings=True,
        stepwise=True
    )
    
    print("Best ARIMA model:", model.order)
    
    return model

def forecast_arima(model, test):
    """
    Use the trained ARIMA model to forecast future values.
    """
    # Forecast future values
    forecast = model.predict(n_periods=len(test))
    
    return forecast
# scripts/forecasting_utils.py (continued)


def evaluate_model(test, forecast):
    """
    Evaluate the model using MAE, RMSE, and MAPE.
    """
    mae = mean_absolute_error(test, forecast)
    rmse = np.sqrt(mean_squared_error(test, forecast))
    mape = np.mean(np.abs((test - forecast) / test)) * 100
    
    print("Evaluation Metrics:")
    print(f"  MAE: {mae:.2f}")
    print(f"  RMSE: {rmse:.2f}")
    print(f"  MAPE: {mape:.2f}%")
    
    return mae, rmse, mape

def plot_forecast(test, forecast):
    """
    Plot the actual vs. forecasted values.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(test.index, test, label="Actual", color="blue")
    plt.plot(test.index, forecast, label="Forecast", color="red")
    plt.title("Tesla Stock Price Forecast (ARIMA)")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.legend()
    plt.savefig(Path("../visualizations/tesla_forecast_arima.png"))
    plt.show()