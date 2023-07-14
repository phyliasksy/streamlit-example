import yfinance as yf
import streamlit as st

symbol = "AAPL"
stock_data = yf.Ticker(symbol)
stock_info = stock_data.info

st.title(f"{symbol} Stock Symbol")
st.write(f"Name: {stock_info['shortName']}")
st.write(f"Country: {stock_info['country']}")
st.write(f"Sector: {stock_info['sector']}")
st.write(f"Industry: {stock_info['industry']}")
