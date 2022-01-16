import yfinance as yf
import datetime as dt
import pandas as pd



def indices(symbol, period, start, end):
    rawData = yf.Ticker(symbol)
    return rawData.history(interval=period, start=start, end=end)["Close"]

def currency(symbol, period, start, end):
    rawData = yf.Ticker(symbol)
    return rawData.history(interval=period, start=start, end=end).drop(["Dividends", "Stock Splits", "Volume"], axis=1)

def next_candle(symbol, period, start, end, df):
    rawData = yf.Ticker(symbol)
    NextCandle = rawData.history(interval=period, start=start, end=end)[["Close"]]
    NextCandle = NextCandle[:df.shape[0]]
    NextCandle.set_index(df.index, inplace=True)
    df["Next Candle"] = NextCandle["Close"]

