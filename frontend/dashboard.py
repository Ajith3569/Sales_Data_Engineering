import streamlit as st
import pandas as pd
import psycopg2
import time

# Database connection
@st.cache_resource
def get_connection():
    return psycopg2.connect(
        dbname="retail_db",
        user="ajithkumardugyala",  # change if needed
        password="",               # empty if trust auth
        host="localhost",
        port="5432"
    )

# Function to fetch data
def load_data():
    conn = get_connection()
    query = "SELECT * FROM retail_sales_stream ORDER BY timestamp DESC LIMIT 50;"
    df = pd.read_sql(query, conn)
    return df

st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")

st.title("🛍️ Real-Time Retail Sales Dashboard")

# Auto-refresh
refresh_interval = st.slider("Auto-refresh every (seconds):", 5, 60, 10)
placeholder = st.empty()

while True:
    with placeholder.container():
        df = load_data()

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📦 Sales by Category")
            category_sales = df.groupby("category")["price"].sum().reset_index()
            st.bar_chart(category_sales.set_index("category"))

        with col2:
            st.subheader("🏬 Sales Count by Store")
            store_sales = df["store_id"].value_counts().reset_index()
            store_sales.columns = ["store_id", "transactions"]
            st.bar_chart(store_sales.set_index("store_id"))

        st.subheader("🧾 Latest Transactions")
        st.dataframe(df)

    time.sleep(refresh_interval)
