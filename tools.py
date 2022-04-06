import streamlit as st
import pandas as pd
import numpy as np
import ta
from ta.volatility import BollingerBands


def data(token, df):
    df = pd.read_pickle('binance_data.pkl')
    st.title(f"{token}")
    df2 = df.loc[token]
    df2.sort_values(by='date', inplace=True, ascending=True)
    indicador_bb = BollingerBands(close=df2['price'], window=20, window_dev=2)
    df2['rsi'] = ta.momentum.RSIIndicator(close=df2['price'], window=14).rsi()
    df2['bb_bbh'] = indicador_bb.bollinger_hband()
    df2['bb_bbm'] = indicador_bb.bollinger_mavg()
    df2['bb_bbl'] = indicador_bb.bollinger_lband()
    #df2['avg_price'] = df['price'].mean()
    st.table(df2.sort_values(by='date', ascending=False).tail(100))