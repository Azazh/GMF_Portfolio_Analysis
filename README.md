
# **GMF Portfolio Analysis**

![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg) ![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue)

## **Overview**
This project focuses on preprocessing and exploring historical financial data to support portfolio management strategies for **Guide Me in Finance (GMF) Investments**, a forward-thinking financial advisory firm. The analysis leverages **time series forecasting** and **data-driven insights** to optimize asset allocation and enhance portfolio performance.

The dataset includes historical financial metrics (e.g., Open, High, Low, Close, Volume) for three key assets:
- **Tesla (TSLA):** High-growth, high-risk stock.
- **Vanguard Total Bond Market ETF (BND):** Low-risk bond ETF providing stability.
- **S&P 500 ETF (SPY):** Broad U.S. market exposure with moderate risk.

The project is structured into reusable scripts, Jupyter notebooks, and visualizations to ensure modularity and reproducibility.


## **Features**
- **Data Preprocessing:** Fetch, clean, and prepare raw financial data for analysis.
- **Exploratory Data Analysis (EDA):** Analyze trends, volatility, and patterns in the data.
- **Time Series Forecasting:** Build ARIMA and LSTM models to predict Tesla's future stock prices.
- **Portfolio Optimization:** Optimize asset allocations based on forecasted trends to maximize returns and minimize risks.
- **Visualization:** Generate insightful plots to understand asset performance and risk.



## **Folder Structure**
The project is organized as follows:

```
GMF_Portfolio_Analysis/
│
├── .github/                  # GitHub workflows (e.g., CI/CD pipelines)
│   └── workflows/            # Example: Python testing workflows
│
├── .gitignore                # Files and folders to ignore in version control
├── .vscode/                  # VS Code settings (optional)
│
├── data/                     # Folder to store raw and processed data
│   ├── raw_data.csv          # Raw data fetched from YFinance
│   └── processed_data.csv    # Cleaned and preprocessed data
│
├── notebooks/                # Jupyter Notebooks for analysis
│   ├── Task1_Data_Preprocessing.ipynb  # Notebook for Task 1
│   ├── Task2_TimeSeriesForecasting.ipynb  # Notebook for Task 2
│   ├── Task3_ForecastFutureTrends.ipynb  # Notebook for Task 3
│   └── Task4_PortfolioOptimization.ipynb  # Notebook for Task 4
│
├── scripts/                  # Reusable Python scripts
│   ├── __init__.py           # Makes the folder a Python package
│   ├── data_preprocessing.py # Functions for data cleaning and preprocessing
│   ├── eda_utils.py          # Functions for exploratory data analysis
│   ├── forecasting_utils.py  # Functions for time series forecasting
│   └── portfolio_optimization.py  # Functions for portfolio optimization
│
├── src/                      # Source code for reusable modules
│   └── utils.py              # Utility functions (e.g., file handling)
│
├── tests/                    # Unit tests for scripts and modules
│   └── test_data_preprocessing.py
│
├── visualizations/           # Folder to store plots and charts
│   ├── closing_prices.png    # Closing prices plot
│   ├── daily_returns.png     # Daily returns plot
│   ├── tesla_volatility.png  # Tesla rolling mean/std dev plot
│   ├── tesla_decomposition.png # Time series decomposition plot
│   ├── tesla_future_forecast_arima.png # Future forecast plot
│   └── portfolio_cumulative_returns.png # Portfolio cumulative returns plot
│
├── README.md                 # Project description and instructions
└── requirements.txt          # List of Python dependencies
```



## **Installation and Setup**

### **Prerequisites**
- Python 3.8 or higher
- Git

### **Steps to Set Up**
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/GMF_Portfolio_Analysis.git
   cd GMF_Portfolio_Analysis
   ```

2. **Set Up a Virtual Environment (Optional but Recommended):**
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Fetch and Process Data:**
   Run the following script to fetch and preprocess the data:
   ```bash
   python scripts/data_preprocessing.py
   ```

5. **Run the Notebooks:**
   Launch Jupyter Notebook to execute the analysis:
   ```bash
   jupyter notebook notebooks/
   ```



## **Tasks Completed**

### **Task 1: Data Preprocessing and Exploratory Analysis**
- Fetched historical financial data for TSLA, BND, and SPY using the `yfinance` library.
- Cleaned and preprocessed the data (handled missing values, ensured correct data types).
- Performed exploratory data analysis (EDA) to analyze trends, volatility, and patterns.
- Generated visualizations such as closing prices, daily returns, rolling statistics, and time series decomposition.

### **Task 2: Time Series Forecasting Models**
- Built and evaluated forecasting models for Tesla's stock prices using:
  - **ARIMA**: A statistical model suitable for univariate time series.
  - **LSTM**: A deep learning model capable of capturing complex patterns.
- Compared the performance of both models using metrics like MAE, RMSE, and MAPE.

### **Task 3: Forecast Future Market Trends**
- Used the trained ARIMA model to forecast Tesla's stock prices for the next 6–12 months.
- Analyzed the forecasted trends, confidence intervals, and potential risks.
- Provided insights into opportunities and risks based on the forecast.

### **Task 4: Optimize Portfolio Based on Forecast**
- Combined forecasted data for TSLA, BND, and SPY to optimize a sample investment portfolio.
- Calculated portfolio metrics such as expected return, risk (volatility), Sharpe Ratio, and Value at Risk (VaR).
- Optimized asset allocations to maximize returns while minimizing risks.
- Visualized cumulative portfolio returns and analyzed the results.



## **Key Findings**
### **Summary Statistics**
#### **Closing Prices**
| **Asset** | **Mean**   | **Median** | **Min**   | **Max**    |
|-----------|------------|------------|-----------|------------|
| TSLA      | $117.85    | $30.30     | $9.58     | $479.86    |
| BND       | $69.29     | $68.33     | $61.86    | $78.82     |
| SPY       | $316.07    | $277.12    | $156.80   | $609.75    |

#### **Daily Returns**
| **Asset** | **Mean Return** | **Std Dev** | **Min Return** | **Max Return** |
|-----------|-----------------|-------------|----------------|----------------|
| TSLA      | 0.0020          | 0.0360      | -0.2106        | 0.2192         |
| BND       | 0.0001          | 0.0034      | -0.0544        | 0.0422         |
| SPY       | 0.0006          | 0.0111      | -0.1094        | 0.0906         |

### **Optimized Portfolio**
- **Weights**: TSLA = 0.00%, BND = 100.00%, SPY = 0.00%
- **Expected Return**: 66.93%
- **Risk (Volatility)**: 0.01%
- **Sharpe Ratio**: 4491.20
- **Value at Risk (VaR)**: -0.26% at 95% confidence level



## **Contributing**
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m "Add YourFeatureName"`)
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.



## **License**
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.



## **Contact**
For questions or feedback, feel free to reach out:
- Email: azazhwuletaw@gmail.com
- GitHub: https://github.com/azazh



## **Acknowledgments**
- **yfinance:** For providing access to historical financial data.
- **Pandas, Matplotlib, Statsmodels:** For data manipulation, visualization, and analysis.
- **TensorFlow, Scikit-learn:** For building and evaluating machine learning models.
