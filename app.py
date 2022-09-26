from tvDatafeed import TvDatafeed,Interval
import pandas as pd
import cufflinks as cf
import numpy as np
import chart_studio.plotly as py
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import streamlit as st
from locale import currency

pio.templates.default = "plotly_dark"

tv = TvDatafeed()

#FOREX

#USDSEK
USD_SEK = tv.get_hist('USDSEK','OANDA',interval=Interval.in_daily,n_bars=300)
USDSEK_Mean = USD_SEK["close"].mean()

#EURSEK
EUR_USD = tv.get_hist('EURUSD','OANDA',interval=Interval.in_daily,n_bars=300)
EURUSD_Mean = EUR_USD["close"].mean()

#VALOUR

#VALOUR BTC ZERO SEK
pd_BTC_ZERO_SEK=tv.get_hist('BTC.ZERO.SEK','NGM',interval=Interval.in_daily,n_bars=300)
pd_BTC_ZERO_SEK["averageprice"] = (pd_BTC_ZERO_SEK["high"] + pd_BTC_ZERO_SEK["open"] + pd_BTC_ZERO_SEK["close"] + pd_BTC_ZERO_SEK["low"]) /4
pd_BTC_ZERO_SEK["turnover"] = (pd_BTC_ZERO_SEK["averageprice"] * pd_BTC_ZERO_SEK["volume"])/USDSEK_Mean
pd_BTC_ZERO_SEK["turnover"].astype(int)

#VALOUR ETH ZERO SEK
pd_ETH_ZERO_SEK=tv.get_hist('ETH.ZERO.SEK','NGM',interval=Interval.in_daily,n_bars=300)
pd_ETH_ZERO_SEK["averageprice"] = (pd_ETH_ZERO_SEK["high"] + pd_ETH_ZERO_SEK["open"] + pd_ETH_ZERO_SEK["close"] + pd_ETH_ZERO_SEK["low"]) /4
pd_ETH_ZERO_SEK["turnover"] = (pd_ETH_ZERO_SEK["averageprice"] * pd_ETH_ZERO_SEK["volume"])/USDSEK_Mean
pd_ETH_ZERO_SEK["turnover"].astype(int)

#VALOUR CARDANO SEK
pd_VALOUR_CARDANO_SEK=tv.get_hist('VALOUR.CARDANO.SEK','NGM',interval=Interval.in_daily,n_bars=300)
pd_VALOUR_CARDANO_SEK["averageprice"] = (pd_VALOUR_CARDANO_SEK["high"] + pd_VALOUR_CARDANO_SEK["open"] + pd_VALOUR_CARDANO_SEK["close"] + pd_VALOUR_CARDANO_SEK["low"]) /4
pd_VALOUR_CARDANO_SEK["turnover"] = (pd_VALOUR_CARDANO_SEK["averageprice"] * pd_VALOUR_CARDANO_SEK["volume"])/USDSEK_Mean
pd_VALOUR_CARDANO_SEK["turnover"].astype(int)

#VALOUR SOLANA SEK
pd_VALOUR_SOLANA_SEK=tv.get_hist('VALOUR.SOLANA.SEK','NGM',interval=Interval.in_daily,n_bars=300)
pd_VALOUR_SOLANA_SEK["averageprice"] = (pd_VALOUR_SOLANA_SEK["high"] + pd_VALOUR_SOLANA_SEK["open"] + pd_VALOUR_SOLANA_SEK["close"] + pd_VALOUR_SOLANA_SEK["low"]) /4
pd_VALOUR_SOLANA_SEK["turnover"] = (pd_VALOUR_SOLANA_SEK["averageprice"] * pd_VALOUR_SOLANA_SEK["volume"])/USDSEK_Mean
pd_VALOUR_SOLANA_SEK["turnover"].astype(int)

