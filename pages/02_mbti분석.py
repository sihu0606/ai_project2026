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

# 제목
st.title("🌍 MBTI Countries Dashboard")
st.markdown(
    "MBTI를 선택하면 상위 10개 국가와 전체 국가 데이터를 확인할 수 있습니다."
)

# 데이터 불러오기
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

# MBTI 컬럼 추출
mbti_types = [col for col in df.columns if col != "Country"]

# MBTI 선택
selected_mbti = st.selectbox(
    "MBTI를 선택하세요",
    sorted(mbti_types)
)

# 데이터 정리
mbti_df = df[["Country", selected_mbti]].copy()

mbti_df.columns = ["Country", "Ratio"]

# 정렬
mbti_df = (
    mbti_df
    .sort_values(by="Ratio", ascending=False)
    .reset_index(drop=True)
)

# TOP 10 데이터
top10_df = mbti_df.head(10)

# 1위 국가
top_country = top10_df.iloc[0]

# 색상 설정
colors = []

max_ratio = top10_df["Ratio"].max()

for i, row in top10_df.iterrows():

    if row["Ratio"] == max_ratio:
        colors.append("#ff3b30")  # 빨간색
    else:
        # 파란색 그라데이션
        intensity = 255 - (i * 18)
        intensity = max(100, intensity)

        colors.append(
            f"rgb(70, 130, {intensity})"
        )

# 그래프 생성
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=top10_df["Country"],
        y=top10_df["Ratio"],
        marker_color=colors,
        text=[
            f"{v*100:.1f}%"
            for v in top10_df["Ratio"]
        ],
        textposition="outside",
        hovertemplate=
        "<b>%{x}</b><br>" +
        "비율: %{y:.2%}<extra></extra>"
    )
)

# 그래프 레이아웃
fig.update_layout(
    title=f"🏆 Top 10 Countries for {selected_mbti}",
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
    ),
    font=dict(
        size=14
    )
)

# Y축 퍼센트 표시
fig.update_yaxes(
    tickformat=".0%"
)

# X축 회전
fig.update_xaxes(
    tickangle=-20
)

# 그래프 출력
st.plotly_chart(
    fig,
    use_container_width=True
)

# 1위 국가 정보
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "🥇 1위 국가",
        top_country["Country"]
    )

with col2:
    st.metric(
        "📊 비율",
        f"{top_country['Ratio']*100:.2f}%"
    )

# 전체 데이터 섹션
st.markdown("---")

st.subheader(f"🌎 All Countries for {selected_mbti}")

# 퍼센트 변환
full_table = mbti_df.copy()

full_table["Ratio"] = (
    full_table["Ratio"] * 100
).round(2).astype(str) + "%"

# 전체 데이터 표시
st.dataframe(
    full_table,
    use_container_width=True,
    hide_index=True,
    height=700
)
