def calculate_moving_averages(df):
    df['MA_50'] = df['Close'].rolling(window=50, min_periods=1).mean()
    df['MA_200'] = df['Close'].rolling(window=200, min_periods=1).mean()
    return df