#VALOUR POLKADOT SEK
pd_VALOUR_POLKADOT_SEK=tv.get_hist('VALOUR.POLKADOT.SEK','NGM',interval=Interval.in_daily,n_bars=300)
pd_VALOUR_POLKADOT_SEK["averageprice"] = (pd_VALOUR_POLKADOT_SEK["high"] + pd_VALOUR_POLKADOT_SEK["open"] + pd_VALOUR_POLKADOT_SEK["close"] + pd_VALOUR_POLKADOT_SEK["low"]) /4
pd_VALOUR_POLKADOT_SEK["turnover"] = (pd_VALOUR_POLKADOT_SEK["averageprice"] * pd_VALOUR_POLKADOT_SEK["volume"])/USDSEK_Mean
pd_VALOUR_POLKADOT_SEK["turnover"].astype(int)

#VALOUR UNISWAP SEK
pd_VALOUR_UNISWAP_SEK=tv.get_hist('VALOUR.UNISWAP.SEK','NGM',interval=Interval.in_daily,n_bars=300)
pd_VALOUR_UNISWAP_SEK["averageprice"] = (pd_VALOUR_UNISWAP_SEK["high"] + pd_VALOUR_UNISWAP_SEK["open"] + pd_VALOUR_UNISWAP_SEK["close"] + pd_VALOUR_UNISWAP_SEK["low"]) /4
pd_VALOUR_UNISWAP_SEK["turnover"] = (pd_VALOUR_UNISWAP_SEK["averageprice"] * pd_VALOUR_UNISWAP_SEK["volume"])/USDSEK_Mean
pd_VALOUR_UNISWAP_SEK["turnover"].astype(int)

#VALOUR AVALANCHE SEK
pd_VALOUR_AVLANCHE_SEK=tv.get_hist('VALOUR.AVALANCHE.AVAX.SEK','NGM',interval=Interval.in_daily,n_bars=300)
pd_VALOUR_AVLANCHE_SEK["averageprice"] = (pd_VALOUR_AVLANCHE_SEK["high"] + pd_VALOUR_AVLANCHE_SEK["open"] + pd_VALOUR_AVLANCHE_SEK["close"] + pd_VALOUR_AVLANCHE_SEK["low"]) /4
pd_VALOUR_AVLANCHE_SEK["turnover"] = (pd_VALOUR_AVLANCHE_SEK["averageprice"] * pd_VALOUR_AVLANCHE_SEK["volume"])/USDSEK_Mean
pd_VALOUR_AVLANCHE_SEK["turnover"].astype(int)

#Valour Products
Valour = pd.concat([pd_BTC_ZERO_SEK, pd_ETH_ZERO_SEK, pd_VALOUR_CARDANO_SEK, pd_VALOUR_POLKADOT_SEK, pd_VALOUR_UNISWAP_SEK, pd_VALOUR_AVLANCHE_SEK])
Valour['Date'] = pd.to_datetime(Valour.index.date)
Valour.set_index(Valour['Date'], drop=True, inplace=True)
Valour.drop(['Date'], axis=1, inplace=True)

#Valour Products Pivot table
pivot_Valour = (
    Valour.pivot_table(index=Valour.index,
                   columns='symbol',
                   values='turnover',
                   aggfunc='first')
        .rename_axis(columns=None)
        .reset_index()
        .fillna(0)
        .astype(int)
)
pivot_Valour.index = pd.to_datetime(pivot_Valour["Date"])
pivot_Valour.drop(["Date"], axis=1, inplace=True)
Valour_Monthly = pivot_Valour.groupby(pd.Grouper(freq='M')).sum()
Valour_Monthly = Valour_Monthly.drop(Valour_Monthly.index[Valour_Monthly.index.year == 2021])
sum_valour = Valour_Monthly.sum(axis=1)
sum_valour = sum_valour.astype(int).map('${:,.0f}'.format)
# VALOUR CHART MONTHLY

fig_valour_monthly = px.bar(Valour_Monthly, x=Valour_Monthly.index,
y=Valour_Monthly.columns,
labels={
    'value':'Turnover $',
    'datetime':'Date'
})

fig_valour_monthly.update_layout(
title={
    'text': 'VALOUR PRODUCTS MONTHLY TURNOVER',
    'y':0.95,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'
})
fig_valour_monthly.update_xaxes(
    dtick='M1',
    showgrid=True,
    tickformat='%b\n%Y',
    ticklabelmode='period'
)
#show total value on top of each bar

