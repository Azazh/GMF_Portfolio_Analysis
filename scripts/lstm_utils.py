# scripts/lstm_utils.py

import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential

def prepare_lstm_data(data, look_back=60):
    """
    Prepare data for LSTM by creating sequences.
    """
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data.values.reshape(-1, 1))
    
    X, y = [], []
    for i in range(look_back, len(scaled_data)):
        X.append(scaled_data[i - look_back:i, 0])
        y.append(scaled_data[i, 0])
    
    X, y = np.array(X), np.array(y)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))
    
    return X, y, scaler

def build_lstm_model(input_shape):
    """
    Build an LSTM model.
    """
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=input_shape),
        LSTM(50, return_sequences=False),
        Dense(25),
        Dense(1)
    ])
    
    model.compile(optimizer="adam", loss="mean_squared_error")
    return model
# scripts/lstm_utils.py (continued)

def forecast_future_lstm(model, scaler, last_sequence, steps=180):
    """
    Generate future forecasts using the trained LSTM model.
    """
    future_forecast = []
    current_sequence = last_sequence.copy()
    
    for _ in range(steps):
        # Predict the next value
        next_value = model.predict(current_sequence.reshape(1, -1, 1))
        
        # Append the prediction to the forecast
        future_forecast.append(next_value[0, 0])
        
        # Update the sequence for the next prediction
        current_sequence = np.roll(current_sequence, -1)
        current_sequence[-1] = next_value
    
    # Inverse transform the forecasted values
    future_forecast = scaler.inverse_transform(np.array(future_forecast).reshape(-1, 1)).flatten()
    
    print("Forecast Generated for", steps, "days.")
    return future_forecast