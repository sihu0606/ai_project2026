# app.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# 페이지 설정
st.set_page_config(
    page_title="Countries MBTI Dashboard",
    page_icon="🌍",
    layout="wide"
)

# 제목
st.title("🌍 Countries MBTI Dashboard")
st.markdown("국가별 MBTI 비율을 인터랙티브하게 확인해보세요.")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# 국가 선택
countries = sorted(df["Country"].unique())

selected_country = st.selectbox(
    "국가를 선택하세요",
    countries
)

# 선택된 국가 데이터
country_data = df[df["Country"] == selected_country].iloc[0]

# MBTI 컬럼 추출
mbti_cols = [col for col in df.columns if col != "Country"]

# 데이터 정리
mbti_values = pd.DataFrame({
    "MBTI": mbti_cols,
    "Ratio": [country_data[col] for col in mbti_cols]
})

# 정렬
mbti_values = mbti_values.sort_values(
    by="Ratio",
    ascending=False
).reset_index(drop=True)

# 색상 지정
colors = []

max_value = mbti_values["Ratio"].max()

for i, row in mbti_values.iterrows():
    if row["Ratio"] == max_value:
        colors.append("#ff3b30")  # 빨간색
    else:
        # 파란색 그라데이션 느낌
        intensity = 255 - (i * 8)
        intensity = max(80, intensity)

        colors.append(
            f"rgb(70, 130, {intensity})"
        )

# 그래프 생성
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=mbti_values["MBTI"],
        y=mbti_values["Ratio"],
        marker_color=colors,
        text=[
            f"{v*100:.1f}%"
            for v in mbti_values["Ratio"]
        ],
        textposition="outside",
        hovertemplate=
        "<b>%{x}</b><br>" +
        "비율: %{y:.2%}<extra></extra>"
    )
)

# 레이아웃
fig.update_layout(
    title=f"{selected_country} MBTI Distribution",
    template="plotly_white",
    height=650,
    xaxis_title="MBTI",
    yaxis_title="Ratio",
    font=dict(
        family="Arial",
        size=14
    ),
    title_font=dict(
        size=26
    ),
    showlegend=False,
    margin=dict(
        t=80,
        l=40,
        r=40,
        b=40
    )
)

# Y축 퍼센트 표시
fig.update_yaxes(
    tickformat=".0%"
)

# 그래프 출력
st.plotly_chart(
    fig,
    use_container_width=True
)

# 추가 정보
top_mbti = mbti_values.iloc[0]

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "가장 높은 MBTI",
        top_mbti["MBTI"]
    )

with col2:
    st.metric(
        "비율",
        f"{top_mbti['Ratio']*100:.2f}%"
    )

# 데이터 테이블
with st.expander("데이터 보기"):
    st.dataframe(
        mbti_values,
        use_container_width=True
    )