fig_valour_monthly.add_trace(go.Scatter(
    x=Valour_Monthly.index,
    y=sum_valour,
    text=sum_valour,
    mode='text',
    textposition='top center',
    textfont=dict(
        size=12,
        color='white'
    ),
    showlegend=False
))

#XBT

#XBT BTC Tracker One
pd_BTC_XBT=tv.get_hist('BITCOIN_XBT','OMXSTO',interval=Interval.in_daily,n_bars=300)
pd_BTC_XBT["averageprice"] = (pd_BTC_XBT["high"] + pd_BTC_XBT["open"] + pd_BTC_XBT["close"] + pd_BTC_XBT["low"]) /4
pd_BTC_XBT["turnover"] = (pd_BTC_XBT["averageprice"] * pd_BTC_XBT["volume"])/USDSEK_Mean
pd_BTC_XBT["turnover"].astype(int)

#XBT BTC Euro Tracker One
pd_BTCE_XBT=tv.get_hist('BITCOIN_XBTE','OMXSTO',interval=Interval.in_daily,n_bars=300)
pd_BTCE_XBT["averageprice"] = (pd_BTCE_XBT["high"] + pd_BTCE_XBT["open"] + pd_BTCE_XBT["close"] + pd_BTCE_XBT["low"]) /4
pd_BTCE_XBT["turnover"] = (pd_BTCE_XBT["averageprice"] * pd_BTCE_XBT["volume"])*EURUSD_Mean
pd_BTCE_XBT["turnover"].astype(int)

#XBT ETH Tracker One
pd_ETH_XBT=tv.get_hist('ETHEREUM_XBT','OMXSTO',interval=Interval.in_daily,n_bars=300)
pd_ETH_XBT["averageprice"] = (pd_ETH_XBT["high"] + pd_ETH_XBT["open"] + pd_ETH_XBT["close"] + pd_ETH_XBT["low"]) /4
pd_ETH_XBT["turnover"] = (pd_ETH_XBT["averageprice"] * pd_ETH_XBT["volume"])/USDSEK_Mean
pd_ETH_XBT["turnover"].astype(int)

#XBT ETH Euro Tracker One
pd_ETHE_XBT=tv.get_hist('ETHEREUM_XBTE','OMXSTO',interval=Interval.in_daily,n_bars=300)
pd_ETHE_XBT["averageprice"] = (pd_ETHE_XBT["high"] + pd_ETHE_XBT["open"] + pd_ETHE_XBT["close"] + pd_ETHE_XBT["low"]) /4
pd_ETHE_XBT["turnover"] = (pd_ETHE_XBT["averageprice"] * pd_ETHE_XBT["volume"])*EURUSD_Mean
pd_ETHE_XBT["turnover"].astype(int)

#XBT Products
XBT = pd.concat([pd_BTC_XBT, pd_ETH_XBT, pd_BTCE_XBT, pd_ETHE_XBT])
XBT['Date'] = pd.to_datetime(XBT.index.date)
XBT.set_index(XBT['Date'], drop=True, inplace=True)
XBT.drop(['Date'], axis=1, inplace=True)

#XBT Products Pivot table
pivot_XBT = (
    XBT.pivot_table(index=XBT.index,
                   columns='symbol',
                   values='turnover',
                   aggfunc='first')
        .rename_axis(columns=None)
        .reset_index()
        .fillna(0)
)
pivot_XBT.index = pd.to_datetime(pivot_XBT["Date"])
pivot_XBT.drop(["Date"], axis=1, inplace=True)
XBT_Monthly = pivot_XBT.groupby(pd.Grouper(freq='M')).sum()
#drop year 2021
XBT_Monthly = XBT_Monthly.drop(XBT_Monthly.index[XBT_Monthly.index.year == 2021])
sum_xbt = XBT_Monthly.sum(axis=1)
sum_xbt = sum_xbt.astype(int).map('${:,.0f}'.format)

# XBT CHART MONTHLY

