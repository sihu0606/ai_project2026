import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 한글 설정
# -----------------------------
plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

# -----------------------------
# 제목
# -----------------------------
st.title("의정부 동네별 인구수")

# -----------------------------
# CSV 읽기
# -----------------------------
df = pd.read_csv("population.csv", encoding="cp949")

# -----------------------------
# 컬럼 설정
# -----------------------------
dong_col = "행정구역"

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
# 기존 기능 : 동네 선택 후 연령별 그래프
# =====================================================

st.header("동네별 연령 인구 그래프")

dong_list = df[dong_col].tolist()

selected_dong = st.selectbox(
    "동네를 선택하세요",
    dong_list
)

selected_row = df[df[dong_col] == selected_dong].iloc[0]

age_labels = list(age_columns.keys())

population_values = []

for col in age_columns.values():
    value = str(selected_row[col]).replace(",", "")
    population_values.append(int(value))

# 그래프 생성
fig1, ax1 = plt.subplots(figsize=(12, 6))

# 회색 배경
fig1.patch.set_facecolor("lightgray")
ax1.set_facecolor("lightgray")

# 빨간색 꺾은선 그래프
ax1.plot(
    age_labels,
    population_values,
    color="red",
    marker="o",
    linewidth=2
)

ax1.set_title("의정부 동네별 인구수", fontsize=18)
ax1.set_xlabel("나이")
ax1.set_ylabel("인구수")

ax1.grid(True)

st.pyplot(fig1)

# =====================================================
# 추가 기능 : 연령대 선택 후 TOP5 행정구역 그래프
# =====================================================

st.header("연령대별 인구 TOP5 행정구역")

selected_age = st.selectbox(
    "연령대를 선택하세요",
    list(age_columns.keys())
)

selected_column = age_columns[selected_age]

# 숫자 변환
df[selected_column] = (
    df[selected_column]
    .astype(str)
    .str.replace(",", "")
    .astype(int)
)

# TOP5 추출
top5_df = df.sort_values(
    by=selected_column,
    ascending=False
).head(5)

# 그래프 데이터
top5_dongs = top5_df[dong_col]
top5_values = top5_df[selected_column]

# 그래프 생성
fig2, ax2 = plt.subplots(figsize=(12, 6))

# 회색 배경
fig2.patch.set_facecolor("lightgray")
ax2.set_facecolor("lightgray")

# 빨간색 꺾은선 그래프
ax2.plot(
    top5_dongs,
    top5_values,
    color="red",
    marker="o",
    linewidth=2
)

ax2.set_title(f"{selected_age} 인구 TOP5 행정구역", fontsize=18)
ax2.set_xlabel("행정구역")
ax2.set_ylabel("인구수")

ax2.grid(True)

st.pyplot(fig2)
