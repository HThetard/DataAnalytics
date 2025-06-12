import numpy as np


class InflationAnalysis:
    def calculate_inflation_rate(self, consumer_price_index):
        """
        Calculate the inflation rate based on the Consumer Price Index (CPI).
        
        Parameters:
        consumer_price_index (list): A list of CPI values over time.
        
        Returns:
        list: A list of calculated inflation rates.
        """
        inflation_rates = []
        for i in range(1, len(consumer_price_index)):
            rate = (consumer_price_index[i] - consumer_price_index[i - 1]) / consumer_price_index[i - 1] * 100
            inflation_rates.append(rate)
        return inflation_rates

    def analyze_relationship_with_interest_rates(self, inflation_rates, interest_rates):
        """
        Analyze the relationship between inflation rates and interest rates.
        
        Parameters:
        inflation_rates (list): A list of inflation rates.
        interest_rates (list): A list of interest rates.
        
        Returns:
        dict: A dictionary containing correlation and other relationship metrics.
        """
        correlation = self.calculate_correlation(inflation_rates, interest_rates)
        return {
            'correlation': correlation,
            'inflation_rates': inflation_rates,
            'interest_rates': interest_rates
        }

    def calculate_correlation(self, inflation_rates, interest_rates):
        """
        Calculate the correlation between inflation rates and interest rates.
        
        Parameters:
        inflation_rates (list): A list of inflation rates.
        interest_rates (list): A list of interest rates.
        
        Returns:
        float: The correlation coefficient.
        """
        if len(inflation_rates) != len(interest_rates):
            raise ValueError("Lists must be of the same length.")
        
        return np.corrcoef(inflation_rates, interest_rates)[0, 1]