fig_xbt_monthly = px.bar(XBT_Monthly, x=XBT_Monthly.index,
y=XBT_Monthly.columns,
labels={
    'value':'Turnover $',
    'datetime':'Date'
})

fig_xbt_monthly.update_layout(
title={
    'text': 'XBT PRODUCTS MONTHLY TURNOVER',
    'y':0.95,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'
})
fig_xbt_monthly.update_xaxes(
    dtick='M1',
    showgrid=True,
    tickformat='%b\n%Y',
    ticklabelmode='period'
)

#show total value on top of each bar

fig_xbt_monthly.add_trace(go.Scatter
    (x=XBT_Monthly.index,
    y=sum_xbt,
    text=sum_xbt,
    mode='text',
    textposition='top center',
    textfont=dict(
        size=12,
        color='white'
    ),
    showlegend=False
))

#21SHARES XETRA

#21SHARES XETRA BITCOIN
pd_21SHARES_XETRA_BTC=tv.get_hist('2BTC','XETR',interval=Interval.in_daily,n_bars=300)
pd_21SHARES_XETRA_BTC["averageprice"] = (pd_21SHARES_XETRA_BTC["high"] + pd_21SHARES_XETRA_BTC["open"] + pd_21SHARES_XETRA_BTC["close"] + pd_21SHARES_XETRA_BTC["low"]) /4
pd_21SHARES_XETRA_BTC["turnover"] = (pd_21SHARES_XETRA_BTC["averageprice"] * pd_21SHARES_XETRA_BTC["volume"])*EURUSD_Mean
pd_21SHARES_XETRA_BTC["turnover"].astype(int)

#21SHARES XETRA ETHEREUM
pd_21SHARES_XETRA_ETH=tv.get_hist('ETHA','XETR',interval=Interval.in_daily,n_bars=300)
pd_21SHARES_XETRA_ETH["averageprice"] = (pd_21SHARES_XETRA_ETH["high"] + pd_21SHARES_XETRA_ETH["open"] + pd_21SHARES_XETRA_ETH["close"] + pd_21SHARES_XETRA_ETH["low"]) /4
pd_21SHARES_XETRA_ETH["turnover"] = (pd_21SHARES_XETRA_ETH["averageprice"] * pd_21SHARES_XETRA_ETH["volume"])*EURUSD_Mean
pd_21SHARES_XETRA_ETH["turnover"].astype(int)

#21SHARES XETRA CARDANO
pd_21SHARES_XETRA_ADA=tv.get_hist('ADAA','XETR',interval=Interval.in_daily,n_bars=300)
pd_21SHARES_XETRA_ADA["averageprice"] = (pd_21SHARES_XETRA_ADA["high"] + pd_21SHARES_XETRA_ADA["open"] + pd_21SHARES_XETRA_ADA["close"] + pd_21SHARES_XETRA_ADA["low"]) /4
pd_21SHARES_XETRA_ADA["turnover"] = (pd_21SHARES_XETRA_ADA["averageprice"] * pd_21SHARES_XETRA_ADA["volume"])*EURUSD_Mean
pd_21SHARES_XETRA_ADA["turnover"].astype(int)

#21SHARES XETRA SOLANA
pd_21SHARES_XETRA_SOL=tv.get_hist('ASOL','XETR',interval=Interval.in_daily,n_bars=300)
pd_21SHARES_XETRA_SOL["averageprice"] = (pd_21SHARES_XETRA_SOL["high"] + pd_21SHARES_XETRA_SOL["open"] + pd_21SHARES_XETRA_SOL["close"] + pd_21SHARES_XETRA_SOL["low"]) /4
pd_21SHARES_XETRA_SOL["turnover"] = (pd_21SHARES_XETRA_SOL["averageprice"] * pd_21SHARES_XETRA_SOL["volume"])*EURUSD_Mean
pd_21SHARES_XETRA_SOL["turnover"].astype(int)

