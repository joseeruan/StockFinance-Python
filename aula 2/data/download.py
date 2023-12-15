import yfinance as yf
import pandas as pd

def downloadData (ticker:str) -> pd.DataFrame:

    """Download data from Yahoo Finances

    Args:
        ticker (str): the ticker of financial asset.

    Returns:
        pd.DataFrame: A datafram retrieved from Yahoo Finances.
    """

    data = yf.download(ticker)

    return data