# Streamlit app to display sales dashboard
import streamlit as st
import pandas as pd
import psycopg2

st.title("📊 Retail Sales Dashboard")

try:
    conn = psycopg2.connect(
        host="localhost",
        database="retaildb",
        user="admin",
        password="password"
    )
    df = pd.read_sql("SELECT * FROM sales ORDER BY timestamp DESC LIMIT 100", conn)
    st.write("### Recent Sales")
    st.dataframe(df)
    st.write("### Total Quantity per Item")
    st.bar_chart(df.groupby("item")["quantity"].sum())
    conn.close()
except Exception as e:
    st.error(f"Could not connect to DB: {e}")