#21SHARES XETRA POLKADOT
pd_21SHARES_XETRA_DOT=tv.get_hist('ADOT','XETR',interval=Interval.in_daily,n_bars=300)
pd_21SHARES_XETRA_DOT["averageprice"] = (pd_21SHARES_XETRA_DOT["high"] + pd_21SHARES_XETRA_DOT["open"] + pd_21SHARES_XETRA_DOT["close"] + pd_21SHARES_XETRA_DOT["low"]) /4
pd_21SHARES_XETRA_DOT["turnover"] = (pd_21SHARES_XETRA_DOT["averageprice"] * pd_21SHARES_XETRA_DOT["volume"])*EURUSD_Mean
pd_21SHARES_XETRA_DOT["turnover"].astype(int)

#21Shares Xetra Products
Shares21_xetr = pd.concat([pd_21SHARES_XETRA_ADA, pd_21SHARES_XETRA_BTC, pd_21SHARES_XETRA_DOT, pd_21SHARES_XETRA_ETH, pd_21SHARES_XETRA_SOL])
Shares21_xetr['Date'] = pd.to_datetime(Shares21_xetr.index.date)
Shares21_xetr.set_index(Shares21_xetr['Date'], drop=True, inplace=True)
Shares21_xetr.drop(['Date'], axis=1, inplace=True)

#21Shares Xetra Products Pivot table
pivot_Shares21_xetr = (
    Shares21_xetr.pivot_table(index=Shares21_xetr.index,
                   columns='symbol',
                   values='turnover',
                   aggfunc='first')
        .rename_axis(columns=None)
        .reset_index()
        .fillna(0)
)
pivot_Shares21_xetr.index = pd.to_datetime(pivot_Shares21_xetr["Date"])
pivot_Shares21_xetr.drop(["Date"], axis=1, inplace=True)
shares21_xetr_Monthly = pivot_Shares21_xetr.groupby(pd.Grouper(freq='M')).sum()
#drop year 2021
shares21_xetr_Monthly = shares21_xetr_Monthly.drop(shares21_xetr_Monthly.index[shares21_xetr_Monthly.index.year == 2021])
sum_shares21_xetr = shares21_xetr_Monthly.sum(axis=1)
sum_shares21_xetr = sum_shares21_xetr.astype(int).map('${:,.0f}'.format)

### 21Shares XETRA CHART MONTHLY

fig_shares21_xetr_monthly = px.bar(shares21_xetr_Monthly, x=shares21_xetr_Monthly.index,
y=shares21_xetr_Monthly.columns,
labels={
    'value':'Turnover $',
    'datetime':'Date'
})

fig_shares21_xetr_monthly.update_layout(
title={
    'text': '21Shares XETRA PRODUCTS MONTHLY TURNOVER',
    'y':0.95,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'
})
fig_shares21_xetr_monthly.update_xaxes(
    dtick='M1',
    showgrid=True,
    tickformat='%b\n%Y',
    ticklabelmode='period'
)

#show total value on top of each bar

fig_shares21_xetr_monthly.add_trace(go.Scatter
    (x=shares21_xetr_Monthly.index,
    y=sum_shares21_xetr,
    text=sum_shares21_xetr,
    mode='text',
    textposition='top center',
    textfont=dict(
        size=12,
        color='white'
    ),
    showlegend=False
))

#21Shares SIX

#21SHARES SIX BITCOIN
pd_21SHARES_SIX_BTC=tv.get_hist('ABTC.USD','SIX',interval=Interval.in_daily,n_bars=300)
pd_21SHARES_SIX_BTC["averageprice"] = (pd_21SHARES_SIX_BTC["high"] + pd_21SHARES_SIX_BTC["open"] + pd_21SHARES_SIX_BTC["close"] + pd_21SHARES_SIX_BTC["low"]) /4
pd_21SHARES_SIX_BTC["turnover"] = (pd_21SHARES_SIX_BTC["averageprice"] * pd_21SHARES_SIX_BTC["volume"])
pd_21SHARES_SIX_BTC["turnover"].astype(int)

