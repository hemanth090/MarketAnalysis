import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta
import altair as alt
import pandas as pd
from neo4j import GraphDatabase

# Neo4j connection details
NEO4J_URI = "neo4j+s://e540fe22.databases.neo4j.io"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = "ZA6-uStM4qmPS_oad_GIli9FOMBwPVYUZknEdMQkjZg"

class Neo4jConnection:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_stock_data(self, ticker, date, price):
        with self.driver.session() as session:
            session.run(
                "MERGE (s:Stock {ticker: $ticker}) "
                "CREATE (s)-[:HAS_PRICE]->(p:Price {date: $date, price: $price})",
                ticker=ticker, date=date.strftime("%Y-%m-%d"), price=price
            )

@st.cache_data
def fetch_stock_data(ticker, start_date, end_date):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)["Close"]
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
                # Store data in Neo4j
                neo4j_conn = Neo4jConnection(NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD)
                for date, price in data_custom_range.items():
                    neo4j_conn.create_stock_data(ticker_symbol, date, price)
                neo4j_conn.close()

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
            else:
                st.error("No data available for the selected date range and ticker symbol.")

if __name__ == "__main__":
    main()
