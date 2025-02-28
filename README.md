


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
- **Visualization:** Generate insightful plots to understand asset performance and risk.
- **Portfolio Insights:** Provide actionable recommendations based on statistical analysis.



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
│   └── Task1_Data_Preprocessing.ipynb  # Notebook for Task 1
│
├── scripts/                  # Reusable Python scripts
│   ├── __init__.py           # Makes the folder a Python package
│   ├── data_preprocessing.py # Functions for data cleaning and preprocessing
│   └── eda_utils.py          # Functions for exploratory data analysis
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
│   └── tesla_decomposition.png # Time series decomposition plot
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

5. **Run the Notebook:**
   Launch Jupyter Notebook to execute the analysis:
   ```bash
   jupyter notebook notebooks/Task1_Data_Preprocessing.ipynb
   ```



## **Usage**

### **1. Data Preprocessing**
The `scripts/data_preprocessing.py` script performs the following tasks:
- Fetches historical financial data for TSLA, BND, and SPY using the `yfinance` library.
- Cleans and preprocesses the data (handles missing values, ensures correct data types).
- Saves the cleaned data to `data/processed_data.csv`.

### **2. Exploratory Data Analysis (EDA)**
The `scripts/eda_utils.py` script provides functions to analyze and visualize the data:
- **Closing Prices:** Visualize trends over time.
- **Daily Returns:** Analyze volatility and daily percentage changes.
- **Volatility Analysis:** Calculate rolling means and standard deviations.
- **Time Series Decomposition:** Break down Tesla's price movements into trend, seasonal, and residual components.

### **3. Generate Reports**
The Jupyter Notebook (`Task1_Data_Preprocessing.ipynb`) combines the outputs of the above scripts to generate visualizations and textual summaries. These outputs can be used to create professional reports for stakeholders.



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

### **Visualizations**
- **Closing Prices Over Time**
- **Daily Percentage Changes**
- **Tesla's Rolling Mean and Standard Deviation**
- **Tesla's Time Series Decomposition**



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
- GitHub:https://github.com/azazh



### **Acknowledgments**
- **yfinance:** For providing access to historical financial data.
- **Pandas, Matplotlib, Statsmodels:** For data manipulation, visualization, and analysis.

