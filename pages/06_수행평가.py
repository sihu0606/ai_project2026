import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="조주기능사 칵테일 추천",
    page_icon="🍸",
    layout="wide"
)

st.title("🍸 조주기능사 칵테일 정보 및 디저트 페어링")

cocktails = {
    "Dry Martini": {
        "조주법": "Stir",
        "재료": "Gin, Dry Vermouth",
        "디저트": "레몬 타르트",
        "설명": "드라이하고 깔끔한 맛이 레몬 타르트의 상큼함과 잘 어울립니다."
    },

    "Manhattan": {
        "조주법": "Stir",
        "재료": "Bourbon Whiskey, Sweet Vermouth",
        "디저트": "다크 초콜릿 브라우니",
        "설명": "위스키의 바닐라 향과 초콜릿의 풍미가 훌륭한 조화를 이룹니다."
    },

    "Old Fashioned": {
        "조주법": "Build",
        "재료": "Bourbon Whiskey, Sugar, Bitters",
        "디저트": "피칸 파이",
        "설명": "카라멜과 견과류 풍미가 위스키와 잘 어울립니다."
    },

    "Margarita": {
        "조주법": "Shake",
        "재료": "Tequila, Triple Sec, Lime Juice",
        "디저트": "치즈케이크",
        "설명": "라임의 산미가 치즈케이크의 진한 맛을 깔끔하게 정리해줍니다."
    },

    "Daiquiri": {
        "조주법": "Shake",
        "재료": "Rum, Lime Juice, Sugar",
        "디저트": "코코넛 마카롱",
        "설명": "럼과 코코넛의 열대과일 향이 자연스럽게 이어집니다."
    },

    "Cosmopolitan": {
        "조주법": "Shake",
        "재료": "Vodka, Triple Sec, Lime Juice, Cranberry Juice",
        "디저트": "베리 타르트",
        "설명": "크랜베리와 베리류의 과일 향이 잘 어울립니다."
    },

    "Pina Colada": {
        "조주법": "Blend",
        "재료": "Rum, Pineapple Juice, Coconut Cream",
        "디저트": "코코넛 케이크",
        "설명": "코코넛 향을 극대화하여 열대풍 느낌을 살려줍니다."
    },

    "Mai-Tai": {
        "조주법": "Blend",
        "재료": "Rum, Triple Sec, Fruit Juice",
        "디저트": "파인애플 업사이드 다운 케이크",
        "설명": "열대과일 풍미가 칵테일과 완벽하게 어울립니다."
    },

    "Whiskey Sour": {
        "조주법": "Shake",
        "재료": "Whiskey, Lemon Juice, Sugar",
        "디저트": "레몬 파운드 케이크",
        "설명": "상큼한 산미가 칵테일과 좋은 밸런스를 만듭니다."
    },

    "Long Island Iced Tea": {
        "조주법": "Build",
        "재료": "5대 증류주 + Cola",
        "디저트": "뉴욕 치즈케이크",
        "설명": "진한 알코올감과 치즈케이크의 묵직함이 균형을 이룹니다."
    }
}

selected = st.selectbox(
    "칵테일을 선택하세요",
    list(cocktails.keys())
)

info = cocktails[selected]

st.subheader(f"🍹 {selected}")

col1, col2 = st.columns(2)

with col1:
    st.metric("조주법", info["조주법"])

with col2:
    st.metric("추천 디저트", info["디저트"])

st.markdown("---")

st.write("### 주요 재료")
st.info(info["재료"])

st.write("### 디저트 페어링 설명")
st.success(info["설명"])
