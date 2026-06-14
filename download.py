import yfinance as yf

data = yf.download(
    "AAPL",
    start="2020-01-01",
    end="2026-06-14"
)

data.to_csv("Apple_Stock_Data.csv")

print(data.head())