#21SHARES SIX ETHEREUM
pd_21SHARES_SIX_ETH=tv.get_hist('AETH.USD','SIX',interval=Interval.in_daily,n_bars=300)
pd_21SHARES_SIX_ETH["averageprice"] = (pd_21SHARES_SIX_ETH["high"] + pd_21SHARES_SIX_ETH["open"] + pd_21SHARES_SIX_ETH["close"] + pd_21SHARES_SIX_ETH["low"]) /4
pd_21SHARES_SIX_ETH["turnover"] = (pd_21SHARES_SIX_ETH["averageprice"] * pd_21SHARES_SIX_ETH["volume"])
pd_21SHARES_SIX_ETH["turnover"].astype(int)

#21SHARES SIX SOLANA
pd_21SHARES_SIX_SOL=tv.get_hist('ASOL.USD','SIX',interval=Interval.in_daily,n_bars=300)
pd_21SHARES_SIX_SOL["averageprice"] = (pd_21SHARES_SIX_SOL["high"] + pd_21SHARES_SIX_SOL["open"] + pd_21SHARES_SIX_SOL["close"] + pd_21SHARES_SIX_SOL["low"]) /4
pd_21SHARES_SIX_SOL["turnover"] = (pd_21SHARES_SIX_SOL["averageprice"] * pd_21SHARES_SIX_SOL["volume"])
pd_21SHARES_SIX_SOL["turnover"].astype(int)

#21SHARES SIX CARDANO
pd_21SHARES_SIX_ADA=tv.get_hist('AADA.USD','SIX',interval=Interval.in_daily,n_bars=300)
pd_21SHARES_SIX_ADA["averageprice"] = (pd_21SHARES_SIX_ADA["high"] + pd_21SHARES_SIX_ADA["open"] + pd_21SHARES_SIX_ADA["close"] + pd_21SHARES_SIX_ADA["low"]) /4
pd_21SHARES_SIX_ADA["turnover"] = (pd_21SHARES_SIX_ADA["averageprice"] * pd_21SHARES_SIX_ADA["volume"])
pd_21SHARES_SIX_ADA["turnover"].astype(int)

#21SHARES SIX POLKADOT
pd_21SHARES_SIX_DOT=tv.get_hist('ADOT.USD','SIX',interval=Interval.in_daily,n_bars=300)
pd_21SHARES_SIX_DOT["averageprice"] = (pd_21SHARES_SIX_DOT["high"] + pd_21SHARES_SIX_DOT["open"] + pd_21SHARES_SIX_DOT["close"] + pd_21SHARES_SIX_DOT["low"]) /4
pd_21SHARES_SIX_DOT["turnover"] = (pd_21SHARES_SIX_DOT["averageprice"] * pd_21SHARES_SIX_DOT["volume"])
pd_21SHARES_SIX_DOT["turnover"].astype(int)

#21Shares Six PRODUCTS
Shares21_six = pd.concat([pd_21SHARES_SIX_ADA, pd_21SHARES_SIX_BTC, pd_21SHARES_SIX_DOT, pd_21SHARES_SIX_ETH, pd_21SHARES_SIX_SOL])
Shares21_six['Date'] = pd.to_datetime(Shares21_six.index.date)
Shares21_six.set_index(Shares21_six['Date'], drop=True, inplace=True)
Shares21_six.drop(['Date'], axis=1, inplace=True)

#21Shares Six Pivot
pivot_Shares21_six = (
    Shares21_six.pivot_table(index=Shares21_six.index,
                   columns='symbol',
                   values='turnover',
                   aggfunc='first')
        .rename_axis(columns=None)
        .reset_index()
        .fillna(0)
)
pivot_Shares21_six.index = pd.to_datetime(pivot_Shares21_six["Date"])
pivot_Shares21_six.drop(["Date"], axis=1, inplace=True)
shares21_six_Monthly = pivot_Shares21_six.groupby(pd.Grouper(freq='M')).sum()
#drop year 2021
shares21_six_Monthly = shares21_six_Monthly.drop(shares21_six_Monthly.index[shares21_six_Monthly.index.year == 2021])
sum_shares21_six = shares21_six_Monthly.sum(axis=1)
sum_shares21_six = sum_shares21_six.astype(int).map('${:,.0f}'.format)

