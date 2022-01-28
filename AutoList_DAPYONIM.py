import time
import pyautogui as pag

###########                 사용설명
#                     Visual Studio Code를 우클릭해서 관리자권한 실행해주세요
#                     밑에 있는 model_code, playtime, time_delay만 조작하시면되세요 변경 후에는 컨트롤 + S 꼭 해주세요.
model_code = "CN"   # ---------------------조회 희망 차량코드 입력하세요
playtime = 2 # ----------------------------조회 희망 횟수입니다
time_delay = 8 # ----------------------------조회시 입력되는 시간이에요. 아침에는 10~13초 그 외에는 5~8초 권장드립니다.


pag.click(71,1186) #국판 화면 클릭
time.sleep(0.5) # 화면띄우는 시간 0.5초지연
pag.click(581,392) # 사양입력창 클릭
pag.hotkey('ctrl','a') # 전체 복사
pag.press('delete')
time.sleep(0.5) # 화면띄우는 시간 0.5초지연
pag.click(581,392) # 사양입력창 재클릭
pag.typewrite(model_code) # CN(희망차량코드) 입력
pag.press('enter') # 조회
time.sleep(time_delay) # 화면띄우는 시간
pag.press('tap') # 탭 입력
pag.press('end') # 스크롤 최하단 이동
pag.press('pgdn') # 조회
time.sleep(time_delay) # 화면띄우는 시간

salse_list = 1
while salse_list < playtime:
    salse_list = salse_list + 1
    pag.press('end') # 스크롤 최하단 이동
    pag.press('pgdn') # 조회
    time.sleep(time_delay) # 화면띄우는 시간 5초지연

pag.click(1442,450)
# time.sleep(30) # 엑셀추출 시간
# pag.hotkey('alt','F4') # 엑셀 닫기