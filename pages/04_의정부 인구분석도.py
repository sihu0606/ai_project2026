import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# =====================================================
# 페이지 제목
# =====================================================

st.title("의정부 동네별 인구수")

# =====================================================
# CSV 읽기
# =====================================================

df = pd.read_csv("population.csv", encoding="cp949")

# =====================================================
# 전체 합계 제거
# =====================================================

df = df[df["행정구역"] != "경기도 의정부시"]

# =====================================================
# 연령 컬럼 설정
# =====================================================

age_columns = {
    "0~9세": "2026년04월_거주자_0~9세",
    "10~19세": "2026년04월_거주자_10~19세",
    "20~29세": "2026년04월_거주자_20~29세",
    "30~39세": "2026년04월_거주자_30~39세",
    "40~49세": "2026년04월_거주자_40~49세",
    "50~59세": "2026년04월_거주자_50~59세",
    "60~69세": "2026년04월_거주자_60~69세",
    "70~79세": "2026년04월_거주자_70~79세",
    "80~89세": "2026년04월_거주자_80~89세",
    "90~99세": "2026년04월_거주자_90~99세",
    "100세 이상": "2026년04월_거주자_100세 이상"
}

# =====================================================
# 숫자 변환
# =====================================================

for col in age_columns.values():
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(",", "")
        .astype(int)
    )

# =====================================================
# 동네별 연령 그래프
# =====================================================

st.header("동네별 연령 인구 그래프")

dong_list = sorted(df["행정구역"].unique())

selected_dong = st.selectbox(
    "동네를 선택하세요",
    dong_list
)

selected_row = df[df["행정구역"] == selected_dong].iloc[0]

age_labels = list(age_columns.keys())

population_values = []

for col in age_columns.values():
    population_values.append(selected_row[col])

# Plotly 그래프 생성

fig1 = go.Figure()

fig1.add_trace(
    go.Scatter(
        x=age_labels,
        y=population_values,
        mode="lines+markers",
        line=dict(
            color="red",
            width=3
        ),
        marker=dict(
            size=10
        ),
        hovertemplate=
        "<b>age</b>: %{x}<br>" +
        "<b>population</b>: %{y}명<extra></extra>"
    )
)

fig1.update_layout(
    title="의정부 동네별 인구수",
    xaxis_title="age",
    yaxis_title="population",
    plot_bgcolor="lightgray",
    paper_bgcolor="lightgray",
    font=dict(
        size=14
    )
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# =====================================================
# 연령대별 TOP5 행정구역 그래프
# =====================================================

st.header("연령대별 인구 TOP5 행정구역")

selected_age = st.selectbox(
    "연령대를 선택하세요",
    list(age_columns.keys())
)

selected_column = age_columns[selected_age]

# TOP5 추출

top5_df = (
    df.sort_values(
        by=selected_column,
        ascending=False
    )
    .head(5)
)

# Plotly 그래프 생성

fig2 = go.Figure()

fig2.add_trace(
    go.Scatter(
        x=top5_df["행정구역"],
        y=top5_df[selected_column],
        mode="lines+markers",
        line=dict(
            color="red",
            width=3
        ),
        marker=dict(
            size=10
        ),
        hovertemplate=
        "<b>행정구역</b>: %{x}<br>" +
        "<b>population</b>: %{y}명<extra></extra>"
    )
)

fig2.update_layout(
    title=f"{selected_age} 인구 TOP5 행정구역",
    xaxis_title="age",
    yaxis_title="population",
    plot_bgcolor="lightgray",
    paper_bgcolor="lightgray",
    font=dict(
        size=14
    )
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
