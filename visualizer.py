from matplotlib import pyplot as plt


def plot_and_save_chart(df, ticker, file_path):
    """Plot and save the chart as image"""
    plt.figure(figsize=(14, 7))
    plt.plot(df['Close'], label='Closing Price', alpha=0.5)
    plt.plot(df['MA_50'], label='50-day MA', color='orange')
    plt.plot(df['MA_200'], label='200-day MA', color='green')

    crossovers = df[df['Crossover']]
    golden = crossovers[crossovers['MA_50'] > crossovers['MA_200']]
    death = crossovers[crossovers['MA_50'] <= crossovers['MA_200']]

    plt.scatter(golden.index, golden['MA_50'], color='gold', s=100, 
                label='Golden Cross', marker='^')
    plt.scatter(death.index, death['MA_50'], color='black', s=100, 
                label='Death Cross', marker='v')

    plt.title(f'{ticker} Price with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price (₹)')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig(file_path)
    plt.close()
