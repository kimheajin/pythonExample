# randint : 두 수 사이의 어떤 랜덤한 정수를 리턴하는 함수
# randint(a, b)를 하면, a ≤ N ≤ b를 만족하는 어떤 랜덤한 정수 N을 리턴

import random

print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))

# uniform : 두 수 사이의 랜덤한 소수를 리턴하는 함수
# randint와 다른 것은 리턴하는 값이 정수가 아니라 소수
# uniform(a, b)를 하면, a ≤ N ≤ b를 만족하는 어떤
# 랜덤한 소수 N을 리턴하는 것

# import random

print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))

# datetime :  '날짜'와 '시간'을 다루기 위한 다양한 '클래스'가 존재

# datetime 값 생성
import datetime

pi_day = datetime.datetime(2020, 3, 14)
# 이렇게 적으면 시간도 직접 설정 가능
# pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)
print(type(pi_day))

# '지금 이 순간'의 날짜와 시간을 받을 때
today = datetime.datetime.now()
print(today)
print(type(today))

# datetime 값 사이의 기간을 알고 싶으면 뺄셈하듯 빼라
today = datetime.datetime.now()
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(today - pi_day)
print(type(today - pi_day))
# 두 datetime 값을 빼면, <class 'datetime.timedelta'>라는 타입이 나온다
# 이건 날짜 간의 차이를 나타내는 타입이라고 생각하면 됨

# 반대로 timedelta를 생성해서 datetime 값에 더해 주는 것도 가능
today = datetime.datetime.now()
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)

print(today)
print(today + my_timedelta)

# datetime 해부하기
# datetime 값에서 '연도'나 '월' 같은 값들을 추출

today = datetime.datetime.now()

print(today)
print(today.year)  # 연도
print(today.month)  # 월
print(today.day)  # 일
print(today.hour)  # 시
print(today.minute)  # 분
print(today.second)  # 초
print(today.microsecond)  # 마이크로초

# datetime 포맷팅
# strftime을 사용하면, 맘대로 바꿀 수 있다

today = datetime.datetime.now()

print(today)
print(today.strftime("%A, %B %dth %Y"))

# 포맷 코드	설명      	예시
# %a	요일 (짧은 버전)	Mon
# %A	요일 (풀 버전)	Monday
# %w	요일 (숫자 버전, 0~6, 0이 일요일)	5
# %d	일 (01~31)	23
# %b	월 (짧은 버전)	Nov
# %B	월 (풀 버전)	November
# %m	월 (숫자 버전, 01~12)	10
# %y	연도 (짧은 버전)	16
# %Y	연도 (풀 버전)	2016
# %H	시간 (00~23)	14
# %I	시간 (00~12)	10
# %p	AM/PM	AM
# %M	분 (00~59)	34
# %S	초 (00~59)	12
# %f	마이크로초 (000000~999999)	413215
# %Z	표준시간대	PST
# %j	1년 중 며칠째인지 (001~366)	162
# %U	1년 중 몇 주째인지 (00~53, 일요일이 한 주의 시작이라고 가정)	35
# %W	1년 중 몇 주째인지 (00~53, 월요일이 한 주의 시작이라고 가정)	35
