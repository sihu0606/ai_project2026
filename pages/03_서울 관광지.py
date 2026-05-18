import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="서울 관광지 TOP10", layout="wide")

st.title("🌏 외국인들이 좋아하는 서울 관광지 TOP10")
st.markdown("폴리움(Folium) 기반 인터랙티브 지도")

# 관광지 데이터
places = [
    {
        "name": "경복궁",
        "lat": 37.579617,
        "lon": 126.977041,
        "subway": "경복궁역(3호선)",
        "summary": "한복 체험, 궁궐 야경, 북촌한옥마을 산책 가능"
    },
    {
        "name": "명동",
        "lat": 37.563757,
        "lon": 126.985302,
        "subway": "명동역(4호선)",
        "summary": "K-뷰티 쇼핑, 길거리 음식, 야간 쇼핑 명소"
    },
    {
        "name": "N서울타워",
        "lat": 37.551169,
        "lon": 126.988227,
        "subway": "명동역(4호선)",
        "summary": "서울 야경, 케이블카, 사랑의 자물쇠 명소"
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.582604,
        "lon": 126.983998,
        "subway": "안국역(3호선)",
        "summary": "전통 한옥 체험과 감성 카페 투어 가능"
    },
    {
        "name": "홍대거리",
        "lat": 37.556268,
        "lon": 126.922641,
        "subway": "홍대입구역(2호선)",
        "summary": "버스킹, 클럽, 맛집과 젊은 감성 거리"
    },
    {
        "name": "강남",
        "lat": 37.497942,
        "lon": 127.027621,
        "subway": "강남역(2호선)",
        "summary": "쇼핑, 코엑스, K-pop 핫플레이스"
    },
    {
        "name": "롯데월드",
        "lat": 37.511115,
        "lon": 127.098167,
        "subway": "잠실역(2호선)",
        "summary": "실내 테마파크와 석촌호수 산책 가능"
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "lat": 37.566526,
        "lon": 127.009223,
        "subway": "동대문역사문화공원역",
        "summary": "야간 포토존과 디자인 전시 관람 가능"
    },
    {
        "name": "한강공원",
        "lat": 37.528316,
        "lon": 126.932599,
        "subway": "여의나루역(5호선)",
        "summary": "치맥, 자전거, 한강 유람선 즐기기 좋음"
    },
    {
        "name": "코엑스",
        "lat": 37.512524,
        "lon": 127.058819,
        "subway": "삼성역(2호선)",
        "summary": "별마당도서관, 쇼핑, 아쿠아리움 인기"
    }
]

# 기본 지도 생성
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11,
    tiles="CartoDB positron"
)

# 마커 추가
for place in places:
    popup_html = f"""
    <b>{place['name']}</b><br>
    🚇 가까운 지하철역: {place['subway']}<br>
    🎈 놀거리: {place['summary']}
    """

    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=folium.Popup(popup_html, max_width=300),
        tooltip=place["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# 세션 상태 초기화
if "selected_place" not in st.session_state:
    st.session_state.selected_place = None

# 지도 출력
map_data = st_folium(
    m,
    width=1000,
    height=600
)

# 클릭된 마커 처리
if map_data["last_object_clicked_popup"]:
    st.session_state.selected_place = map_data["last_object_clicked_popup"]

# 하단 정보 출력
st.markdown("---")
st.subheader("📍 관광지 정보")

if st.session_state.selected_place:
    st.info(st.session_state.selected_place)
else:
    st.write("지도의 관광지를 클릭해보세요.")
