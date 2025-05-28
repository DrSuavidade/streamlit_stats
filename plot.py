import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Overview Data Explorer")
    df = pd.read_csv("data/Overview.csv")
    col1 = st.selectbox("X-axis", df.columns)
    col2 = st.selectbox("Y-axis", df.columns)
    fig = px.scatter(df, x=col1, y=col2, title=f"{col1} vs {col2}")
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
