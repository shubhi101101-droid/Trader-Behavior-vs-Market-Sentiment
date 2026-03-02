# Trader-Behavior-vs-Market-Sentiment
## 📌 Project Overview

This project analyzes how market sentiment (Fear & Greed Index) influences trader behavior and profitability on Hyperliquid.

The objective is to uncover behavioral trading patterns across different sentiment regimes (Fear, Greed, Neutral), evaluate trader performance under varying market conditions, and propose actionable strategy recommendations.

The project includes data cleaning, feature engineering, exploratory analysis, predictive modeling, clustering, and a lightweight Streamlit dashboard.

---

## 🎯 Objectives

- Analyze trader performance across sentiment regimes  
- Identify behavioral differences in trading activity  
- Segment traders into behavioral archetypes  
- Build a predictive model for trader profitability  
- Develop regime-based strategy recommendations  
- Create an interactive dashboard for result exploration  

---


---

# 🔎 Methodology

## 1️⃣ Data Cleaning
- Converted millisecond timestamps to datetime format  
- Aggregated trade-level data into daily account-level metrics  
- Merged trader data with sentiment dataset using date alignment  
- Removed observations without valid sentiment classification  

## 2️⃣ Feature Engineering
Constructed behavioral metrics at daily account level:
- Daily PnL  
- Trade count  
- Win rate  
- Average trade size  
- Long/Short ratio  
- Leverage proxy segment  

## 3️⃣ Exploratory Analysis
- Compared PnL distribution across sentiment regimes  
- Analyzed trading intensity during Fear vs Greed periods  
- Evaluated risk-taking behavior and volatility exposure  

## 4️⃣ Predictive Modeling
- Built a Random Forest classifier  
- Target: profitability bucket (profitable vs non-profitable)  
- Features: trade behavior + sentiment classification  
- Evaluated using classification metrics  

## 5️⃣ Clustering
- Applied KMeans clustering  
- Identified trader behavioral archetypes  
- Compared cluster performance across regimes  

---

# 📈 Key Insights

- Trade frequency increases significantly during Fear regimes.  
- Profitability dispersion is highest during Fear, indicating elevated volatility.  
- High-intensity traders amplify both gains and losses during extreme sentiment states.  
- Conservative traders exhibit more stable performance across regimes.  

---

# 💡 Strategy Recommendations (Part C)
### Strategy 1: Volatility-Aware Leverage Control During Fear regimes:
Cap leverage dynamically
Reduce position sizes by ~25%
Tighten stop-loss levels This captures volatility opportunities while reducing drawdown risk.

### Strategy 2: Selective Aggression During Greed During Greed regimes:
Allow leverage expansion for high win-rate traders
Encourage trend-following strategies
Maintain conservative exposure for inconsistent traders

### Strategy 3: Overtrading Control in Fear Since trade frequency spikes dramatically during Fear:
Limit daily trade count
Pause after consecutive losses
Reduce emotional trading This improves risk-adjusted returns
---

# 📊 Output Visualizations

Saved inside the `/outputs` folder:
- PnL Distribution by Sentiment  
- Trade Frequency Comparison  
- Trade Size Distribution  
- Trader Clustering Visualization  

# 🚀 Setup Instructions

## 1️⃣  Create Virtual Environment

### Windows
python -m venv venv
venv\Scripts\activate

## 3️⃣ Install Dependencies
pip install -r requirements.txt

---

# ▶️ How to Run the Notebook
jupyter notebook
Open `notebook.ipynb` and run all cells sequentially.
---

# 🌐 How to Run the Streamlit Dashboard
streamlit run app.py

The dashboard will automatically open in your browser.

---

# 📦 Dependencies

- pandas  
- numpy  
- matplotlib  
- seaborn  
- scikit-learn  
- streamlit  




