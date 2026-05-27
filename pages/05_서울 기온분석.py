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

# 데이터 불러오기
@st.cache_data
def load_data():

    # utf-8 실패하면 cp949 시도
    try:
        df = pd.read_csv("seoul.csv", encoding="utf-8")
    except:
        df = pd.read_csv("seoul.csv", encoding="cp949")

    # 날짜 변환
    df["날짜"] = pd.to_datetime(
        df["날짜"],
        errors="coerce"
    )

    # 날짜 변환 실패 행 제거
    df = df.dropna(subset=["날짜"])

    # 컬럼 생성
    df["연도"] = df["날짜"].dt.year
    df["월"] = df["날짜"].dt.month
    df["일"] = df["날짜"].dt.day

    return df

df = load_data()

# 사이드바
st.sidebar.header("날짜 선택")

month = st.sidebar.selectbox(
    "월 선택",
    sorted(df["월"].unique())
)

day = st.sidebar.selectbox(
    "일 선택",
    sorted(df[df["월"] == month]["일"].unique())
)

# 데이터 필터링
filtered = df[
    (df["월"] == month) &
    (df["일"] == day)
]

result = filtered[
    ["연도", "최고기온(℃)", "최저기온(℃)"]
].dropna()

# 그래프
st.subheader(f"📅 {month}월 {day}일의 연도별 기온 변화")

fig, ax = plt.subplots(figsize=(12, 6))

# 최고기온
ax.plot(
    result["연도"],
    result["최고기온(℃)"],
    color="hotpink",
    linewidth=2,
    label="최고기온"
)

# 최저기온
ax.plot(
    result["연도"],
    result["최저기온(℃)"],
    color="lightblue",
    linewidth=2,
    label="최저기온"
)

# 그래프 설정
ax.set_xlabel("연도")
ax.set_ylabel("기온(℃)")
ax.set_title(f"{month}월 {day}일 기온 변화")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# 표 출력
st.subheader("📋 데이터")
st.dataframe(result, use_container_width=True)
