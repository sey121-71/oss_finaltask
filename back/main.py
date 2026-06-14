from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserData(BaseModel):
    action: str
    crisis: str
    physical: str

@app.post("/recommend")
def recommend_position(data: UserData):
    # 빈 공간 침투 성향
    if "빈 공간" in data.action:
        if "과감한 패스" in data.crisis:
            position = "스트라이커 (Striker - ST)"
            desc = "상대 수비 라인을 무너뜨리고 오직 득점에 집중하는 최전방 해결사입니다."
            tip = "오프사이드 라인을 깨는 타이밍과 정교한 슈팅 능력을 기르세요."
        else:
            position = "윙어 (Winger - LW/RW)"
            desc = "빠른 스피드로 측면 공간을 허물고 크로스를 올리거나 안쪽으로 파고드는 크랙입니다."
            tip = "순간적인 가속도와 1대1 돌파 기술을 연마하세요."

    # 패스 및 조율 성향
    elif "위치를 넓게" in data.action:
        if "활동량" in data.physical:
            position = "중앙 미드필더 (Central Midfielder - CM)"
            desc = "공수를 연결하는 그라운드의 사령관입니다. 경기 흐름을 읽고 조율하는 역할을 잘 수행합니다."
            tip = "넓은 시야와 패스 정확도를 기본으로, 공수 전환 속도를 높이세요."
        else:
            position = "공격형 미드필더 (Attacking Midfielder - CAM)"
            desc = "창의적인 패스로 어시스트를 하는 플레이메이커입니다."
            tip = "상대 압박 속에서도 볼을 소유하는 탈압박 능력을 키우세요."

    # 수비 및 마크 성향
    else:
        if "활동량" in data.physical:
            position = "수비형 미드필더 (Defensive Midfielder - CDM)"
            desc = "수비수 앞을 지키는 든든한 방패입니다. 끊임없는 활동량으로 상대 공격을 1차 저지합니다."
            tip = "패스 길목을 차단하는 위치 선정과 가로채기 능력을 발전시키세요."
        else:
            position = "중앙 수비수 (Center Back - CB)"
            desc = "최후방에서 실점을 막아내는 수비수입니다. 거친 몸싸움을 마다하지 않는 강력한 피지컬을 가지고 있습니다."
            tip = "수비 라인을 지휘하는 조율력과 공중볼 경합 능력을 기르세요."

    return {"position": position, "description": desc, "tip": tip}