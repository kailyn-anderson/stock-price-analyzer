#!/usr/bin/env python
# coding: utf-8



import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.title("Stock Price Analyzer")

ticker = st.text_input("Enter Stock Ticker (e.g. AAPL, TSLA):", "AAPL")
start_date = st.date_input("Start Date", pd.to_datetime("2024-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("2024-06-30"))

if st.button("Analyze"):
    data = yf.download(ticker, start=start_date, end=end_date)

    if data.empty:
        st.error("No data found. Check the ticker or date range.")
    else:
        data['MA_20'] = data['Close'].rolling(window=20).mean()

        st.subheader(f"{ticker} Closing Price with 20-Day Moving Average")
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(data['Close'], label='Close')
        ax.plot(data['MA_20'], label='20-Day MA', linestyle='--')
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.legend()
        st.pyplot(fig)

        st.subheader("Raw Data")
        st.dataframe(data.tail())





