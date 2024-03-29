import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta
import altair as alt
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)["Close"]
    return data

def main():
    st.title("Stock Analysis")

    ticker_symbol = st.text_input("Enter the ticker symbol (e.g., AAPL for Apple):", "AAPL")

    start_date = st.date_input("Select start date", datetime.now() - timedelta(days=365))
    end_date = st.date_input("Select end date", datetime.now())
    if st.button("Fetch and Analyze Data"):
        with st.spinner('Fetching data...'):
            try:
                data_custom_range = fetch_stock_data(ticker_symbol, start_date, end_date)

                chart_data = pd.DataFrame({"Date": data_custom_range.index, "Stock Price": data_custom_range.values})
                chart = alt.Chart(chart_data).mark_line().encode(
                    x='Date:T',
                    y='Stock Price:Q',
                    tooltip=['Date:T', 'Stock Price:Q']
                ).properties(width=800, height=400)

                col1, col2 = st.columns([2, 1])

                # Display chart 
                col1.altair_chart(chart, use_container_width=True)

                # Display the data in a dataframe in the second column
                col2.write("Stock Prices Data:")
                col2.dataframe(data_custom_range)

            except Exception as e:
                st.error(f"Error: {e}. Please check the provided ticker symbol.")

if __name__ == "__main__":
    main()
