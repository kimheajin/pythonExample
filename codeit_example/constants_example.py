# 상수 (constant)
PI = 3.14


# 상수를 대문자로 하는 이유는 바로 알아채기 위함.
# 하지만 자바와는 다르게 값을 바꿀 수는 있다.
# 이건 약속의 의미이기때문에 대문자로 쓰인 변수는 상수로 취급하며 값을 바꾸지 않을 것.

# 반지름 받아 원의 넓이 계산
def calculate_area(r):
    return PI * r * r


radius = 4  # 반지름
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))
