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
st.markdown("MBTI를 선택하면 국가별 비율을 확인할 수 있습니다.")

# 데이터 로드
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

# 선택한 MBTI 기준 데이터 생성
mbti_df = df[["Country", selected_mbti]].copy()

# 컬럼명 변경
mbti_df.columns = ["Country", "Ratio"]

# 정렬
mbti_df = mbti_df.sort_values(
    by="Ratio",
    ascending=False
).reset_index(drop=True)

# TOP 국가
top_country = mbti_df.iloc[0]

# 색상 설정
colors = []

max_ratio = mbti_df["Ratio"].max()

for i, row in mbti_df.iterrows():

    if row["Ratio"] == max_ratio:
        colors.append("#ff3b30")  # 1등 빨간색
    else:
        # 파란색 그라데이션
        intensity = 255 - int(i * 1.2)
        intensity = max(80, intensity)

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

# 레이아웃 설정
fig.update_layout(
    title=f"{selected_mbti} Distribution by Country",
    template="plotly_white",
    height=700,
    xaxis_title="Country",
    yaxis_title="Ratio",
    showlegend=False,
    margin=dict(
        t=80,
        l=40,
        r=40,
        b=120
    ),
    font=dict(
        size=13
    )
)

# Y축 퍼센트
fig.update_yaxes(
    tickformat=".0%"
)

# X축 회전
fig.update_xaxes(
    tickangle=-45
)

# 출력
st.plotly_chart(
    fig,
    use_container_width=True
)

# TOP 국가 표시
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "가장 높은 국가",
        top_country["Country"]
    )

with col2:
    st.metric(
        "비율",
        f"{top_country['Ratio']*100:.2f}%"
    )

# TOP 10 테이블
st.subheader(f"🏆 TOP 10 Countries for {selected_mbti}")

top10 = mbti_df.head(10).copy()

top10["Ratio"] = (
    top10["Ratio"] * 100
).round(2).astype(str) + "%"

st.dataframe(
    top10,
    use_container_width=True
)
