def insertion_sort(ist_sort):
    # 배열 위치
    list_count = 1

    # 배열의 크기만큼 반복
    while list_count < len(ist_sort):
        # 현 지점의 비교할 배열의 값을 diff에 저장
        diff = ist_sort[list_count]
        little_count = list_count
        while little_count != 0:

            # 저장한 값과 이전 배열의 값을 비교
            # True인 경우는 이전 배열의 값이 diff보다 클 경우이다.
            # 클 경우엔 diff의 값을 이전 배열에다가 저장하고, 이전 배열의 값은 diff위치에 넣음.
            if ist_sort[little_count-1] > diff:
                save_value = ist_sort[little_count-1]
                ist_sort[little_count-1] = diff
                ist_sort[little_count] = save_value
            little_count -= 1
        list_count += 1
    return ist_sort


print(insertion_sort([4, 2, 7, 1, 9, 3]))