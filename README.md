# Stock Analysis App

## Overview

**Stock Analysis App** is a Streamlit application designed to fetch and analyze stock prices using Yahoo Finance data. The application stores the fetched data in a Neo4j database and visualizes it using Altair charts, helping users track stock performance over time.

## Features

- **Stock Data Fetching**: Get historical stock prices by entering the ticker symbol.
- **Data Visualization**: Interactive line chart displaying stock price trends over a specified date range.
- **Neo4j Integration**: Store fetched stock data in a Neo4j database for further analysis.
- **Downloadable Data**: Option to download the fetched stock prices as a CSV file.

## Prerequisites

- **Python** 3.6 or higher
- **Required Packages**:
  - `streamlit`
  - `yfinance`
  - `altair`
  - `pandas`
  - `neo4j`

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Stock-Analysis-App.git
   cd Stock-Analysis-App
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Neo4j Connection**:
   - Ensure you have a Neo4j database set up and replace the connection details in the code:
     ```python
     NEO4J_URI = "your_neo4j_uri"
     NEO4J_USERNAME = "your_username"
     NEO4J_PASSWORD = "your_password"
     ```

## Usage

1. **Start the Application**:
   ```bash
   streamlit run app.py
   ```

2. **Access the App**: Open your browser and go to [http://localhost:8501](http://localhost:8501).

3. **Analyze Stocks**:
   - Enter the ticker symbol (e.g., AAPL for Apple).
   - Select a date range and click "Fetch and Analyze Data" to view the stock prices and chart.

## Code Structure

- **`app.py`**: Main Streamlit application file.
- **`requirements.txt`**: Lists all package dependencies.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make and commit your changes.
4. Push to your fork and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions, suggestions, or collaboration inquiries, please reach out to:

- **Email**: naveenhemanth4@gmail.com
- **GitHub**: [hemanth090](https://github.com/hemanth090)
- **LinkedIn**: [hemanthkokkonda](https://www.linkedin.com/in/hemanthkokkonda/)
