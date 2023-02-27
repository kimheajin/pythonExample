import random

rg_answer = random.randint(1, 20)
NUM_COUNT = 4
use_answer = 0

# for 문을 사용할 경우 20이상의 수가 들어와도 OK된다.
# 때문에 이 문제는 while문이 더 적절한것 같다.

# for num in range(4):
#     use_answer = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞춰보세요:".format(4 - num)))
#     print(use_answer)
#     if use_answer == rg_answer:
#         print("축하합니다. {}번 만에 숫자를 맞추셨습니다.".format(num+1))
#     else:
#         if num == 3:
#             print("아쉽습니다. 정답은 {}였습니다.".format(rg_answer))
#         elif use_answer < rg_answer:
#             print("Up")
#         elif use_answer > rg_answer:
#             print("Down")

input_count = 0
while NUM_COUNT > input_count and rg_answer != use_answer:

    use_answer = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞춰보세요:".format(NUM_COUNT - input_count)))
    if use_answer < rg_answer:
        print("Up")
    elif use_answer > rg_answer:
        print("Down")
    input_count += 1

if rg_answer == use_answer:
    print("축하합니다. {}번 만에 숫자를 맞추셨습니다.".format(input_count))
else:
    print("아쉽습니다. 정답은 {}였습니다.".format(rg_answer))