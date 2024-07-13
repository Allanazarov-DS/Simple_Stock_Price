import pandas as pd
import yfinance as yf
import streamlit as st

st.write("""

# Sample stock Price App
         
#### Shown are the stock ***closing*** and ***volume*** price of Google!

""")

# define the tickersymbol
tickersymbol = 'GOOGL'

# get data on this ticker
tickerdata = yf.Ticker(tickersymbol)

tickerdf = tickerdata.history(period = '1d', start = '2010-07-13', end = '2024-07-13')

# Open  High  Low  Close   Volume  Dividends  Stock  Splits   

st.write("""
         
### Closing price
         
""")

st.line_chart(tickerdf.Close)

st.write("""
         
### Volume Price
         
""")

st.line_chart(tickerdf.Volume)

st.write("""
         
#### Shown are the stock ***closing*** and ***volume*** price of Apple!

""")

# define the tickersymbol
tickersymbol = 'AAPL'

# get data on this ticker
tickerdata2 = yf.Ticker(tickersymbol)

tickerdf2 = tickerdata2.history(period = '1d', start = '2010-07-13', end = '2024-07-13')

# Open  High  Low  Close   Volume  Dividends  Stock  Splits   

st.write("""
         
### Closing price
         
""")

st.line_chart(tickerdf2.Close)

st.write("""
         
### Volume Price
         
""")

st.line_chart(tickerdf.Volume)