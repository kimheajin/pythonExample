# 기본적인 import방식 + 이름붙여서 부르는 방식
# import calculator as calc

# 2번째 방법
# 이 방법을 사용하면 아래에서 호출 할 때 calculator을 쓸 필요 없이
# add(a, b) , multiply(a, b)로 해도 해당 기능을 사용할 수 있게 해준다.

from calculator import add, multiply

# print(calc.add(2, 5))
# print(calc.multiply(2, 5))
print(add(2, 5))
print(multiply(2, 5))