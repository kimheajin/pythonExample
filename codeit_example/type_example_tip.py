# 아래와 같은 형식으로 type(형을 보고싶은 데이터)를 하면 어떤 형의 데이터인지 볼 수 있다.
print(type(3))
print(type(3.0))
print(type("3"))


def hello():
    print("Hello world")


print(type(hello)) # function
print(type(print)) # builtin_function_or_method 여기서 builtin은 내장함수라는 의미
