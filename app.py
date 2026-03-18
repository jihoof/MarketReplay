from flask import Flask, request, jsonify, render_template
import pandas as pd
import os

app = Flask(__name__)

# 🔥 CSV 경로 안전하게 잡기
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "data", "NVDA_20240101-20251231.csv")


# 🔥 거래량 변환
def parse_volume(v):
    if isinstance(v, str):
        v = v.strip().upper()

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

def load_data(interval):
    df = pd.read_csv(FILE_PATH)

    df = df.rename(columns={"hight": "High", "Price": "Close"})
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")

    # 거래량 처리
    if "Vol." in df.columns:
        df["Volume"] = df["Vol."].apply(parse_volume)

    df = df.set_index("Date")

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

    df = df.reset_index()

    return df.to_dict(orient="records")


# 🔥 메인 페이지
@app.route("/")
def home():
    return render_template("index.html")


# 🔥 데이터 API
@app.route("/data")
def data():
    interval = request.args.get("interval", "day")
    return jsonify(load_data(interval))


if __name__ == "__main__":
    app.run(debug=True)