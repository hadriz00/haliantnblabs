import streamlit as st
import pandas as pd
import pickle

col1, col2 = st.columns(2)
df = pd.read_csv('data.csv')

with col1:
    df_city = df.groupby('City')['ElectricityBill'].sum().reset_index()
    st.bar_chart(df, x="City", y="MonthlyHours")

with col2:
    df_city = df.groupby('City')['ElectricityBill'].sum().reset_index()
    st.bar_chart(df, x="City", y="ElectricityBill")

fan = st.slider("Number of fan", 5,20, value=10)
fridge = st.slider("Number of Refrigerator", 18,23, value=20)
aircon= st.slider("Number of Aircon", 0,3, value=1)
tv= st.slider("Number of TV", 5,20, value=3)
hour=st.slider(Number of hours", 390,600, value=400)
               