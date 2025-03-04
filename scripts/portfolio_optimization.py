# scripts/portfolio_optimization.py

from matplotlib import pyplot as plt
import pandas as pd
from pathlib import Path

def combine_forecasted_data(tsla_forecast, bnd_forecast, spy_forecast):
    """
    Combine forecasted data for TSLA, BND, and SPY into a single DataFrame.
    """
    # Create a DataFrame with forecasted prices
    dates = pd.date_range(start="2025-02-01", periods=len(tsla_forecast), freq="D")
    df = pd.DataFrame({
        "TSLA": tsla_forecast,
        "BND": bnd_forecast,
        "SPY": spy_forecast
    }, index=dates)
    
    return df
def compute_annualized_returns(df):
    """
    Compute annualized returns for each asset.
    """
    daily_returns = df.pct_change().dropna()
    annualized_returns = daily_returns.mean() * 252  # 252 trading days per year
    
    print("Annualized Returns:")
    print(annualized_returns)
    
    return annualized_returns

def compute_covariance_matrix(df):
    """
    Compute the covariance matrix of daily returns.
    """
    daily_returns = df.pct_change().dropna()
    covariance_matrix = daily_returns.cov() * 252  # Scale to annualize
    
    print("Covariance Matrix:")
    print(covariance_matrix)
    
    return covariance_matrix

import numpy as np

def calculate_portfolio_metrics(weights, annualized_returns, covariance_matrix, risk_free_rate=0.02):
    """
    Calculate portfolio return, risk, and Sharpe Ratio.
    """
    # Portfolio Return
    portfolio_return = np.dot(weights, annualized_returns)
    
    # Portfolio Risk (Volatility)
    portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(covariance_matrix, weights)))
    
    # Sharpe Ratio
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_risk
    
    return portfolio_return, portfolio_risk, sharpe_ratio

from scipy.optimize import minimize

def optimize_portfolio(annualized_returns, covariance_matrix, risk_free_rate=0.02):
    """
    Optimize portfolio weights to maximize the Sharpe Ratio.
    """
    num_assets = len(annualized_returns)
    
    # Objective function to minimize (negative Sharpe Ratio)
    def negative_sharpe_ratio(weights):
        portfolio_return, portfolio_risk, sharpe_ratio = calculate_portfolio_metrics(
            weights, annualized_returns, covariance_matrix, risk_free_rate
        )
        return -sharpe_ratio
    
    # Constraints: Weights must sum to 1
    constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})
    
    # Bounds: Weights must be between 0 and 1
    bounds = [(0, 1) for _ in range(num_assets)]
    
    # Initial guess: Equal weights
    initial_weights = [1 / num_assets] * num_assets
    
    # Perform optimization
    result = minimize(negative_sharpe_ratio, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)
    
    optimized_weights = result.x
    optimized_return, optimized_risk, optimized_sharpe = calculate_portfolio_metrics(
        optimized_weights, annualized_returns, covariance_matrix, risk_free_rate
    )
    
    print("Optimized Weights:", optimized_weights)
    print("Optimized Return:", optimized_return)
    print("Optimized Risk:", optimized_risk)
    print("Optimized Sharpe Ratio:", optimized_sharpe)
    
    return optimized_weights, optimized_return, optimized_risk, optimized_sharpe

def calculate_var(df, weights, confidence_level=0.95):
    """
    Calculate Value at Risk (VaR) for the portfolio.
    """
    daily_returns = df.pct_change().dropna()
    portfolio_returns = daily_returns.dot(weights)
    var = np.percentile(portfolio_returns, 100 * (1 - confidence_level))
    
    print(f"Value at Risk (VaR) at {confidence_level * 100}% confidence level:", var)
    
    return var

def plot_cumulative_returns(df, weights):
    """
    Plot cumulative returns for the portfolio.
    """
    daily_returns = df.pct_change().dropna()
    portfolio_returns = daily_returns.dot(weights)
    cumulative_returns = (1 + portfolio_returns).cumprod()
    
    plt.figure(figsize=(12, 6))
    plt.plot(cumulative_returns, label="Portfolio Cumulative Returns")
    plt.title("Cumulative Portfolio Returns")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.legend()
    plt.savefig(Path("../visualizations/portfolio_cumulative_returns.png"))
    plt.show()