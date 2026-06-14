import streamlit as st
import requests

st.set_page_config(page_title="풋볼 파인더", layout="centered")

st.title("나만의 축구 포지션 매칭 테스트")
st.write("실전 경기 상황에서의 행동 성향을 분석하여 당신에게 가장 적합한 축구 포지션을 찾아냅니다.")
st.markdown("---")

st.subheader("경기 상황 문항")

action = st.radio(
    "1. 경기 중 그라운드 위에서 당신이 가장 자주 취하는 '본능적인 행동'은?",
    [
        "상대 수비 빈 공간을 찾아 계속 파고들거나 전방으로 뛰어나간다.",
        "우리 팀 선수들의 위치를 넓게 살피며 패스 줄 곳을 찾는다.",
        "상대 팀에서 가장 위협적인 선수가 누구인지 먼저 확인하고 마크한다."
    ]
)

crisis = st.radio(
    "2. 경기 중 우리 팀이 위기에 처했을 때, 당신이 생각하는 최선의 해결책은?",
    [
        "리스크를 감수하더라도 과감한 패스나 돌파로 분위기를 반전시킨다.",
        "실점하지 않도록 내 위치를 고수하며 동료들과 협력 수비를 한다."
    ]
)

physical = st.selectbox(
    "3. 본인의 피지컬/신체 능력 중 가장 강점이라고 생각하는 부분은?",
    [
        "90분 내내 지치지 않고 경기장 전역을 뛰어다닐 수 있는 활동량",
        "순간적인 가속도와 방향 전환, 혹은 상대와의 거친 몸싸움을 버티는 힘"
    ]
)

st.markdown("---")

if st.button("내 최적 포지션 확인하기", use_container_width=True):
   
    BACKEND_URL = "http://localhost:8000/recommend"
    
    payload = {"action": action, "crisis": crisis, "physical": physical}
    
    with st.spinner("플레이 스타일 데이터 연산 중... "):
        try:
            response = requests.post(BACKEND_URL, json=payload, timeout=5)
            if response.status_code == 200:
                result = response.json()
                st.balloons()
                st.success("매칭 완료!")
                st.subheader(f"추천 포지션: **{result['position']}**")
                st.info(f" **포지션 역할 설명:**\n{result['description']}")
                st.warning(f"**핵심 훈련 팁:** {result['tip']}")
            else:
                st.error("서버 에러가 발생했습니다.")
        except requests.exceptions.ConnectionError:
            st.error("백엔드 서버에 연결할 수 없습니다.")
