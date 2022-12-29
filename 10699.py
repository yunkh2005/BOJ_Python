from datetime import datetime

datetime.today()            # 현재 날짜 가져오기
datetime.today().year        # 현재 연도 가져오기
datetime.today().month      # 현재 월 가져오기
datetime.today().day        # 현재 일 가져오기

print(datetime.today().strftime("%Y-%m-%d"))