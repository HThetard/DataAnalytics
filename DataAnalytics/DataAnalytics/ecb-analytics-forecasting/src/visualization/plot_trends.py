def plot_trends(interest_rate_data, inflation_data, exchange_rate_data):
    import matplotlib.pyplot as plt
    import pandas as pd

    # Create a figure with subplots
    fig, axs = plt.subplots(3, 1, figsize=(10, 15))

    # Plot Interest Rate Trends
    axs[0].plot(interest_rate_data['Date'], interest_rate_data['Rate'], color='blue', label='Interest Rate')
    axs[0].set_title('Interest Rate Trends')
    axs[0].set_xlabel('Date')
    axs[0].set_ylabel('Interest Rate (%)')
    axs[0].legend()
    axs[0].grid()

    # Plot Inflation Trends
    axs[1].plot(inflation_data['Date'], inflation_data['Inflation'], color='orange', label='Inflation Rate')
    axs[1].set_title('Inflation Trends')
    axs[1].set_xlabel('Date')
    axs[1].set_ylabel('Inflation Rate (%)')
    axs[1].legend()
    axs[1].grid()

    # Plot Exchange Rate Trends
    axs[2].plot(exchange_rate_data['Date'], exchange_rate_data['Exchange Rate'], color='green', label='Exchange Rate')
    axs[2].set_title('Exchange Rate Trends')
    axs[2].set_xlabel('Date')
    axs[2].set_ylabel('Exchange Rate')
    axs[2].legend()
    axs[2].grid()

    # Adjust layout
    plt.tight_layout()
    plt.show()