import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from csv_json import csv_to_json

def plot_stock_data(data, view_type='daily'):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    df.set_index('date', inplace=True)

    if view_type == 'weekly':
        df = df.resample('W').agg({
            'price': 'last',
            'open': 'first',
            'hight': 'max',
            'low': 'min',
            'vol.': 'last'
        })
    elif view_type == 'monthly':
        df = df.resample('ME').agg({
            'price': 'last',
            'open': 'first',
            'hight': 'max',
            'low': 'min',
            'vol.': 'last'
        })

    def convert_volume(v):
        if isinstance(v, str):
            v = v.replace('M', 'e6').replace('K', 'e3').replace('B', 'e9')
            return float(v)
        return v

    df['vol_num'] = df['vol.'].apply(convert_volume)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True, 
                                   gridspec_kw={'height_ratios': [3, 1]})
    
    ax1.plot(df.index, df['price'], color='#0052cc', linewidth=2, label='Close Price')
    ax1.fill_between(df.index, df['price'], alpha=0.1, color='#0052cc')
    ax1.set_title(f'Stock Price Analysis ({view_type.capitalize()})', fontsize=16, pad=20)
    ax1.set_ylabel('Price', fontsize=12)
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.legend(loc='upper left')

    colors = ['#ff4d4d' if (df['price'].iloc[i] >= df['open'].iloc[i]) else '#4d79ff' 
              for i in range(len(df))]
    
    ax2.bar(df.index, df['vol_num'], color=colors, alpha=0.8, width=0.6 if view_type == 'daily' else 5)
    ax2.set_ylabel('Volume', fontsize=12)
    ax2.grid(True, linestyle='--', alpha=0.5)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()
    
if __name__ == '__main__':
    jihoo_path = "C:/Users/jihoo/Documents/Github/MarketReplay/data/NVDA_20240101-20251231.csv"
    yojun_path = "/Users/yojunsmacbookprp/Documents/GitHub/MarketReplay/data/NVDA_20240101-20251231.csv"
    
    csv_data = csv_to_json(yojun_path)
    
    plot_stock_data(csv_data, view_type='monthly')