from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

import yfinance as yf

symbol = "AAPL"
stock_data = yf.Ticker(symbol)
stock_info = stock_data.info

st.title(f"{symbol} Stock Symbol")
st.write(f"Name: {stock_info['shortName']}")
st.write(f"Country: {stock_info['country']}")
st.write(f"Sector: {stock_info['sector']}")
st.write(f"Industry: {stock_info['industry']}")
