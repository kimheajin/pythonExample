# return문은 값을 반환하는 것 뿐만 아니라 함수를 종료하는 역할도 겸하고 있다.

def square(x):
    print("시작")
    return x * x
    print("종료") # <<dead code라고도 한다.


print("이제부른다")
print(square(2) * square(8))
print("불렀다")

# return 문의 이해
# 아래와 같이 하면 결국 return되는 값이 없기 때문에 x * x의 값을 print해 준 뒤
# sqr(5)의 결과값 none을 print해주게 된다.
def sqr(x):
    print(x * x)


print(sqr(5))