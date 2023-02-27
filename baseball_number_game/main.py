from random import randint


# 무작위로 0과 9 사이의 서로 다른 숫자 3개를 뽑고, 그 숫자들이 담긴 리스트를 리턴
def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        random_num = randint(0, 9)
        if random_num not in numbers:
            numbers.append(random_num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    while len(new_guess) < 3:

        user_input = input("{}번째 숫자를 입력하세요: ".format(len(new_guess) + 1))

        if user_input != '':
            if int(user_input) <= 10 or int(user_input) >= 0:
                if int(user_input) not in new_guess:
                    new_guess.append(int(user_input))
                else:
                    print("중복되는 숫자입니다. 다시 입력하세요.")
            else:
                print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        else:
            print("공백이 입력되었습니다. 숫자를 입력해주세요.")

    return new_guess


def get_score(guess, solution):

    strike_count = 0
    ball_count = 0
    for use_num in guess:
        if use_num == solution[guess.index(use_num)]:
            strike_count += 1
        elif use_num in solution:
            ball_count += 1

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:
    USER_NUMBER = take_guess()
    stk, ball = get_score(USER_NUMBER, ANSWER)

    print("{}S {}B".format(stk, ball))
    tries += 1

    if stk == 3:
        break


print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
