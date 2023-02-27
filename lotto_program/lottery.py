from random import randint


# 함수 정의 : 참가자의 번호를 뽑는 데에도 쓰이고, 보너스를 포함한 당첨 번호 7개를 뽑는 데에도 쓰입니다.
def generate_numbers(n):
    # 무작위로 1과 45 사이의 서로 다른 번호 n개를 뽑는 부분
    # 참가자 전용 번호 혹은 로또 번호가 저장되는 리스트
    save_number = []
    while n > len(save_number):
        random_number = randint(1, 45)
        # 랜덤으로 뽑히는 값이 중복 되는 경우가 있는가 check한 후 list안에 넣기
        if random_number not in save_number:
            save_number.append(random_number)

    return save_number


# 함수 정의 : 일반 당첨 번호 6개와 보너스 번호 1개가 포함된 리스트를 리턴
# 조건 :  일반 당첨 번호 6개는 정렬되어 있어야 하고, 보너스 번호는 마지막에 추가하면 됩니다.
def draw_winning_numbers():
    # lotto_numbers = generate_numbers(6)
    lotto_numbers = generate_numbers(7)
    # lotto_numbers.sort()
    #
    # while len(lotto_numbers) < 7:
    #     # 보너스 번호
    #     random_number = randint(1, 45)
    #     if random_number not in lotto_numbers:
    #         lotto_numbers.append(random_number)

    return sorted(lotto_numbers[:6]) + lotto_numbers[6:]


# 리스트 list_1과 리스트 list_2를 받고, 두 리스트 사이에 겹치는 번호 개수를 리턴합니다.
# def count_matching_numbers(list_1, list_2):
#     if len(list_1) > len(list_2):
#         big_list, sm_list = list_1, list_2
#     else:
#         big_list, sm_list = list_2, list_1
#
#     # 파라미터로 받은 두 리스트에서 총 몇 개의 번호가 겹치는지 세는 용도
#     count = 0
#     loop_ct = 0
#     while len(sm_list) > loop_ct:
#
#         if int(sm_list[loop_ct]) in big_list:
#             count += 1
#
#         loop_ct += 1
#
#     return count

# 리스트 list_1과 리스트 list_2를 받고, 두 리스트 사이에 겹치는 번호 개수를 리턴합니다.
def count_matching_numbers(list_1, list_2):
    # 파라미터로 받은 두 리스트에서 총 몇 개의 번호가 겹치는지 세는 용도
    count = 0
    # list_1의 각 원소를 보는 것
    for num in list_1:
        # 현재 보고 있는 원소인 num이 list_2에 있는지 확인하는 것
        if num in list_2:
            count = count + 1

    return count


def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_ct = count_matching_numbers(numbers, winning_numbers[6:])
    # if winning_numbers[6] in numbers:
    #     bonus_ct = 1

    if 3 == count:
        return 5000
    elif 4 == count:
        return 50000
    elif 5 == count and 1 == bonus_ct:
        return 50000000
    elif 5 == count:
        return 1000000
    elif 6 == count:
        return 1000000000
    else:
        return 0