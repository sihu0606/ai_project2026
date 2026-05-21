import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 한글 설정
# -----------------------------
plt.rcParams['font.family'] = 'DejaVu Sans'
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
# 필요한 컬럼
# -----------------------------
dong_col = "행정구역"

age_columns = [
    "2026년04월_거주자_0~9세",
    "2026년04월_거주자_10~19세",
    "2026년04월_거주자_20~29세",
    "2026년04월_거주자_30~39세",
    "2026년04월_거주자_40~49세",
    "2026년04월_거주자_50~59세",
    "2026년04월_거주자_60~69세",
    "2026년04월_거주자_70~79세",
    "2026년04월_거주자_80~89세",
    "2026년04월_거주자_90~99세",
    "2026년04월_거주자_100세 이상"
]

# -----------------------------
# 동네 목록 만들기
# -----------------------------
dong_list = df[dong_col].tolist()

selected_dong = st.selectbox(
    "동네를 선택하세요",
    dong_list
)

# -----------------------------
# 선택된 동 데이터
# -----------------------------
selected_row = df[df[dong_col] == selected_dong].iloc[0]

# 나이 labels
age_labels = [
    "0~9세",
    "10~19세",
    "20~29세",
    "30~39세",
    "40~49세",
    "50~59세",
    "60~69세",
    "70~79세",
    "80~89세",
    "90~99세",
    "100세 이상"
]

# 인구 데이터
population_values = []

for col in age_columns:
    value = str(selected_row[col]).replace(",", "")
    population_values.append(int(value))

# -----------------------------
# 그래프 생성
# -----------------------------
fig, ax = plt.subplots(figsize=(12, 6))

# 회색 배경
fig.patch.set_facecolor("lightgray")
ax.set_facecolor("lightgray")

# 빨간색 꺾은선 그래프
ax.plot(
    age_labels,
    population_values,
    color="red",
    marker="o",
    linewidth=2
)

# 제목 및 축
ax.set_title("의정부 동네별 인구수", fontsize=18)
ax.set_xlabel("나이")
ax.set_ylabel("인구수")

# 격자
ax.grid(True)

# 출력
st.pyplot(fig)
