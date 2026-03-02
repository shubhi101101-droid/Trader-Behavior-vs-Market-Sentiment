import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Trader Sentiment Dashboard", layout="wide")

st.title("📊 Trader Performance vs Market Sentiment Dashboard")

# ---------------------------
# Load Data
# ---------------------------
@st.cache_data
def load_data():
    trades = pd.read_csv("historical_data.csv")
    sentiment = pd.read_csv("fear_greed_index.csv")

    trades['Timestamp'] = trades['Timestamp'].astype('int64')
    trades['Timestamp'] = pd.to_datetime(trades['Timestamp'], unit='ms')
    trades['date'] = trades['Timestamp'].dt.date

    sentiment['date'] = pd.to_datetime(sentiment['date']).dt.date
    sentiment = sentiment[['date', 'classification']]

    # Daily Aggregations
    daily_pnl = trades.groupby(['Account', 'date'])['Closed PnL'].sum().reset_index()
    daily_pnl.rename(columns={'Closed PnL': 'daily_pnl'}, inplace=True)

    daily_trades = trades.groupby(['Account', 'date']).size().reset_index(name='trade_count')

    trades['win'] = trades['Closed PnL'] > 0
    daily_winrate = trades.groupby(['Account', 'date'])['win'].mean().reset_index()
    daily_winrate.rename(columns={'win': 'win_rate'}, inplace=True)

    avg_size = trades.groupby(['Account', 'date'])['Size USD'].mean().reset_index()
    avg_size.rename(columns={'Size USD': 'avg_trade_size'}, inplace=True)

    df = daily_pnl.merge(daily_trades, on=['Account', 'date'])
    df = df.merge(daily_winrate, on=['Account', 'date'])
    df = df.merge(avg_size, on=['Account', 'date'])
    df = df.merge(sentiment, on='date', how='left')
    df = df.dropna(subset=['classification'])

    return df

df = load_data()

# ---------------------------
# Sidebar Filters
# ---------------------------
st.sidebar.header("Filters")

sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment Regime",
    options=df['classification'].unique(),
    default=df['classification'].unique()
)

df_filtered = df[df['classification'].isin(sentiment_filter)]

# ---------------------------
# Summary Metrics
# ---------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Average Daily PnL", f"{df_filtered['daily_pnl'].mean():,.0f}")
col2.metric("Average Trade Count", f"{df_filtered['trade_count'].mean():,.0f}")
col3.metric("Average Win Rate", f"{df_filtered['win_rate'].mean():.2%}")

st.markdown("---")

# ---------------------------
# PnL Distribution
# ---------------------------
st.subheader("Daily PnL Distribution")

fig1, ax1 = plt.subplots(figsize=(8,5))
sns.boxplot(x='classification', y='daily_pnl', data=df_filtered, ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)

# ---------------------------
# Trade Frequency
# ---------------------------
st.subheader("Average Trade Count by Sentiment")

freq = df_filtered.groupby('classification')['trade_count'].mean().reset_index()

fig2, ax2 = plt.subplots(figsize=(8,5))
sns.barplot(x='classification', y='trade_count', data=freq, ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)

# ---------------------------
# Trade Size Distribution
# ---------------------------
st.subheader("Average Trade Size Distribution")

fig3, ax3 = plt.subplots(figsize=(8,5))
sns.boxplot(x='classification', y='avg_trade_size', data=df_filtered, ax=ax3)
plt.xticks(rotation=45)
st.pyplot(fig3)

# ---------------------------
# Top Traders
# ---------------------------
st.subheader("Top 10 Traders by Average Daily PnL")

top_traders = (
    df_filtered.groupby('Account')['daily_pnl']
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

st.dataframe(top_traders)

st.markdown("---")
st.caption("Sentiment-Adaptive Trading Analysis Dashboard")