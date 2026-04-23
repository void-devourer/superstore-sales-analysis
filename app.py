import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="Superstore Sales Dashboard", 
                   page_icon="🏪", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv(r'C:\Users\Piyush Kumar\Desktop\lessgo\projects\sample-superstore-sales-project\data\Sample - Superstore.csv', 
                     encoding='latin-1')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    df['Order Year'] = df['Order Date'].dt.year
    df['Order Month'] = df['Order Date'].dt.month
    df['Profit Margin %'] = (df['Profit'] / df['Sales']) * 100
    return df

df = load_data()

# Title
st.title("🏪 Superstore Sales Intelligence Dashboard")
st.markdown("*4-year retail analysis (2014–2017) — Key findings for business decision making*")
st.markdown("---")

# Sidebar filters
st.sidebar.header("Filters")
year_filter = st.sidebar.multiselect("Select Year", 
                                      sorted(df['Order Year'].unique()), 
                                      default=sorted(df['Order Year'].unique()))
region_filter = st.sidebar.multiselect("Select Region", 
                                        df['Region'].unique(), 
                                        default=df['Region'].unique())
category_filter = st.sidebar.multiselect("Select Category", 
                                          df['Category'].unique(), 
                                          default=df['Category'].unique())

# Apply filters
filtered = df[
    df['Order Year'].isin(year_filter) & 
    df['Region'].isin(region_filter) & 
    df['Category'].isin(category_filter)
]

# KPI Row
st.header("Key Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${filtered['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"${filtered['Profit'].sum():,.0f}")
col3.metric("Avg Margin", f"{filtered['Profit Margin %'].mean():.1f}%")
col4.metric("Total Orders", f"{len(filtered):,}")

st.markdown("---")

# Row 1 - Category and Region
st.header("Category & Regional Performance")
col5, col6 = st.columns(2)

with col5:
    cat_data = filtered.groupby('Category')['Profit'].sum().sort_values()
    fig, ax = plt.subplots(figsize=(6, 4))
    colors = ['#F44336' if x < 0 else '#4CAF50' for x in cat_data.values]
    ax.barh(cat_data.index, cat_data.values, color=colors)
    ax.set_title('Total Profit by Category')
    ax.set_xlabel('Profit ($)')
    ax.axvline(x=0, color='black', linestyle='--', alpha=0.5)
    st.pyplot(fig)
    plt.close()

with col6:
    reg_data = filtered.groupby('Region')['Profit Margin %'].mean().sort_values()
    fig, ax = plt.subplots(figsize=(6, 4))
    colors = ['#F44336' if x < 0 else '#4CAF50' for x in reg_data.values]
    ax.barh(reg_data.index, reg_data.values, color=colors)
    ax.set_title('Avg Profit Margin % by Region')
    ax.set_xlabel('Margin %')
    ax.axvline(x=0, color='black', linestyle='--', alpha=0.5)
    st.pyplot(fig)
    plt.close()

st.markdown("---")

# Row 2 - Discount Impact
st.header("⚠️ The Discount Problem")
col7, col8 = st.columns(2)

with col7:
    discount_bins = pd.cut(filtered['Discount'], 
                           bins=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.8],
                           labels=['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-80%'],
                           include_lowest=True)
    discount_profit = filtered.groupby(discount_bins, observed=True)['Profit Margin %'].mean()
    fig, ax = plt.subplots(figsize=(6, 4))
    colors = ['#4CAF50' if x > 0 else '#F44336' for x in discount_profit.values]
    ax.bar(discount_profit.index, discount_profit.values, color=colors)
    ax.axhline(y=0, color='black', linestyle='--')
    ax.set_title('Avg Profit Margin by Discount Level')
    ax.set_ylabel('Margin %')
    ax.set_xlabel('Discount Range')
    st.pyplot(fig)
    plt.close()

with col8:
    st.markdown("### 🔍 Key Finding")
    st.error("Any discount above 20% results in average losses")
    disc_table = pd.DataFrame({
        'Discount Range': ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-80%'],
        'Avg Margin': ['33.7%', '17.5%', '-11.6%', '-21.7%', '-53.6%', '-113.9%'],
        'Status': ['✅ Profitable', '✅ Profitable', '🚨 Loss', '🚨 Loss', '🚨 Loss', '💀 Severe Loss']
    })
    st.dataframe(disc_table, hide_index=True)

st.markdown("---")

# Row 3 - Yearly trend
st.header("Year-over-Year Growth")
yearly = filtered.groupby('Order Year').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum')
).round(2)

fig, ax1 = plt.subplots(figsize=(10, 4))
ax2 = ax1.twinx()
ax1.bar(yearly.index, yearly['Total_Sales'], color='#2196F3', alpha=0.7, label='Sales')
ax2.plot(yearly.index, yearly['Total_Profit'], color='#4CAF50', marker='o', linewidth=2, label='Profit')
ax1.set_ylabel('Sales ($)', color='#2196F3')
ax2.set_ylabel('Profit ($)', color='#4CAF50')
ax1.set_title('Sales vs Profit by Year')
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
st.pyplot(fig)
plt.close()

st.markdown("---")

# Footer
st.markdown("Built by **Piyush Kumar** | IIT Goa Mechanical Engineering")
st.markdown("Data Analysis Project — Superstore Retail Sales Intelligence")