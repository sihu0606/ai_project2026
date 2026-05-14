# app.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(
    page_title="MBTI Countries Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 MBTI Countries Dashboard")
st.markdown("MBTI를 선택하면 상위 국가 비율을 확인할 수 있습니다.")

# 데이터 로드
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

# MBTI 컬럼
mbti_types = [col for col in df.columns if col != "Country"]

# MBTI 선택
selected_mbti = st.selectbox(
    "MBTI를 선택하세요",
    sorted(mbti_types)
)

# 상위 개수 선택
top_n = st.slider(
    "표시할 국가 개수",
    min_value=5,
    max_value=10,
    value=5
)

# 데이터 정리
mbti_df = df[["Country", selected_mbti]].copy()

mbti_df.columns = ["Country", "Ratio"]

# 정렬 후 TOP N만 선택
mbti_df = (
    mbti_df
    .sort_values(by="Ratio", ascending=False)
    .head(top_n)
    .reset_index(drop=True)
)

# 최고 국가
top_country = mbti_df.iloc[0]

# 색상 설정
colors = []

max_ratio = mbti_df["Ratio"].max()

for i, row in mbti_df.iterrows():

    if row["Ratio"] == max_ratio:
        colors.append("#ff3b30")  # 빨간색
    else:
        intensity = 255 - (i * 20)
        intensity = max(100, intensity)

        colors.append(
            f"rgb(70, 130, {intensity})"
        )

# 그래프 생성
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=mbti_df["Country"],
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

# 레이아웃
fig.update_layout(
    title=f"Top {top_n} Countries for {selected_mbti}",
    template="plotly_white",
    height=650,
    showlegend=False,
    xaxis_title="Country",
    yaxis_title="Ratio",
    margin=dict(
        t=80,
        l=40,
        r=40,
        b=80
    )
)

# Y축 퍼센트
fig.update_yaxes(
    tickformat=".0%"
)

# 그래프 출력
st.plotly_chart(
    fig,
    use_container_width=True
)

# 최고 국가 표시
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "1위 국가",
        top_country["Country"]
    )

with col2:
    st.metric(
        "비율",
        f"{top_country['Ratio']*100:.2f}%"
    )

# 테이블
st.subheader("📋 데이터")

table_df = mbti_df.copy()

table_df["Ratio"] = (
    table_df["Ratio"] * 100
).round(2).astype(str) + "%"

st.dataframe(
    table_df,
    use_container_width=True
)
