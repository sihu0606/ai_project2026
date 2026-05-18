import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="서울 관광지 TOP10", layout="wide")

st.title("🌏 외국인 인기 서울 관광지 TOP10")

places = [
    {
        "name": "경복궁",
        "lat": 37.579617,
        "lon": 126.977041,
        "subway": "경복궁역(3호선)",
        "summary": "한복 체험, 궁궐 야경, 북촌한옥마을 산책"
    },
    {
        "name": "명동",
        "lat": 37.563757,
        "lon": 126.985302,
        "subway": "명동역(4호선)",
        "summary": "K-뷰티 쇼핑과 길거리 음식"
    },
    {
        "name": "N서울타워",
        "lat": 37.551169,
        "lon": 126.988227,
        "subway": "명동역(4호선)",
        "summary": "서울 야경과 케이블카"
    },
    {
        "name": "홍대거리",
        "lat": 37.556268,
        "lon": 126.922641,
        "subway": "홍대입구역(2호선)",
        "summary": "버스킹, 클럽, 감성 카페"
    },
    {
        "name": "강남",
        "lat": 37.497942,
        "lon": 127.027621,
        "subway": "강남역(2호선)",
        "summary": "쇼핑과 K-pop 핫플"
    },
]

# 기본 설명
info_text = """
📍 관광지를 클릭하면  
🚇 가까운 지하철역과  
🎈 놀거리가 지도 하단에 표시됩니다.
"""

# 세션 상태
if "info_text" not in st.session_state:
    st.session_state.info_text = info_text

# 지도 생성
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11
)

# 마커 추가
for place in places:

    popup_html = f"""
    <b>{place['name']}</b>
    """

    folium.Marker(
        [place["lat"], place["lon"]],
        popup=popup_html,
        tooltip=place["name"]
    ).add_to(m)

# 하단 고정 설명 박스 HTML
bottom_html = f"""
<div style="
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 70%;
    z-index:9999;
    font-size:16px;
    background-color: rgba(0,0,0,0.75);
    color:white;
    padding:15px;
    border-radius:12px;
    text-align:center;
">
{st.session_state.info_text}
</div>
"""

m.get_root().html.add_child(folium.Element(bottom_html))

# 지도 출력
map_data = st_folium(
    m,
    width=1000,
    height=650
)

# 클릭 이벤트 처리
clicked = None

if map_data:
    clicked = map_data.get("last_object_clicked_tooltip")

if clicked:

    for place in places:
        if place["name"] == clicked:

            st.session_state.info_text = f"""
            📍 <b>{place['name']}</b><br>
            🚇 {place['subway']}<br>
            🎈 {place['summary']}
            """

            st.rerun()
