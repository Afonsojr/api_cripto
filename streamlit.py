import streamlit as st
import pandas as pd
import numpy as np
import ta
from ta.volatility import BollingerBands

from tools import data


def page_body():
    st.sidebar.title("Sidebar")
    token = st.sidebar.selectbox("Select a coin", ["BTCUSDT", "BNBUSDT", "ETHUSDT"])
    if token == "BTCUSDT":
        data(token)

    if token == "BNBUSDT":
        data(token)
    
    if token == "ETHUSDT":
        data(token)

        
def main():
    page_body()
    return None


if __name__ == '__main__':
    main()