import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('data/vehicles_us_cleaned.csv')
        
        # Convert date columns if any exist
        date_columns = ['date_posted', 'model_year']  # Adjust based on your data
        for col in date_columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='coerce')
        
        # More efficient numeric conversion
        for col in df.select_dtypes(include=['number']).columns:
            df[col] = pd.to_numeric(df[col], downcast='integer', errors='ignore')
            
        return df
    except FileNotFoundError:
        st.error("Data file not found. Please check the path.")
        return pd.DataFrame()

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


