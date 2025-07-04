import yfinance as yf

def get_indian_stock_data(ticker, period='5y'):
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period=period)
        return df
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None
