import streamlit as st
import random

st.set_page_config(
    page_title="조주기능사 칵테일 학습",
    page_icon="🍸",
    layout="wide"
)

cocktails = {

    "Brandy": {

        "Pousse Cafe": {
            "조주법": "Float",
            "글라스": "Stemmed Liqueur Glass",
            "가니쉬": "없음",
            "레시피": [
                "Grenadine Syrup 1/3 part",
                "Creme De Menthe(Green) 1/3 part",
                "Brandy 1/3 part"
            ],
            "디저트": "체리 무스 케이크",
            "설명": "체리와 민트 계열 향이 브랜디의 달콤함과 잘 어울린다."
        },

        "Brandy Alexander": {
            "조주법": "Shake",
            "글라스": "Cocktail Glass",
            "가니쉬": "Nutmeg Powder",
            "레시피": [
                "Brandy 3/4oz",
                "Creme De Cacao(Brown) 3/4oz",
                "Light Milk 3/4oz"
            ],
            "디저트": "티라미수",
            "설명": "초콜릿과 유제품 풍미가 티라미수와 훌륭하게 조화된다."
        },

        "Sidecar": {
            "조주법": "Shake",
            "글라스": "Cocktail Glass",
            "가니쉬": "없음",
            "레시피": [
                "Brandy 1oz",
                "Triple Sec 1oz",
                "Lemon Juice 1/4oz"
            ],
            "디저트": "오렌지 마들렌",
            "설명": "시트러스 계열 향을 더욱 풍부하게 느끼게 해준다."
        },

        "Apricot Cocktail": {
            "조주법": "Shake",
            "글라스": "Cocktail Glass",
            "가니쉬": "없음",
            "레시피": [
                "Apricot Brandy 1 1/2oz",
                "Dry Gin 1 tsp",
                "Lemon Juice 1/2oz",
                "Orange Juice 1/2oz"
            ],
            "디저트": "살구 타르트",
            "설명": "살구 풍미를 자연스럽게 연결한다."
        },

        "Honeymoon Cocktail": {
            "조주법": "Shake",
            "글라스": "Cocktail Glass",
            "가니쉬": "없음",
            "레시피": [
                "Apple Brandy 3/4oz",
                "Benedictine DOM 3/4oz",
                "Triple Sec 1/4oz",
                "Lemon Juice 1/2oz"
            ],
            "디저트": "애플파이",
            "설명": "사과 향과 시나몬 계열 디저트가 잘 어울린다."
        }
    },

    "Whiskey": {

        "Manhattan": {
            "조주법": "Stir",
            "글라스": "Cocktail Glass",
            "가니쉬": "Cherry",
            "레시피": [
                "Bourbon Whiskey 1 1/2oz",
                "Sweet Vermouth 3/4oz",
                "Angostura Bitters 1dash"
            ],
            "디저트": "다크 초콜릿 브라우니",
            "설명": "위스키와 초콜릿 풍미가 훌륭한 조화를 만든다."
        },

        "Old Fashioned": {
            "조주법": "Build",
            "글라스": "Old-fashioned Glass",
            "가니쉬": "Orange & Cherry",
            "레시피": [
                "Bourbon Whiskey 1 1/2oz",
                "Powdered Sugar 1tsp",
                "Angostura Bitters 1dash",
                "Soda Water 1/2oz"
            ],
            "디저트": "피칸 파이",
            "설명": "견과류와 카라멜 풍미가 잘 어울린다."
        },

        "Rusty Nail": {
            "조주법": "Build",
            "글라스": "Old-fashioned Glass",
            "가니쉬": "없음",
            "레시피": [
                "Scotch Whisky 1oz",
                "Drambuie 1/2oz"
            ],
            "디저트": "허니 케이크",
            "설명": "꿀 향과 스카치의 조화가 뛰어나다."
        },

        "Whiskey Sour": {
            "조주법": "Shake/Build",
            "글라스": "Sour Glass",
            "가니쉬": "Lemon & Cherry",
            "레시피": [
                "Bourbon Whiskey 1 1/2oz",
                "Lemon Juice 1/2oz",
                "Powdered Sugar 1tsp",
                "Soda Water 1oz"
            ],
            "디저트": "레몬 파운드 케이크",
            "설명": "레몬의 산미를 자연스럽게 연결한다."
        },

        "New York": {
            "조주법": "Shake",
            "글라스": "Cocktail Glass",
            "가니쉬": "Twist of Lemon Peel",
            "레시피": [
                "Bourbon Whiskey 1 1/2oz",
                "Lime Juice 1/2oz",
                "Powdered Sugar 1tsp",
                "Grenadine Syrup 1/2tsp"
            ],
            "디저트": "체리 치즈케이크",
            "설명": "그레나딘의 과일 향과 잘 어울린다."
        },

        "Boulevardier": {
            "조주법": "Stir",
            "글라스": "Old-fashioned Glass",
            "가니쉬": "Twist of Orange Peel",
            "레시피": [
                "Bourbon Whiskey 1oz",
                "Sweet Vermouth 1oz",
                "Campari 1oz"
            ],
            "디저트": "오렌지 초콜릿 타르트",
            "설명": "캄파리의 쌉쌀함을 초콜릿이 부드럽게 잡아준다."
        }
    },
        "Vodka": {

        "Bloody Mary": {
            "조주법": "Build",
            "글라스": "Highball Glass",
            "가니쉬": "Lemon/Celery",
            "레시피": [
                "Vodka 1 1/2oz",
                "Worcestershire Sauce 1tsp",
                "Tabasco Sauce 1dash",
                "Salt & Pepper",
                "Tomato Juice"
            ],
            "디저트": "토마토 타르트",
            "설명": "토마토 풍미와 허브 계열 디저트가 잘 어울린다."
        },

        "Black Russian": {
            "조주법": "Build",
            "글라스": "Old-fashioned Glass",
            "가니쉬": "없음",
            "레시피": [
                "Vodka 1oz",
                "Coffee Liqueur 1/2oz"
            ],
            "디저트": "티라미수",
            "설명": "커피 리큐르와 티라미수의 풍미가 자연스럽게 연결된다."
        },

        "Harvey Wallbanger": {
            "조주법": "Build/Float",
            "글라스": "Collins Glass",
            "가니쉬": "없음",
            "레시피": [
                "Vodka 1 1/2oz",
                "Orange Juice",
                "Galliano 1/2oz Float"
            ],
            "디저트": "오렌지 케이크",
            "설명": "오렌지 향을 더욱 풍부하게 만들어준다."
        },

        "Kiss of Fire": {
            "조주법": "Shake",
            "글라스": "Cocktail Glass",
            "가니쉬": "Sugar Rim",
            "레시피": [
                "Vodka 1oz",
                "Sloe Gin 1/2oz",
                "Dry Vermouth 1/2oz",
                "Lemon Juice 1tsp"
            ],
            "디저트": "라즈베리 무스",
            "설명": "달콤한 베리 향과 잘 어울린다."
        },

        "Seabreeze": {
            "조주법": "Build",
            "글라스": "Highball Glass",
            "가니쉬": "Lime/Lemon Wedge",
            "레시피": [
                "Vodka 1 1/2oz",
                "Cranberry Juice 3oz",
                "Grapefruit Juice 1/2oz"
            ],
            "디저트": "자몽 타르트",
            "설명": "상큼한 시트러스 향을 극대화한다."
        },

        "Apple Martini": {
            "조주법": "Shake",
            "글라스": "Cocktail Glass",
            "가니쉬": "Apple Slice",
            "레시피": [
                "Vodka 1oz",
                "Apple Pucker 1oz",
                "Lime Juice 1/2oz"
            ],
            "디저트": "애플파이",
            "설명": "사과 향이 디저트와 자연스럽게 이어진다."
        },

        "Cosmopolitan": {
            "조주법": "Shake",
            "글라스": "Cocktail Glass",
            "가니쉬": "Lime/Lemon Twist",
            "레시피": [
                "Vodka 1oz",
                "Triple Sec 1/2oz",
                "Lime Juice 1/2oz",
                "Cranberry Juice 1/2oz"
            ],
            "디저트": "베리 치즈케이크",
            "설명": "크랜베리의 산미와 베리류 디저트가 잘 어울린다."
        },

        "Moscow Mule": {
            "조주법": "Build",
            "글라스": "Highball Glass",
            "가니쉬": "Lime/Lemon Slice",
            "레시피": [
                "Vodka 1 1/2oz",
                "Lime Juice 1/2oz",
                "Ginger Ale"
            ],
            "디저트": "진저 쿠키",
            "설명": "생강 향을 더욱 부드럽게 즐길 수 있다."
        }
    },

    "Gin": {

        "Dry Martini": {
            "조주법": "Stir",
            "글라스": "Cocktail Glass",
            "가니쉬": "Green Olive",
            "레시피": [
                "Dry Gin 2oz",
                "Dry Vermouth 1/3oz"
            ],
            "디저트": "레몬 타르트",
            "설명": "드라이한 풍미와 상큼한 산미가 잘 어울린다."
        },

        "Singapore Sling": {
            "조주법": "Shake/Build",
            "글라스": "Footed Pilsner Glass",
            "가니쉬": "Orange & Cherry",
            "레시피": [
                "Dry Gin 1 1/2oz",
                "Lemon Juice 1/2oz",
                "Powdered Sugar 1tsp",
                "Club Soda",
                "Cherry Brandy 1/2oz Float"
            ],
            "디저트": "체리 타르트",
            "설명": "체리 향과 과일 디저트가 조화를 이룬다."
        },

        "Sloe Gin Fizz": {
            "조주법": "Shake/Build",
            "글라스": "Highball Glass",
            "가니쉬": "Lemon Slice",
            "레시피": [
                "Sloe Gin 1 1/2oz",
                "Lemon Juice 1/2oz",
                "Powdered Sugar 1tsp",
                "Club Soda"
            ],
            "디저트": "레몬 마들렌",
            "설명": "산뜻한 레몬 향을 살려준다."
        },

        "Negroni": {
            "조주법": "Build",
            "글라스": "Old-fashioned Glass",
            "가니쉬": "Twist of Lemon Peel",
            "레시피": [
                "Gin 3/4oz",
                "Sweet Vermouth 3/4oz",
                "Campari 3/4oz"
            ],
            "디저트": "오렌지 초콜릿",
            "설명": "캄파리의 쌉쌀함과 초콜릿이 잘 어울린다."
        },

        "Gin Fizz": {
            "조주법": "Shake/Build",
            "글라스": "Highball Glass",
            "가니쉬": "Lemon Slice",
            "레시피": [
                "Gin",
                "Lemon Juice",
                "Sugar",
                "Club Soda"
            ],
            "디저트": "레몬 쿠키",
            "설명": "산뜻한 레몬 풍미가 강조된다."
        }
    },

    "Tequila": {

        "Margarita": {
            "조주법": "Shake",
            "글라스": "Cocktail Glass",
            "가니쉬": "Salt Rim",
            "레시피": [
                "Tequila 1 1/2oz",
                "Triple Sec 1/2oz",
                "Lime Juice 1/2oz"
            ],
            "디저트": "치즈케이크",
            "설명": "라임의 산미와 치즈 풍미가 좋은 균형을 만든다."
        },

        "Tequila Sunrise": {
            "조주법": "Build/Float",
            "글라스": "Footed Pilsner Glass",
            "가니쉬": "없음",
            "레시피": [
                "Tequila 1 1/2oz",
                "Orange Juice",
                "Grenadine Syrup 1/2oz"
            ],
            "디저트": "오렌지 무스",
            "설명": "오렌지 향과 과일 디저트가 잘 어울린다."
        }
    },
        "Rum": {

        "Daiquiri": {
            "조주법": "Shake",
            "글라스": "Cocktail Glass",
            "가니쉬": "없음",
            "레시피": [
                "Light Rum 1 3/4oz",
                "Lime Juice 3/4oz",
                "Powdered Sugar 1tsp"
            ],
            "디저트": "코코넛 마카롱",
            "설명": "럼의 열대풍 향과 코코넛이 잘 어울린다."
        },

        "Bacardi Cocktail": {
            "조주법": "Shake",
            "글라스": "Cocktail Glass",
            "가니쉬": "없음",
            "레시피": [
                "Bacardi Rum 1 3/4oz",
                "Lime Juice 3/4oz",
                "Grenadine Syrup 1tsp"
            ],
            "디저트": "체리 타르트",
            "설명": "그레나딘의 과일 향을 더욱 살려준다."
        },

        "Cuba Libre": {
            "조주법": "Build",
            "글라스": "Highball Glass",
            "가니쉬": "Lime Wedge",
            "레시피": [
                "Light Rum 1 1/2oz",
                "Lime Juice 1/2oz",
                "Cola"
            ],
            "디저트": "초콜릿 브라우니",
            "설명": "콜라와 초콜릿의 풍미가 자연스럽게 연결된다."
        },

        "Mai-Tai": {
            "조주법": "Blend",
            "글라스": "Footed Pilsner Glass",
            "가니쉬": "Pineapple & Cherry",
            "레시피": [
                "Light Rum 1 1/4oz",
                "Triple Sec 3/4oz",
                "Lime Juice 1oz",
                "Pineapple Juice 1oz",
                "Orange Juice 1oz",
                "Grenadine 1/4oz"
            ],
            "디저트": "파인애플 케이크",
            "설명": "열대과일 향을 극대화한다."
        },

        "Pina Colada": {
            "조주법": "Blend",
            "글라스": "Footed Pilsner Glass",
            "가니쉬": "Pineapple & Cherry",
            "레시피": [
                "Light Rum 1 1/4oz",
                "Pina Colada Mix 2oz",
                "Pineapple Juice 2oz"
            ],
            "디저트": "코코넛 케이크",
            "설명": "코코넛 향이 풍부한 디저트와 잘 어울린다."
        },

        "Blue Hawaiian": {
            "조주법": "Blend",
            "글라스": "Footed Pilsner Glass",
            "가니쉬": "Pineapple & Cherry",
            "레시피": [
                "Light Rum 1oz",
                "Blue Curacao 1oz",
                "Coconut Rum 1oz",
                "Pineapple Juice 2 1/2oz"
            ],
            "디저트": "블루베리 치즈케이크",
            "설명": "과일 향과 치즈 풍미의 조화가 좋다."
        }
    },

    "기타": {

        "B-52": {
            "조주법": "Float",
            "글라스": "Sherry Glass",
            "가니쉬": "없음",
            "레시피": [
                "Coffee Liqueur 1/3",
                "Bailey's Irish Cream 1/3",
                "Grand Marnier 1/3"
            ],
            "디저트": "티라미수",
            "설명": "커피와 크림 향이 티라미수와 완벽하게 어울린다."
        },

        "June Bug": {
            "조주법": "Shake",
            "글라스": "Collins Glass",
            "가니쉬": "Pineapple & Cherry",
            "레시피": [
                "Midori",
                "Coconut Rum",
                "Banana Liqueur",
                "Pineapple Juice",
                "Sweet & Sour Mix"
            ],
            "디저트": "바나나 케이크",
            "설명": "열대과일 풍미를 강조한다."
        },

        "Grasshopper": {
            "조주법": "Shake",
            "글라스": "Champagne Glass",
            "가니쉬": "없음",
            "레시피": [
                "Creme de Menthe",
                "Creme de Cacao",
                "Light Milk"
            ],
            "디저트": "민트 초콜릿 브라우니",
            "설명": "민트초코 조합을 좋아한다면 최고의 선택."
        },

        "Kir": {
            "조주법": "Build",
            "글라스": "White Wine Glass",
            "가니쉬": "Twist of Lemon Peel",
            "레시피": [
                "White Wine 3oz",
                "Creme de Cassis 1/2oz"
            ],
            "디저트": "블랙베리 타르트",
            "설명": "카시스 향을 더욱 풍부하게 즐길 수 있다."
        },

        "Healing": {
            "조주법": "Shake",
            "글라스": "Cocktail Glass",
            "가니쉬": "Lemon Twist",
            "디저트": "꿀 케이크",
            "설명": "약재 향과 은은한 단맛이 잘 어울린다."
        },

        "Jindo": {
            "조주법": "Shake",
            "글라스": "Cocktail Glass",
            "가니쉬": "없음",
            "디저트": "포도 타르트",
            "설명": "포도 향과 과일 디저트가 잘 맞는다."
        },

        "Puppy Love": {
            "조주법": "Shake",
            "글라스": "Cocktail Glass",
            "가니쉬": "Apple Slice",
            "디저트": "애플파이",
            "설명": "사과 풍미를 강조한다."
        },

        "Geumsan": {
            "조주법": "Shake",
            "글라스": "Cocktail Glass",
            "가니쉬": "없음",
            "디저트": "인삼 꿀쿠키",
            "설명": "인삼주의 향을 부드럽게 즐길 수 있다."
        },

        "Gochang": {
            "조주법": "Stir",
            "글라스": "Flute Champagne Glass",
            "가니쉬": "없음",
            "디저트": "베리 무스",
            "설명": "복분자 향과 베리류 디저트가 잘 어울린다."
        },

        "Fresh Lemon Squash": {
            "조주법": "Build",
            "글라스": "Highball Glass",
            "가니쉬": "Lemon Slice",
            "디저트": "레몬 마들렌",
            "설명": "레몬 향을 극대화한다."
        },

        "Virgin Fruit Punch": {
            "조주법": "Build",
            "글라스": "Highball Glass",
            "가니쉬": "Orange & Cherry",
            "디저트": "과일 타르트",
            "설명": "다양한 과일 향과 잘 어울린다."
        }
    }
}
st.title("🍸 조주기능사 칵테일 & 디저트 페어링")

