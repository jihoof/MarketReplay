import pandas as pd
import matplotlib.pyplot as plt
from csv_json import csv_to_json


def plot_stock(json_data, start_date, end_date, interval="day"):
    """
    json_data : csv_to_json으로 만든 데이터
    start_date : "YYYY-MM-DD"
    end_date : "YYYY-MM-DD"
    interval : day / week / month
    """

    # DataFrame 변환
    df = pd.DataFrame(json_data)

    # 날짜 변환
    df["date"] = pd.to_datetime(df["date"])

    # 정렬
    df = df.sort_values("date")

    # 날짜 범위 필터
    mask = (df["date"] >= start_date) & (df["date"] <= end_date)
    df = df.loc[mask]

    # 인덱스 설정
    df = df.set_index("date")

    # 주 / 월 리샘플링
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

    # 그래프
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
        interval="week"
    )