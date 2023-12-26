import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta

# Function to fetch stock data
def fetch_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)["Close"]
    return data

# Function to calculate total return over the period
def calculate_returns(data):
    # Calculate total return from start to end of the period
    total_return = (data.iloc[-1] / data.iloc[0] - 1)
    return total_return

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

                # Display the data and calculate returns
                st.write(f"Stock Data for {ticker_symbol} - Custom Date Range:")
                st.dataframe(data_custom_range)
                annual_return_custom = calculate_returns(data_custom_range)
                st.write(f"Annual Return based on custom date range: {annual_return_custom:.2%}")

            except Exception as e:
                st.error(f"Error: {e}. Please check the provided ticker symbol.")


if __name__ == "__main__":
    main()
