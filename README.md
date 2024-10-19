# Stock Market Analysis App

This project is a web-based application that provides stock market analysis, allowing users to fetch historical stock price data and visualize it in an interactive chart. The app is built using `Streamlit`, `yfinance`, and `altair`.

## Features

- **Stock Ticker Search:** Users can input a valid stock ticker symbol (e.g., `AAPL` for Apple).
- **Date Range Selection:** Analyze stock prices over a specific date range.
- **Interactive Chart:** Displays the closing stock price in an interactive line chart.
- **Stock Data Table:** The fetched stock prices are displayed in a table for easy analysis.

## How It Works

1. **User Input:** The user enters a stock ticker symbol (e.g., `AAPL`) and selects a date range.
2. **Fetch Data:** The app fetches historical stock data from Yahoo Finance using the `yfinance` API.
3. **Display Results:** The stock prices are displayed in an interactive line chart and in a tabular format.

## Demo

To see the live version of the app, visit [Streamlit Cloud](https://marketanalysis.streamlit.app/).

## Installation Guide

Follow the steps below to set up the project locally.

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/yourusername/stock-market-analysis.git
cd stock-market-analysis
