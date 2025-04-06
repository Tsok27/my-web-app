import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('data/vehicles_us_cleaned.csv')

df = load_data()

# Header
st.header('Vehicle Market Analysis Tool')
st.write("Explore pricing trends and vehicle characteristics")

# Checkbox filter
show_expensive = st.checkbox('Show only vehicles above $20,000')
if show_expensive:
    df = df[df['price'] > 20000]

# Histogram
st.subheader('Price Distribution')
fig = px.histogram(df, 
                  x='price',
                  title='Price Distribution',
                  labels={'price': 'Price (USD)'},
                  nbins=30)
fig.update_layout(bargap=0.1)
st.plotly_chart(fig, use_container_width=True)

# Scatter plot
st.subheader('Price vs Mileage')
scatter_fig = px.scatter(
    df,
    x='odometer',
    y='price',
    color='condition',
    hover_name='model',
    title='How Mileage Affects Pricing'
)
st.plotly_chart(scatter_fig, use_container_width=True)

# Data table toggle
if st.checkbox('Show raw data'):
    st.dataframe(df.head(100).astype(str))

