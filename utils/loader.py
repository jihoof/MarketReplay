import pandas as pd


def parse_volume(v):
    if isinstance(v, str):
        v = v.replace(",", "").strip().upper()

        if "B" in v:
            return float(v.replace("B", "")) * 1_000_000_000
        elif "M" in v:
            return float(v.replace("M", "")) * 1_000_000
        elif "K" in v:
            return float(v.replace("K", "")) * 1_000

    try:
        return float(v)
    except:
        return 0


def load_stock_data(file_path, start_date=None, end_date=None, interval="day"):
    df = pd.read_csv(file_path)

    # 🔥 컬럼 정리 (CSV마다 다를 수 있음)
    df = df.rename(columns={
        "hight": "High",
        "price": "Close",
        "vol.": "Volume",
        "Vol.": "Volume"
    })

    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")

    # 🔥 거래량 처리
    if "Volume" in df.columns:
        df["Volume"] = df["Volume"].apply(parse_volume)

    # 🔥 날짜 필터
    if start_date:
        df = df[df["Date"] >= pd.to_datetime(start_date)]
    if end_date:
        df = df[df["Date"] <= pd.to_datetime(end_date)]

    df = df.set_index("Date")

    # 🔥 리샘플링
    if interval == "week":
        df = df.resample("W").agg({
            "Open": "first",
            "High": "max",
            "Low": "min",
            "Close": "last",
            "Volume": "sum"
        })
    elif interval == "month":
        df = df.resample("M").agg({
            "Open": "first",
            "High": "max",
            "Low": "min",
            "Close": "last",
            "Volume": "sum"
        })

    return df.dropna()