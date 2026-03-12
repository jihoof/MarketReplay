import pandas as pd
import matplotlib.pyplot as plt
from csv_json import csv_to_json


def plot_stock(json_data, start_date, end_date, interval="day"):
    df = pd.DataFrame(json_data)

    df = df.rename(columns={"hight": "high", "price": "close"})
    
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    mask = (df["date"] >= start_date) & (df["date"] <= end_date)
    df = df.loc[mask]

    df = df.set_index("date")

    if interval == "week":
        df = df.resample("W").agg({
            "open": "first",
            "high": "max",
            "low": "min",
            "close": "last"
        })
    elif interval == "month":
        df = df.resample("M").agg({
            "open": "first",
            "high": "max",
            "low": "min",
            "close": "last"
        })

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["close"], marker="o")

    plt.title(f"Stock Price ({interval})")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)

    plt.show()

if __name__ == "__main__":

    plot_stock(
        csv_to_json("C:/Users/jihoo/Documents/Github/MarketReplay/data/NVDA_20240101-20251231.csv"),
        start_date="2024-01-01",
        end_date="2024-06-01",
        interval="day"
    )