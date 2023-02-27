def is_palindrome(word):
    count = 0
    save_word = ""
    for wd in range(len(word)):
        save_word += word[len(word)-wd-1]
        count += 1

    return word == save_word


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))