# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    # list의 길이
    save_list = some_list[1:]

    if len(save_list) == 1:
        return save_list[0]

    return flip(save_list)


# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)