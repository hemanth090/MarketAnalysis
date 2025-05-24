import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta
import altair as alt
import pandas as pd

@st.cache_data
def fetch_stock_data(ticker, start_date, end_date):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        return data
    except Exception as e:
        st.error(f"Could not fetch data for {ticker}: {e}")
        return None

def main():
    st.title("Stock Analysis")

    ticker_symbol = st.text_input("Enter the ticker symbol (e.g., AAPL for Apple):", "AAPL")

    start_date = st.date_input("Select start date", datetime.now() - timedelta(days=365))
    end_date = st.date_input("Select end date", datetime.now())
    
    if st.button("Fetch and Analyze Data"):
        with st.spinner('Fetching data...'):
            data_custom_range = fetch_stock_data(ticker_symbol, start_date, end_date)

            if data_custom_range is not None and not data_custom_range.empty:
                # Reset index to make Date a column
                data_custom_range = data_custom_range.reset_index()
                
                # Create chart using Close prices
                chart = alt.Chart(data_custom_range).mark_line().encode(
                    x='Date:T',
                    y='Close:Q',
                    tooltip=['Date:T', 'Close:Q']
                ).properties(width=800, height=400)

                col1, col2 = st.columns([2, 1])

                # Display chart 
                col1.altair_chart(chart, use_container_width=True)

                # Display the data in a dataframe in the second column
                col2.write("Stock Prices Data:")
                col2.dataframe(data_custom_range)

                # Download option for the displayed data
                csv = data_custom_range.to_csv(index=False).encode('utf-8')
                col2.download_button("Download CSV", csv, "stock_data.csv", "text/csv")
            else:
                st.error("No data available for the selected date range and ticker symbol.")

if __name__ == "__main__":
    main()
