import time
import pyautogui as pag

# 커서 좌표 확인
# pos = pag.position()
# print(pos)

model_cord = "CN"   # ---------------------조회 희망 차량코드 입력하세요
playtime = 2 # ----------------------------조회 희망 횟수입니다

pag.click(711,1057) #국판 화면 클릭
time.sleep(1) # 화면띄우는 시간 1초지연
pag.click(487,280) # 사양입력창 클릭
pag.hotkey('ctrl','a') # 전체 복사
pag.press('delete')
time.sleep(0.5) # 화면띄우는 시간 0.5초지연
pag.click(487,280) # 사양입력창 재클릭
pag.typewrite(model_cord) # CN(희망차량코드) 입력
pag.press('enter') # 조회
pag.press('tap') # 탭 입력
pag.press('end') # 스크롤 최하단 이동
pag.press('pgdn') # 조회
time.sleep(5) # 화면띄우는 시간 5초지연

salse_list = 0
while salse_list < playtime:
    salse_list = salse_list + 1
    pag.press('end') # 스크롤 최하단 이동
    pag.press('pgdn') # 조회
    time.sleep(5) # 화면띄우는 시간 5초지연