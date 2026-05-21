import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import platform

# -----------------------------
# 한글 폰트 설정
# -----------------------------
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin':
    plt.rc('font', family='AppleGothic')
else:
    plt.rc('font', family='NanumGothic')

plt.rcParams['axes.unicode_minus'] = False

# -----------------------------
# 페이지 제목
# -----------------------------
st.title("의정부 동네별 인구수")

# -----------------------------
# CSV 파일 불러오기
# -----------------------------
df = pd.read_csv("population.csv")

# 컬럼 공백 제거
df.columns = [col.strip() for col in df.columns]

# -----------------------------
# 컬럼명 설정
# -----------------------------
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
# 선택된 동네 데이터 필터링
# -----------------------------
filtered_df = df[df[dong_col] == selected_dong]

# 나이순 정렬
filtered_df = filtered_df.sort_values(by=age_col)

# -----------------------------
# 그래프 생성
# -----------------------------
fig, ax = plt.subplots(figsize=(12, 6))

# 회색 배경
fig.patch.set_facecolor('lightgray')
ax.set_facecolor('lightgray')

# 빨간색 꺾은선 그래프
ax.plot(
    filtered_df[age_col],
    filtered_df[pop_col],
    color='red',
    marker='o',
    linewidth=2
)

# 제목 및 축 이름
ax.set_title("의정부 동네별 인구수", fontsize=18)
ax.set_xlabel("나이", fontsize=12)
ax.set_ylabel("인구수", fontsize=12)

# x축 글자 회전
plt.xticks(rotation=45)

# 격자 추가
ax.grid(True)

# Streamlit 출력
st.pyplot(fig)