base = st.selectbox(
    "베이스 주종 선택",
    list(cocktails.keys())
)

cocktail = st.selectbox(
    "칵테일 선택",
    list(cocktails[base].keys())
)

info = cocktails[base][cocktail]

st.subheader(f"🍹 {cocktail}")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("조주법", info["조주법"])

with col2:
    st.metric("글라스", info["글라스"])

with col3:
    st.metric("가니쉬", info["가니쉬"])

st.divider()

st.subheader("📖 레시피")

if "레시피" in info:
    for item in info["레시피"]:
        st.write(f"• {item}")

st.divider()

st.subheader("🍰 추천 디저트")
st.success(info["디저트"])

st.subheader("✨ 페어링 설명")
st.info(info["설명"])

st.divider()

st.subheader("🎯 조주법 퀴즈")

all_cocktails = []
for category in cocktails.values():
    for name, data in category.items():
        all_cocktails.append((name, data["조주법"]))

question = random.choice(all_cocktails)

answer = st.selectbox(
    f"{question[0]}의 조주법은?",
    ["Build", "Shake", "Stir", "Blend", "Float", "Shake/Build", "Build/Float"]
)

if st.button("정답 확인"):
    if answer == question[1]:
        st.success("정답입니다! 🎉")
    else:
        st.error(f"오답입니다. 정답은 {question[1]} 입니다.")
