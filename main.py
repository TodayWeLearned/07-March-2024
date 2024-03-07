import streamlit as st
import pandas as pd
import duckdb

st.title('Students!')

df = pd.read_csv('data/student.csv')

st.dataframe(df)

gender_counts_pd = df.groupby("gender").size()
st.subheader("Gender counts by Pandas")
st.bar_chart(gender_counts_pd)

st.subheader("Gender counts by DuckDB")
gender_counts_db = duckdb.query("SELECT gender, COUNT(*) as count FROM df GROUP BY gender").df()
st.bar_chart(gender_counts_db, x="gender", y="count")
