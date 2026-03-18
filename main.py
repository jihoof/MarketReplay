import os
from utils.loader import load_stock_data
from utils.plotter import plot_stock

# 🔥 경로 자동 처리 (안 터짐)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "data", "NVDA_20240101-20251231.csv")


if __name__ == "__main__":
    df = load_stock_data(
        FILE_PATH,
        start_date="2024-01-01",
        end_date="2024-06-01",
        interval="day"   # "day", "week", "month"
    )

    print(df.head())  # 디버깅용

    plot_stock(df, title="NVDA Stock")