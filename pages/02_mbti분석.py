# app.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ---------------------------------------------------
# 페이지 설정
# ---------------------------------------------------

st.set_page_config(
    page_title="MBTI Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 MBTI Interactive Dashboard")

st.markdown("""
- 국가를 선택 → 해당 국가의 MBTI 비율 보기
- MBTI를 선택 → 해당 MBTI 비율이 높은 국가 TOP 10 보기
""")

# ---------------------------------------------------
# 데이터 로드
# ---------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

mbti_cols = [col for col in df.columns if col != "Country"]

# ---------------------------------------------------
# 탭 생성
# ---------------------------------------------------

tab1, tab2 = st.tabs([
    "🌎 Country → MBTI",
    "🧠 MBTI → Countries"
])

# ===================================================
# TAB 1
# 국가 선택 → MBTI 그래프
# ===================================================

with tab1:

    st.subheader("🌎 국가별 MBTI 비율")

    countries = sorted(df["Country"].unique())

    selected_country = st.selectbox(
        "국가를 선택하세요",
        countries
    )

    # 국가 데이터 추출
    country_data = df[df["Country"] == selected_country].iloc[0]

    mbti_df = pd.DataFrame({
        "MBTI": mbti_cols,
        "Ratio": [country_data[col] for col in mbti_cols]
    })

    # 정렬
    mbti_df = (
        mbti_df
        .sort_values(by="Ratio", ascending=False)
        .reset_index(drop=True)
    )

    # 색상 설정
    colors = []

    max_ratio = mbti_df["Ratio"].max()

    for i, row in mbti_df.iterrows():

        if row["Ratio"] == max_ratio:
            colors.append("#ff3b30")
        else:
            intensity = 255 - (i * 8)
            intensity = max(100, intensity)

            colors.append(
                f"rgb(70, 130, {intensity})"
            )

    # 그래프 생성
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=mbti_df["MBTI"],
            y=mbti_df["Ratio"],
            marker_color=colors,
            text=[
                f"{v*100:.1f}%"
                for v in mbti_df["Ratio"]
            ],
            textposition="outside",
            hovertemplate=
            "<b>%{x}</b><br>" +
            "비율: %{y:.2%}<extra></extra>"
        )
    )

    fig.update_layout(
        title=f"{selected_country} MBTI Distribution",
        template="plotly_white",
        height=650,
        showlegend=False,
        xaxis_title="MBTI",
        yaxis_title="Ratio"
    )

    fig.update_yaxes(
        tickformat=".0%"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ===================================================
# TAB 2
# MBTI 선택 → 국가 TOP 10
# ===================================================

with tab2:

    st.subheader("🧠 MBTI별 국가 TOP 10")

    selected_mbti = st.selectbox(
        "MBTI를 선택하세요",
        sorted(mbti_cols)
    )

    # 데이터 생성
    mbti_country_df = df[[
        "Country",
        selected_mbti
    ]].copy()

    mbti_country_df.columns = [
        "Country",
        "Ratio"
    ]

    # 정렬 후 TOP10
    mbti_country_df = (
        mbti_country_df
        .sort_values(by="Ratio", ascending=False)
        .head(10)
        .reset_index(drop=True)
    )

    # 색상 설정
    colors = []

    max_ratio = mbti_country_df["Ratio"].max()

    for i, row in mbti_country_df.iterrows():

        if row["Ratio"] == max_ratio:
            colors.append("#ff3b30")
        else:
            intensity = 255 - (i * 18)
            intensity = max(100, intensity)

            colors.append(
                f"rgb(70, 130, {intensity})"
            )

    # 그래프 생성
    fig2 = go.Figure()

    fig2.add_trace(
        go.Bar(
            x=mbti_country_df["Country"],
            y=mbti_country_df["Ratio"],
            marker_color=colors,
            text=[
                f"{v*100:.1f}%"
                for v in mbti_country_df["Ratio"]
            ],
            textposition="outside",
            hovertemplate=
            "<b>%{x}</b><br>" +
            "비율: %{y:.2%}<extra></extra>"
        )
    )

    fig2.update_layout(
        title=f"Top 10 Countries for {selected_mbti}",
        template="plotly_white",
        height=650,
        showlegend=False,
        xaxis_title="Country",
        yaxis_title="Ratio"
    )

    fig2.update_yaxes(
        tickformat=".0%"
    )

    fig2.update_xaxes(
        tickangle=-20
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # 데이터 테이블
    st.subheader("📋 TOP 10 데이터")

    table_df = mbti_country_df.copy()

    table_df["Ratio"] = (
        table_df["Ratio"] * 100
    ).round(2).astype(str) + "%"

    st.dataframe(
        table_df,
        use_container_width=True,
        hide_index=True
    )
