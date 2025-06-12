# ecb-analytics-forecasting

This project analyzes and forecasts economic indicators using data from the European Central Bank (ECB). The primary focus is on three key metrics: Interest Rates, Inflation, and Exchange Rates. The project includes data loading, analysis, forecasting, and visualization components.

## Project Structure

```
ecb-analytics-forecasting
├── src
│   ├── data
│   │   └── ecb_data_loader.py
│   ├── analysis
│   │   ├── interest_rate_analysis.py
│   │   ├── inflation_analysis.py
│   │   └── exchange_rate_analysis.py
│   ├── forecasting
│   │   ├── interest_rate_forecast.py
│   │   ├── inflation_forecast.py
│   │   └── exchange_rate_forecast.py
│   ├── visualization
│   │   └── plot_trends.py
│   └── main.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ecb-analytics-forecasting
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the analysis and forecasting model, execute the main script:

```
python src/main.py
```

## Components

- **Data Loading**: The `ecb_data_loader.py` file contains the `DataLoader` class, which is responsible for loading and preprocessing ECB data.

- **Analysis**:
  - `interest_rate_analysis.py`: Contains the `InterestRateAnalysis` class for analyzing interest rate trends.
  - `inflation_analysis.py`: Focuses on inflation data analysis through the `InflationAnalysis` class.
  - `exchange_rate_analysis.py`: Analyzes exchange rate movements using the `ExchangeRateAnalysis` class.

- **Forecasting**:
  - `interest_rate_forecast.py`: Provides the `InterestRateForecast` class for forecasting future interest rates.
  - `inflation_forecast.py`: Contains the `InflationForecast` class for inflation rate forecasting.
  - `exchange_rate_forecast.py`: Includes the `ExchangeRateForecast` class for exchange rate forecasting.

- **Visualization**: The `plot_trends.py` file generates visualizations of the analyzed data through the `plot_trends` function.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License.