### 21Shares SIX MONTHLY CHART

fig_shares21_six_monthly = px.bar(shares21_six_Monthly, x=shares21_six_Monthly.index,
y=shares21_six_Monthly.columns,
labels={
    'value':'Turnover $',
    'datetime':'Date'
})

fig_shares21_six_monthly.update_layout(
title={
    'text': '21Shares SIX PRODUCTS MONTHLY TURNOVER',
    'y':0.95,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'
})
fig_shares21_six_monthly.update_xaxes(
    dtick='M1',
    showgrid=True,
    tickformat='%b\n%Y',
    ticklabelmode='period'
)
#show total value on top of each bar

fig_shares21_six_monthly.add_trace(go.Scatter
    (x=shares21_six_Monthly.index,
    y=sum_shares21_six,
    text=sum_shares21_six,
    mode='text',
    textposition='top center',
    textfont=dict(
        size=12,
        color='white'
    ),
    showlegend=False
))


#ETC-GROUP BITCOIN
pd_ETC_GROUP_XETRA_BTC=tv.get_hist('BTCE','XETR',interval=Interval.in_daily,n_bars=300)
pd_ETC_GROUP_XETRA_BTC["averageprice"] = (pd_ETC_GROUP_XETRA_BTC["high"] + pd_ETC_GROUP_XETRA_BTC["open"] + pd_ETC_GROUP_XETRA_BTC["close"] + pd_ETC_GROUP_XETRA_BTC["low"]) /4
pd_ETC_GROUP_XETRA_BTC["turnover"] = (pd_ETC_GROUP_XETRA_BTC["averageprice"] * pd_ETC_GROUP_XETRA_BTC["volume"])*EURUSD_Mean
pd_ETC_GROUP_XETRA_BTC["turnover"].astype(int)

#ETC-GROUP ETHEREUM
pd_ETC_GROUP_XETRA_ETH=tv.get_hist('ZETH','XETR',interval=Interval.in_daily,n_bars=300)
pd_ETC_GROUP_XETRA_ETH["averageprice"] = (pd_ETC_GROUP_XETRA_ETH["high"] + pd_ETC_GROUP_XETRA_ETH["open"] + pd_ETC_GROUP_XETRA_ETH["close"] + pd_ETC_GROUP_XETRA_ETH["low"]) /4
pd_ETC_GROUP_XETRA_ETH["turnover"] = (pd_ETC_GROUP_XETRA_ETH["averageprice"] * pd_ETC_GROUP_XETRA_ETH["volume"])*EURUSD_Mean
pd_ETC_GROUP_XETRA_ETH["turnover"].astype(int)

#ETC-GROUP SOLANA
pd_ETC_GROUP_XETRA_SOL=tv.get_hist('ESOL','XETR',interval=Interval.in_daily,n_bars=300)
pd_ETC_GROUP_XETRA_SOL["averageprice"] = (pd_ETC_GROUP_XETRA_SOL["high"] + pd_ETC_GROUP_XETRA_SOL["open"] + pd_ETC_GROUP_XETRA_SOL["close"] + pd_ETC_GROUP_XETRA_SOL["low"]) /4
pd_ETC_GROUP_XETRA_SOL["turnover"] = (pd_ETC_GROUP_XETRA_SOL["averageprice"] * pd_ETC_GROUP_XETRA_SOL["volume"])*EURUSD_Mean
pd_ETC_GROUP_XETRA_SOL["turnover"].astype(int)

#ETC-GROUP CARDANO
pd_ETC_GROUP_XETRA_ADA=tv.get_hist('RDAN','XETR',interval=Interval.in_daily,n_bars=300)
pd_ETC_GROUP_XETRA_ADA["averageprice"] = (pd_ETC_GROUP_XETRA_ADA["high"] + pd_ETC_GROUP_XETRA_ADA["open"] + pd_ETC_GROUP_XETRA_ADA["close"] + pd_ETC_GROUP_XETRA_ADA["low"]) /4
pd_ETC_GROUP_XETRA_ADA["turnover"] = (pd_ETC_GROUP_XETRA_ADA["averageprice"] * pd_ETC_GROUP_XETRA_ADA["volume"])*EURUSD_Mean
pd_ETC_GROUP_XETRA_ADA["turnover"].astype(int)

