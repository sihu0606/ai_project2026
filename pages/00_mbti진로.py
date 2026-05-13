# MBTI 진로 추천 스트림릿 코드

python
import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천", page_icon="💼", layout="centered")

st.title("💼 MBTI 진로 추천 프로그램")
st.write("MBTI를 선택하면 추천 진로와 관련 정보를 알려드립니다!")

mbti_data = {
    "INTJ": {
        "career1": {
            "name": "데이터 분석가",
            "major": "데이터사이언스학과, 컴퓨터공학과",
            "personality": "논리적이고 분석적인 사람",
            "salary": "평균 연봉 약 5,500만원"
        },
        "career2": {
            "name": "전략 기획가",
            "major": "경영학과, 경제학과",
            "personality": "계획적이고 목표 지향적인 사람",
            "salary": "평균 연봉 약 6,000만원"
        }
    },
    "INTP": {
        "career1": {
            "name": "소프트웨어 개발자",
            "major": "컴퓨터공학과, 소프트웨어학과",
            "personality": "호기심이 많고 창의적인 사람",
            "salary": "평균 연봉 약 5,800만원"
        },
        "career2": {
            "name": "연구원",
            "major": "자연과학계열, 공학계열",
            "personality": "탐구심이 강한 사람",
            "salary": "평균 연봉 약 5,200만원"
        }
    },
    "ENTJ": {
        "career1": {
            "name": "CEO",
            "major": "경영학과, 경제학과",
            "personality": "리더십이 강하고 결단력 있는 사람",
            "salary": "평균 연봉 약 8,000만원"
        },
        "career2": {
            "name": "마케팅 매니저",
            "major": "광고홍보학과, 경영학과",
            "personality": "도전적이고 추진력 있는 사람",
            "salary": "평균 연봉 약 5,500만원"
        }
    },
    "ENTP": {
        "career1": {
            "name": "창업가",
            "major": "경영학과, 창업학과",
            "personality": "아이디어가 많고 활동적인 사람",
            "salary": "평균 연봉 약 6,500만원"
        },
        "career2": {
            "name": "광고 기획자",
            "major": "광고홍보학과, 미디어학과",
            "personality": "창의적이고 사교적인 사람",
            "salary": "평균 연봉 약 4,800만원"
        }
    },
    "INFJ": {
        "career1": {
            "name": "상담사",
            "major": "심리학과, 상담학과",
            "personality": "공감 능력이 뛰어난 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        "career2": {
            "name": "작가",
            "major": "문예창작학과, 국어국문학과",
            "personality": "감수성이 풍부한 사람",
            "salary": "평균 연봉 약 4,000만원"
        }
    },
    "INFP": {
        "career1": {
            "name": "일러스트레이터",
            "major": "디자인학과, 시각디자인학과",
            "personality": "상상력이 풍부한 사람",
            "salary": "평균 연봉 약 4,200만원"
        },
        "career2": {
            "name": "사회복지사",
            "major": "사회복지학과",
            "personality": "따뜻하고 배려심 있는 사람",
            "salary": "평균 연봉 약 3,800만원"
        }
    },
    "ENFJ": {
        "career1": {
            "name": "교사",
            "major": "교육학과, 국어교육과",
            "personality": "사람을 이끄는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        "career2": {
            "name": "인사 담당자",
            "major": "경영학과, 심리학과",
            "personality": "의사소통 능력이 좋은 사람",
            "salary": "평균 연봉 약 4,900만원"
        }
    },
    "ENFP": {
        "career1": {
            "name": "유튜버",
            "major": "미디어학과, 방송영상학과",
            "personality": "에너지가 넘치고 창의적인 사람",
            "salary": "평균 연봉 약 5,000만원 이상"
        },
        "career2": {
            "name": "이벤트 기획자",
            "major": "관광경영학과, 이벤트학과",
            "personality": "활동적이고 아이디어가 많은 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    },
    "ISTJ": {
        "career1": {
            "name": "공무원",
            "major": "행정학과, 법학과",
            "personality": "책임감이 강하고 성실한 사람",
            "salary": "평균 연봉 약 4,700만원"
        },
        "career2": {
            "name": "회계사",
            "major": "회계학과, 경영학과",
            "personality": "꼼꼼하고 체계적인 사람",
            "salary": "평균 연봉 약 7,000만원"
        }
    },
    "ISFJ": {
        "career1": {
            "name": "간호사",
            "major": "간호학과",
            "personality": "배려심이 깊고 책임감 있는 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        "career2": {
            "name": "초등교사",
            "major": "초등교육과",
            "personality": "친절하고 인내심 있는 사람",
            "salary": "평균 연봉 약 5,200만원"
        }
    },
    "ISTP": {
        "career1": {
            "name": "자동차 엔지니어",
            "major": "기계공학과, 자동차공학과",
            "personality": "문제 해결 능력이 뛰어난 사람",
            "salary": "평균 연봉 약 5,500만원"
        },
        "career2": {
            "name": "파일럿",
            "major": "항공운항학과",
            "personality": "침착하고 집중력이 좋은 사람",
            "salary": "평균 연봉 약 8,000만원"
        }
    },
    "ISFP": {
        "career1": {
            "name": "플로리스트",
            "major": "원예학과, 플로리스트학과",
            "personality": "감각적이고 섬세한 사람",
            "salary": "평균 연봉 약 3,800만원"
        },
        "career2": {
            "name": "패션 디자이너",
            "major": "패션디자인학과",
            "personality": "예술 감각이 뛰어난 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    },
    "ESTJ": {
        "career1": {
            "name": "경찰관",
            "major": "경찰행정학과",
            "personality": "원칙적이고 리더십 있는 사람",
            "salary": "평균 연봉 약 5,200만원"
        },
        "career2": {
            "name": "은행원",
            "major": "금융학과, 경제학과",
            "personality": "체계적이고 신뢰감 있는 사람",
            "salary": "평균 연봉 약 5,500만원"
        }
    },
    "ESFJ": {
        "career1": {
            "name": "승무원",
            "major": "항공서비스학과",
            "personality": "친절하고 사교적인 사람",
            "salary": "평균 연봉 약 4,800만원"
        },
        "career2": {
            "name": "호텔리어",
            "major": "호텔경영학과",
            "personality": "서비스 정신이 뛰어난 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    },
    "ESTP": {
        "career1": {
            "name": "영업 전문가",
            "major": "경영학과, 무역학과",
            "personality": "사교적이고 도전적인 사람",
            "salary": "평균 연봉 약 5,300만원"
        },
        "career2": {
            "name": "스포츠 코치",
            "major": "체육학과",
            "personality": "활동적이고 리더십 있는 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    },
    "ESFP": {
        "career1": {
            "name": "연예인",
            "major": "연극영화과, 실용음악과",
            "personality": "사람들과 어울리기 좋아하는 사람",
            "salary": "평균 연봉 약 5,000만원 이상"
        },
        "career2": {
            "name": "파티 플래너",
            "major": "이벤트학과, 관광경영학과",
            "personality": "밝고 활발한 사람",
            "salary": "평균 연봉 약 4,300만원"
        }
    }
}

mbti_list = list(mbti_data.keys())
selected_mbti = st.selectbox("MBTI를 선택하세요", mbti_list)

if selected_mbti:
    st.subheader(f"✨ {selected_mbti} 추천 진로")

    data = mbti_data[selected_mbti]

    for key in ["career1", "career2"]:
        career = data[key]

        st.markdown("---")
        st.markdown(f"## 📌 {career['name']}")
        st.write(f"🎓 추천 학과: {career['major']}")
        st.write(f"😊 잘 맞는 성격: {career['personality']}")
        st.write(f"💰 {career['salary']}")

st.markdown("---")
st.caption("Made with Streamlit")

