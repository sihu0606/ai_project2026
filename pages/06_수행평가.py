import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="조주기능사 칵테일 가이드",
    page_icon="🍸",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("cocktail_recipes.csv")

df = load_data()

st.title("🍸 조주기능사 칵테일 & 디저트 페어링")

base = st.selectbox(
    "베이스 주종 선택",
    sorted(df["베이스"].unique())
)

filtered = df[df["베이스"] == base]

cocktail = st.selectbox(
    "칵테일 선택",
    sorted(filtered["칵테일"].tolist())
)

info = filtered[filtered["칵테일"] == cocktail].iloc[0]

col1, col2 = st.columns(2)

with col1:
    st.metric("조주법", info["조주법"])

with col2:
    st.metric("가니쉬", info["가니쉬"])

st.divider()

st.subheader("🥃 레시피")

recipe_cols = [
    "재료1",
    "재료2",
    "재료3",
    "재료4",
    "재료5",
    "재료6"
]

for col in recipe_cols:
    value = info[col]

    if pd.notna(value) and str(value).strip() != "":
        st.write(f"• {value}")

st.divider()

st.subheader("🍰 추천 디저트")

st.success(info["디저트"])

st.subheader("📖 페어링 설명")

st.info(info["페어링설명"])
