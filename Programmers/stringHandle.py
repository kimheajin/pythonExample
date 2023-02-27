import re

def solution(s):
    answer = True
    if " ".join(s.split()) == len(s):
        if len(s) == 4 or len(s) == 6 and len(s) >= 0 or len(s) <= 8 and re.match('\d', s) != None:
            answer = True
        else:
            answer = False
    else:
        answer = False

    return answer

# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
# 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

print(solution("4 444"))