#ETC-GROUP POLKADOT
pd_ETC_GROUP_XETRA_DOT=tv.get_hist('PLKA','XETR',interval=Interval.in_daily,n_bars=300)
pd_ETC_GROUP_XETRA_DOT["averageprice"] = (pd_ETC_GROUP_XETRA_DOT["high"] + pd_ETC_GROUP_XETRA_DOT["open"] + pd_ETC_GROUP_XETRA_DOT["close"] + pd_ETC_GROUP_XETRA_DOT["low"]) /4
pd_ETC_GROUP_XETRA_DOT["turnover"] = (pd_ETC_GROUP_XETRA_DOT["averageprice"] * pd_ETC_GROUP_XETRA_DOT["volume"])*EURUSD_Mean
pd_ETC_GROUP_XETRA_DOT["turnover"].astype(int)

ETC_xetr = pd.concat([pd_ETC_GROUP_XETRA_ADA, pd_ETC_GROUP_XETRA_BTC, pd_ETC_GROUP_XETRA_DOT, pd_ETC_GROUP_XETRA_ETH, pd_ETC_GROUP_XETRA_SOL])
ETC_xetr['Date'] = pd.to_datetime(ETC_xetr.index.date)
ETC_xetr.set_index(ETC_xetr['Date'], drop=True, inplace=True)
ETC_xetr.drop(['Date'], axis=1, inplace=True)

#ETC-Group Xetra Pivot
pivot_ETC_xetr = (
    ETC_xetr.pivot_table(index=ETC_xetr.index,
                   columns='symbol',
                   values='turnover',
                   aggfunc='first')
        .rename_axis(columns=None)
        .reset_index()
        .fillna(0)
)

#ETC-Group XETRA Products MONTHLY
pivot_ETC_xetr.index = pd.to_datetime(pivot_ETC_xetr["Date"])
pivot_ETC_xetr.drop(["Date"], axis=1, inplace=True)
ETC_xetr_Monthly = pivot_ETC_xetr.groupby(pd.Grouper(freq='M')).sum()
#drop year 2021
ETC_xetr_Monthly = ETC_xetr_Monthly.drop(ETC_xetr_Monthly.index[ETC_xetr_Monthly.index.year == 2021])
sum_ETC_xetr = ETC_xetr_Monthly.sum(axis=1)
sum_ETC_xetr = sum_ETC_xetr.astype(int).map('${:,.0f}'.format)

### ETC-Group XETRA Products MONTHLY CHART

fig_ETC_xetr_monthly = px.bar(ETC_xetr_Monthly, x=ETC_xetr_Monthly.index,
y=ETC_xetr_Monthly.columns,
labels={
    'value':'Turnover $',
    'datetime':'Date'
})

fig_ETC_xetr_monthly.update_layout(
title={
    'text': 'ETC Group PRODUCTS MONTHLY TURNOVER',
    'y':0.95,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'
})
fig_ETC_xetr_monthly.update_xaxes(
    dtick='M1',
    showgrid=True,
    tickformat='%b\n%Y',
    ticklabelmode='period'
)
#show total value on top of each bar

fig_ETC_xetr_monthly.add_trace(go.Scatter
    (x=ETC_xetr_Monthly.index,
    y=sum_ETC_xetr,
    text=sum_ETC_xetr,
    mode='text',
    textposition='top center',
    textfont=dict(
        size=12,
        color='white'
    ),
    showlegend=False
))



st.title('Valour Dashboard')

st.plotly_chart(fig_valour_monthly, use_container_width=True)
st.plotly_chart(fig_xbt_monthly, use_container_width=True)
st.plotly_chart(fig_shares21_xetr_monthly, use_container_width=True)
st.plotly_chart(fig_shares21_six_monthly, use_container_width=True)
st.plotly_chart(fig_ETC_xetr_monthly, use_container_width=True)


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 