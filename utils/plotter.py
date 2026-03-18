import matplotlib.pyplot as plt


def plot_stock(df, title="Stock Chart"):
    plt.figure(figsize=(12, 6))

    # 🔥 종가 라인
    plt.plot(df.index, df["Close"], label="Close", linewidth=2)

    # 🔥 이동평균선
    df["MA20"] = df["Close"].rolling(20).mean()
    df["MA5"] = df["Close"].rolling(5).mean()

    plt.plot(df.index, df["MA5"], linestyle="--", label="MA5")
    plt.plot(df.index, df["MA20"], linestyle="--", label="MA20")

    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()