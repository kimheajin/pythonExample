def is_palindrome(word):

    bool_return = False
    for wd in range(round(len(word)/2)):
        bool_return = word[wd] == word[-wd-1]

    return bool_return

    # 모범 답안
    # for left in range(len(word) // 2):
    #     # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
    #     right = len(word) - left - 1
    #     if word[left] != word[right]:
    #         return False
    #
    #     # for문에서 나왔다면 모든 쌍이 일치
    # return True


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))