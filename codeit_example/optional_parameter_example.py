# 기본값을 설정해 두면, 함수를 호출할 때 꼭 파라미터에 값을 안 넘겨 줘도 된다.
def myself(name, age, nationality="한국"):
    print("내 이름은 %s" % name)
    print("나이는 %d살" % age)
    print("국적은 %s" % nationality)


myself("코드잇", 1, "미국")  # 옵셔널 파라미터를 제공하는 경우
print()
myself("코드잇", 1)  # 옵셔널 파라미터를 제공하지 않는 경우


# 옵셔널 파라미터는 꼭 마지막에 넣을 것!
# 아래와 같이 할 시에는 오류가 나게 된다.
# def myself(name, nationality="한국", age):
def myself(name, age, nationality="한국"):
    print("내 이름은 %s" % name)
    print("나이는 %d살" % age)
    print("국적은 %s" % nationality)


# myself("코드잇", 1)  # 기본값이 설정된 파라미터를 바꾸지 않을 때
print()
# myself("코드잇", "미국", 1)  # 기본값이 설정된 파라미터를 바꾸었을 때
myself("코드잇", 1, "미국")