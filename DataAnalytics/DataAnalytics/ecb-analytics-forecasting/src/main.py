# main.py

import pandas as pd
from data.ecb_data_loader import DataLoader
from analysis.interest_rate_analysis import InterestRateAnalysis
from analysis.inflation_analysis import InflationAnalysis
from analysis.exchange_rate_analysis import ExchangeRateAnalysis
from forecasting.interest_rate_forecast import InterestRateForecast
from forecasting.inflation_forecast import InflationForecast
from forecasting.exchange_rate_forecast import ExchangeRateForecast
from visualization.plot_trends import plot_trends

def main():
    # Load and preprocess ECB data
    data_loader = DataLoader("C:/Users/Hein/Desktop/DataAnalytics/DataAnalytics/ecb-analytics-forecasting/src/ecb_data.csv")
    data = data_loader.load_data()
    preprocessed_data = data_loader.preprocess_data()

    # Analyze interest rates
    interest_rate_analysis = InterestRateAnalysis(preprocessed_data)
    interest_rate_trends = interest_rate_analysis.calculate_trends()
    interest_rate_analysis.compare_with_inflation()

    # Analyze inflation
    inflation_analysis = InflationAnalysis(preprocessed_data)
    inflation_rate = inflation_analysis.calculate_inflation_rate()
    inflation_analysis.analyze_relationship_with_interest_rates()

    # Analyze exchange rates
    exchange_rate_analysis = ExchangeRateAnalysis(preprocessed_data)
    exchange_rate_trends = exchange_rate_analysis.calculate_exchange_rate_trends()
    exchange_rate_analysis.compare_with_inflation()

    # Forecast future rates
    interest_rate_forecast = InterestRateForecast(preprocessed_data)
    future_interest_rates = interest_rate_forecast.forecast_future_rates()
    interest_rate_forecast.evaluate_forecast_accuracy()

    inflation_forecast = InflationForecast(preprocessed_data)
    future_inflation = inflation_forecast.forecast_inflation()
    inflation_forecast.assess_forecast_accuracy()

    exchange_rate_forecast = ExchangeRateForecast(preprocessed_data)
    future_exchange_rates = exchange_rate_forecast.forecast_exchange_rate()
    exchange_rate_forecast.validate_forecast()

    # Visualize trends
    plot_trends(interest_rate_trends, inflation_rate, exchange_rate_trends)

if __name__ == "__main__":
    main()