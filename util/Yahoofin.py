import yfinance as yf

def get_stock_prices(tickers):
    """
    Get stock prices for a set of tickers of Brazilian enterprises listed in B3.
    
    Parameters:
    tickers (list): List of ticker symbols.
    
    Returns:
    dict: Dictionary with ticker symbols as keys and their corresponding stock prices as values.
    """
    stock_prices = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        stock_info = stock.history(period="1d")
        if not stock_info.empty:
            stock_prices[ticker] = stock_info['Close'].iloc[-1]
        else:
            stock_prices[ticker] = None
    return stock_prices


# Example usage
if __name__ == "__main__":
    tickers = ["PETR4.SA", "VALE3.SA", "ITUB4.SA"]
    prices = get_stock_prices(tickers)
    for ticker, price in prices.items():
        print(f"{ticker}: {price}")
