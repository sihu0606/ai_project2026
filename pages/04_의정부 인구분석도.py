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
try:
    df = pd.read_csv("population.csv", encoding="cp949")
except:
    df = pd.read_csv("population.csv", encoding="euc-kr")

# 컬럼명 공백 제거
df.columns = df.columns.str.strip()

# 실제 컬럼명 출력
st.write("현재 컬럼명:", df.columns.tolist())

# -----------------------------
# 컬럼 자동 찾기
# -----------------------------
dong_col = None
age_col = None
pop_col = None

for col in df.columns:
    if "동" in col:
        dong_col = col
    elif "나이" in col or "연령" in col:
        age_col = col
    elif "인구" in col:
        pop_col = col

# 컬럼 확인
if dong_col is None or age_col is None or pop_col is None:
    st.error("CSV 컬럼명을 찾을 수 없습니다.")
    st.stop()

# -----------------------------
# 동네 선택
# -----------------------------
dong_list = sorted(df[dong_col].unique())

selected_dong = st.selectbox(
    "동네를 선택하세요",
    dong_list
)

# -----------------------------
# 데이터 필터링
# -----------------------------
filtered_df = df[df[dong_col] == selected_dong]

# 숫자 변환
filtered_df[pop_col] = pd.to_numeric(
    filtered_df[pop_col],
    errors='coerce'
)

# 정렬
filtered_df = filtered_df.sort_values(by=age_col)

# -----------------------------
# 그래프 생성
# -----------------------------
fig, ax = plt.subplots(figsize=(12, 6))

# 회색 배경
fig.patch.set_facecolor("lightgray")
ax.set_facecolor("lightgray")

# 빨간색 꺾은선 그래프
ax.plot(
    filtered_df[age_col],
    filtered_df[pop_col],
    color="red",
    marker="o",
    linewidth=2
)

# 제목 및 축
ax.set_title("의정부 동네별 인구수", fontsize=18)
ax.set_xlabel("나이")
ax.set_ylabel("인구수")

# x축 회전
plt.xticks(rotation=45)

# 격자
ax.grid(True)

# 출력
st.pyplot(fig)
