# 자리수 합 리턴
def sum_digit(num):
    # 코드를 입력하세요.
    sum_return = 0
    str_num = str(num)
    for digit in str_num:
        sum_return += int(digit)

    return sum_return


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
digit_total = 0
for num in range(1, 1000):
    digit_total += sum_digit(num)

print(digit_total)