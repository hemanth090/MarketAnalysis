import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta

# Function to fetch stock data
def fetch_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)["Close"]
    return data

# Streamlit app layout
def main():
    st.title("Stock Analysis")

    # Input for ticker symbol
    ticker_symbol = st.text_input("Enter the ticker symbol (e.g., AAPL for Apple):", "AAPL")

    # Input for date range
    start_date = st.date_input("Select start date", datetime.now() - timedelta(days=365))
    end_date = st.date_input("Select end date", datetime.now())

    # Fetch and display data button
    if st.button("Fetch and Analyze Data"):
        with st.spinner('Fetching data...'):
            try:
                # Fetch data for the selected date range
                data_custom_range = fetch_stock_data(ticker_symbol, start_date, end_date)

                # Display the data
                st.write(f"Stock Data for {ticker_symbol} - Custom Date Range:")
                st.dataframe(data_custom_range)

            except Exception as e:
                st.error(f"Error: {e}. Please check the provided ticker symbol.")


if __name__ == "__main__":
    main()
