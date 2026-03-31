import pandas as pd
import plotly.graph_objects as go
from .csv_json import load_csv_to_mongodb

def plot_stock(json_data, start_date, end_date, interval="day"):
    df = pd.DataFrame(json_data)

    df = df.rename(columns={"hight": "high", "price": "close"})
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    mask = (df["date"] >= start_date) & (df["date"] <= end_date)
    df = df.loc[mask]

    # 🔥 캔들 차트
    fig = go.Figure(data=[go.Candlestick(
        x=df['date'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close']
    )])

    # 🔥 이동평균선 추가
    df['ma20'] = df['close'].rolling(20).mean()

    fig.add_trace(go.Scatter(
        x=df['date'],
        y=df['ma20'],
        mode='lines',
        name='MA20'
    ))

    # 🔥 UI 설정 (진짜 중요)
    fig.update_layout(
        title="Stock Chart",
        xaxis_title="Date",
        yaxis_title="Price",
        template="plotly_dark",   # 트레이딩뷰 느낌
        xaxis_rangeslider_visible=False
    )

    fig.show()


if __name__ == "__main__":
    plot_stock(
        csv_to_json("C:/Users/jihoo/Documents/Github/MarketReplay/data/NVDA_20240101-20251231.csv"),
        "2024-01-01",
        "2024-06-01"
    )