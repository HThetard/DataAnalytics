import pandas as pd
import matplotlib.pyplot as plt

class ExchangeRateAnalysis:
    def calculate_exchange_rate_trends(self, data):
        """
        Calculate and return the rolling mean (trend) of exchange rates.
        """
        # Assuming 'ExchangeRate' column exists
        trends = data['ExchangeRate'].rolling(window=3, min_periods=1).mean()
        return trends

    def compare_with_inflation(self, exchange_rate_data, inflation_data):
        """
        Plot exchange rates and inflation rates on the same graph to compare trends.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(exchange_rate_data.index, exchange_rate_data['ExchangeRate'], label='Exchange Rate', color='blue')
        plt.plot(inflation_data.index, inflation_data['Inflation'], label='Inflation Rate', color='red')
        plt.title('Exchange Rate vs Inflation Rate')
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.legend()
        plt.tight_layout()
        plt.show()