import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 페이지 설정
st.set_page_config(
    page_title="서울 기온 분석",
    page_icon="🌡️",
    layout="wide"
)

st.title("🌡️ 서울 특정 날짜 기온 변화 분석")

# CSV 파일 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("seoul.csv", encoding="cp949")

    # 날짜 처리
    df["날짜"] = pd.to_datetime(df["날짜"])

    # 월, 일, 연도 컬럼 생성
    df["월"] = df["날짜"].dt.month
    df["일"] = df["날짜"].dt.day
    df["연도"] = df["날짜"].dt.year

    return df

df = load_data()

# 월/일 선택
st.sidebar.header("날짜 선택")

month = st.sidebar.selectbox(
    "월 선택",
    sorted(df["월"].unique())
)

day = st.sidebar.selectbox(
    "일 선택",
    sorted(df[df["월"] == month]["일"].unique())
)

# 선택 날짜 데이터 필터링
filtered = df[(df["월"] == month) & (df["일"] == day)]

# 필요한 컬럼만 정리
result = filtered[["연도", "최고기온(℃)", "최저기온(℃)"]].dropna()

st.subheader(f"📅 {month}월 {day}일의 연도별 기온 변화")

# 그래프 생성
fig, ax = plt.subplots(figsize=(12, 6))

# 최고기온
ax.plot(
    result["연도"],
    result["최고기온(℃)"],
    color="hotpink",
    label="최고기온",
    linewidth=2
)

# 최저기온
ax.plot(
    result["연도"],
    result["최저기온(℃)"],
    color="lightblue",
    label="최저기온",
    linewidth=2
)

# 그래프 꾸미기
ax.set_title(f"{month}월 {day}일 연도별 최고/최저기온 변화")
ax.set_xlabel("연도")
ax.set_ylabel("기온(℃)")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# 데이터 테이블
st.subheader("📋 데이터 보기")
st.dataframe(result, use_container_width=True)


