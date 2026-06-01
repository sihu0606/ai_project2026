import streamlit as st

st.title("🍸 조주기능사 칵테일 학습")

cocktails = {
    "Vodka": {
        "Bloody Mary": {
            "조주법": "Build",
            "가니쉬": "Lemon, Celery",
            "레시피": [
                "Vodka 1 1/2oz",
                "Tomato Juice",
                "Worcestershire Sauce",
                "Tabasco"
            ],
            "디저트": "토마토 타르트",
            "설명": "토마토 풍미를 자연스럽게 연결"
        },

        "Cosmopolitan": {
            "조주법": "Shake",
            "가니쉬": "Lemon Twist",
            "레시피": [
                "Vodka 1oz",
                "Triple Sec 1/2oz",
                "Lime Juice 1/2oz",
                "Cranberry Juice 1/2oz"
            ],
            "디저트": "베리 치즈케이크",
            "설명": "크랜베리 향과 베리류 디저트가 잘 어울림"
        }
    },

    "Rum": {
        "Daiquiri": {
            "조주법": "Shake",
            "가니쉬": "없음",
            "레시피": [
                "Light Rum 1 3/4oz",
                "Lime Juice 3/4oz",
                "Sugar"
            ],
            "디저트": "코코넛 마카롱",
            "설명": "열대과일 향과 좋은 조화"
        }
    },

    "Gin": {
        "Dry Martini": {
            "조주법": "Stir",
            "가니쉬": "Olive",
            "레시피": [
                "Dry Gin 2oz",
                "Dry Vermouth 1/3oz"
            ],
            "디저트": "레몬 타르트",
            "설명": "깔끔한 드라이함과 상큼한 산미"
        }
    }
}

base = st.selectbox(
    "베이스 주종 선택",
    list(cocktails.keys())
)

recipe = st.selectbox(
    "칵테일 선택",
    list(cocktails[base].keys())
)

info = cocktails[base][recipe]

st.subheader(f"🍹 {recipe}")

st.write("### 조주법")
st.success(info["조주법"])

st.write("### 가니쉬")
st.info(info["가니쉬"])

st.write("### 레시피")

for item in info["레시피"]:
    st.write(f"• {item}")

st.write("### 추천 디저트")
st.warning(info["디저트"])

st.write("### 페어링 설명")
st.write(info["설명"])
