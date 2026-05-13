import streamlit as st

st.set_page_config(page_title="MBTI 책 & 영화 추천", page_icon="📚", layout="centered")

st.title("📚 MBTI 책 & 영화 추천 프로그램")
st.write("MBTI를 선택하면 어울리는 책과 영화를 추천해드립니다!")

mbti_data = {
    "INTJ": {
        "book": {
            "title": "사피엔스",
            "year": "2015",
            "price": "약 22,000원",
            "feature": "깊은 통찰과 분석적인 사고를 자극하는 역사 교양서"
        },
        "movie": {
            "title": "인터스텔라",
            "year": "2014",
            "price": "대여 약 5,000원",
            "feature": "과학적 사고와 철학적 메시지가 담긴 SF 영화"
        }
    },
    "INTP": {
        "book": {
            "title": "코스모스",
            "year": "2006",
            "price": "약 18,000원",
            "feature": "우주와 과학에 대한 호기심을 자극하는 책"
        },
        "movie": {
            "title": "매트릭스",
            "year": "1999",
            "price": "대여 약 4,000원",
            "feature": "철학적 질문과 창의적인 세계관이 특징"
        }
    },
    "ENTJ": {
        "book": {
            "title": "성공하는 사람들의 7가지 습관",
            "year": "2014",
            "price": "약 17,000원",
            "feature": "리더십과 자기계발에 도움을 주는 책"
        },
        "movie": {
            "title": "아이언맨",
            "year": "2008",
            "price": "대여 약 4,500원",
            "feature": "카리스마 있는 리더형 주인공이 매력적인 영화"
        }
    },
    "ENTP": {
        "book": {
            "title": "아웃라이어",
            "year": "2009",
            "price": "약 16,000원",
            "feature": "새로운 시각과 창의적인 사고를 다루는 책"
        },
        "movie": {
            "title": "인셉션",
            "year": "2010",
            "price": "대여 약 5,000원",
            "feature": "독창적인 전개와 반전이 특징인 영화"
        }
    },
    "INFJ": {
        "book": {
            "title": "어린 왕자",
            "year": "1943",
            "price": "약 12,000원",
            "feature": "감성적이고 깊은 의미를 담은 소설"
        },
        "movie": {
            "title": "코코",
            "year": "2017",
            "price": "대여 약 5,000원",
            "feature": "가족과 꿈에 대한 따뜻한 메시지를 전달"
        }
    },
    "INFP": {
        "book": {
            "title": "데미안",
            "year": "1919",
            "price": "약 9,000원",
            "feature": "자아 탐색과 성장 이야기를 담은 작품"
        },
        "movie": {
            "title": "월터의 상상은 현실이 된다",
            "year": "2013",
            "price": "대여 약 4,500원",
            "feature": "꿈과 도전을 응원하는 감성 영화"
        }
    },
    "ENFJ": {
        "book": {
            "title": "미움받을 용기",
            "year": "2014",
            "price": "약 15,000원",
            "feature": "인간관계와 성장에 대한 조언이 담긴 책"
        },
        "movie": {
            "title": "죽은 시인의 사회",
            "year": "1989",
            "price": "대여 약 4,000원",
            "feature": "사람들에게 영감을 주는 감동 영화"
        }
    },
    "ENFP": {
        "book": {
            "title": "트렌드 코리아",
            "year": "2025",
            "price": "약 19,000원",
            "feature": "새로운 아이디어와 흐름을 파악하기 좋은 책"
        },
        "movie": {
            "title": "라라랜드",
            "year": "2016",
            "price": "대여 약 5,000원",
            "feature": "열정과 꿈을 표현한 뮤지컬 영화"
        }
    },
    "ISTJ": {
        "book": {
            "title": "넛지",
            "year": "2008",
            "price": "약 18,000원",
            "feature": "체계적이고 현실적인 사고를 돕는 경제학 책"
        },
        "movie": {
            "title": "머니볼",
            "year": "2011",
            "price": "대여 약 4,500원",
            "feature": "데이터와 전략 중심의 실화 영화"
        }
    },
    "ISFJ": {
        "book": {
            "title": "아몬드",
            "year": "2017",
            "price": "약 14,000원",
            "feature": "따뜻한 감정과 성장 이야기를 담은 소설"
        },
        "movie": {
            "title": "인사이드 아웃",
            "year": "2015",
            "price": "대여 약 5,000원",
            "feature": "감정을 섬세하게 표현한 애니메이션"
        }
    },
    "ISTP": {
        "book": {
            "title": "팩트풀니스",
            "year": "2019",
            "price": "약 19,000원",
            "feature": "현실적 사고와 문제 해결 능력을 키워주는 책"
        },
        "movie": {
            "title": "탑건: 매버릭",
            "year": "2022",
            "price": "대여 약 6,000원",
            "feature": "스릴과 뛰어난 액션이 특징인 영화"
        }
    },
    "ISFP": {
        "book": {
            "title": "나미야 잡화점의 기적",
            "year": "2012",
            "price": "약 15,000원",
            "feature": "따뜻한 감성과 위로를 주는 이야기"
        },
        "movie": {
            "title": "비긴 어게인",
            "year": "2013",
            "price": "대여 약 4,500원",
            "feature": "음악과 감성이 어우러진 힐링 영화"
        }
    },
    "ESTJ": {
        "book": {
            "title": "원칙",
            "year": "2018",
            "price": "약 35,000원",
            "feature": "효율성과 조직 관리에 도움을 주는 책"
        },
        "movie": {
            "title": "포드 V 페라리",
            "year": "2019",
            "price": "대여 약 5,000원",
            "feature": "목표 달성과 팀워크를 강조한 영화"
        }
    },
    "ESFJ": {
        "book": {
            "title": "관계를 읽는 시간",
            "year": "2021",
            "price": "약 16,000원",
            "feature": "인간관계와 공감 능력을 다루는 책"
        },
        "movie": {
            "title": "맘마미아!",
            "year": "2008",
            "price": "대여 약 4,000원",
            "feature": "밝고 따뜻한 분위기의 뮤지컬 영화"
        }
    },
    "ESTP": {
        "book": {
            "title": "그릿",
            "year": "2016",
            "price": "약 18,000원",
            "feature": "도전 정신과 실행력을 강조하는 책"
        },
        "movie": {
            "title": "분노의 질주",
            "year": "2001",
            "price": "대여 약 4,000원",
            "feature": "속도감과 액션이 매력적인 영화"
        }
    },
    "ESFP": {
        "book": {
            "title": "멈추면 비로소 보이는 것들",
            "year": "2012",
            "price": "약 14,000원",
            "feature": "긍정적이고 편안한 메시지를 담은 에세이"
        },
        "movie": {
            "title": "위대한 쇼맨",
            "year": "2017",
            "price": "대여 약 5,000원",
            "feature": "화려한 음악과 퍼포먼스가 특징인 영화"
        }
    }
}

mbti_list = list(mbti_data.keys())
selected_mbti = st.selectbox("MBTI를 선택하세요", mbti_list)

if selected_mbti:
    data = mbti_data[selected_mbti]

    st.markdown("---")
    st.subheader(f"📖 {selected_mbti} 추천 책")
    st.write(f"📚 제목: {data['book']['title']}")
    st.write(f"📅 출간 연도: {data['book']['year']}")
    st.write(f"💰 가격: {data['book']['price']}")
    st.write(f"✨ 특징: {data['book']['feature']}")

    st.markdown("---")
    st.subheader(f"🎬 {selected_mbti} 추천 영화")
    st.write(f"🎥 제목: {data['movie']['title']}")
    st.write(f"📅 개봉 연도: {data['movie']['year']}")
    st.write(f"💰 가격: {data['movie']['price']}")
    st.write(f"✨ 특징: {data['movie']['feature']}")

st.markdown("---")
st.caption("Made with Streamlit")

