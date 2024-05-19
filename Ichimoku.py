import numpy as np
import pandas as pd
import pandas_datareader as pdt
import matplotlib.pyplot as plt
import yfinance as yf

plt.style.use('ggplot')

df = yf.download("BTC-USD", start="2020-01-01", end="2022-01-01")
print(df.head(10))

plt.plot(df['Close'], ls='-', lw=1, c='k', label='Close')
plt.title('Bitcoin Price')
plt.xlabel('Time (Day)')
plt.ylabel('Price ($)')
plt.yscale('log')
plt.legend()
plt.show()

def Ichimoku(df:pd.core.frame.DataFrame, Lt:int=9, Lk:int=26, Ld:int=26, La:int=52):
    df['Tenkan-sen'] = (df['High'].rolling(Lt).max() + df['Low'].rolling(Lt).min()) / 2
    df['Kijun-sen'] = (df['High'].rolling(Lk).max() + df['Low'].rolling(Lk).min()) / 2
    df['Chikou span'] = df['Close'].shift(-Ld)
    df['Senkou span A'] = ((df['Tenkan-sen'] + df['Kijun-sen']) / 2).shift(Ld)
    df['Senkou span B'] = ((df['High'].rolling(La).max() + df['Low'].rolling(La).min()) / 2).shift(Ld)

Ichimoku(df)


plt.plot(df['Close'], ls='-', lw=1, c='k', label='Close')
plt.plot(df['Tenkan-sen'], ls='-', lw=0.8, c='r', label='Tenkan-sen')
plt.plot(df['Kijun-sen'], ls='-', lw=0.8, c='b', label='Kijun-sen')
plt.plot(df['Chikou span'], ls='--', lw=0.8, c='g', label='Chikou span')
plt.plot(df['Senkou span A'], ls='--', lw=0.8, c='g', label='Senkou span A')
plt.plot(df['Senkou span B'], ls='--', lw=0.8, c='r', label='Senkou span B')
plt.fill_between(df.index, df['Senkou span A'], df['Senkou span B'], where=(df['Senkou span A'] > df['Senkou span B']), color='lime', alpha=0.7)
plt.fill_between(df.index, df['Senkou span A'], df['Senkou span B'], where=(df['Senkou span A'] < df['Senkou span B']), color='crimson', alpha=0.7)
plt.title('Bitcoin Price + Ichimoku Indicator')
plt.xlabel('Time (Day)')
plt.ylabel('Price ($)')
plt.yscale('log')
plt.legend()
plt.show()