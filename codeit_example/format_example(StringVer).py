# 오늘은 2019년 10월 29일 입니다.
year = 2019
month = 10
day = 29

print("오늘은" + str(year) +"년" + str(month) + "월" + str(day) + "일입니다.")

# format 을 사용하면 변수의 숫자를 날짜로 변환
data_string = "오늘은 {}년 {}월 {}일입니다."
print(data_string.format(year, month, day))

# format안에 문자열을 순서대로 입력하면 {}부분에 문자열이 들어간다.
# format안의 문자열을 원하는 대로 넣고 싶으면 {}안에 인덱스를 입력하면 된다.
print("저는 {1}, {0}, {2}를 좋아합니다.".format("박지성","유재석","빌 게이츠"))

num1 = 1
num2 = 3
# f는 소수점을 나타내는 것이며, 2:.2f를 할 시에는 소수점 2째자리까지 출력하게된다.
# 2:.4f 를 하면 4째자리까지 출력하게 된다.
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num1, num2, num1/num2))
print("{0} 나누기 {1}은 {2:.4f}입니다.".format(num1, num2, num1/num2))

# 가장 오래된 방식 (% 기호)
name = "최지웅"
age = 32
# C나 자바 등 많은 언어들에서 이와 유사한 방식으로 문자열 포맷팅을 함
print("제 이름은 %s이고 %d살입니다." % (name, age))

# 현재 가장 많이 쓰는 방식 (format 메소드)
name = "최지웅"
age = 32

print("제 이름은 {}이고 {}살입니다.".format(name, age))

# 새로운 방식 (f-string)
name = "최지웅"
age = 32

# 파이썬 버전 3.6부터 새롭게 나온 방식입니다
print(f"제 이름은 {name}이고 {age}살입니다.")