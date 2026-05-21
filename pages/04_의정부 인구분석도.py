import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 한글 깨짐 방지
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
df = pd.read_csv("population.csv")

# 컬럼명 공백 제거
df.columns = df.columns.str.strip()

# -----------------------------
# 실제 컬럼명 확인
# -----------------------------
st.write("컬럼명:", df.columns.tolist())

# 아래 컬럼명을 CSV에 맞게 수정
dong_col = "행정동"
age_col = "연령"
pop_col = "인구수"

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

# 나이순 정렬
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
