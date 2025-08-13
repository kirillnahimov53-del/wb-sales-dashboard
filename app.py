import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(page_title="WB Sales", layout="wide")
st.title("WB Sales — продажи по дням")

uploaded = st.file_uploader("Загрузите CSV (date,orders,revenue)", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
else:
    df = pd.DataFrame({"date": ["2025-08-01","2025-08-02"], "orders":[1,3], "revenue":[1000,2300]})

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")
st.line_chart(df.set_index("date")[["orders"]])
st.bar_chart(df.set_index("date")[["revenue"]])

st.caption("Заглушка. Позже подключим прямую выгрузку из WB через wb-api-clients.")
