# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    str_number = str(n)

    # base_case : n의 자리수가 1개만 있을 경우
    if n < 10:
        return n
    # return sum_digits(n % (10**(len(str_number)-1))) + int(str_number[1:])
    # return n % 10 + sum_digits(n // 10)
    return sum_digits(n % (10**(len(str_number)-1)))


# 테스트
# print(sum_digits(22541))
# print(sum_digits(92130))
print(sum_digits(12634))
# print(sum_digits(704))
# print(sum_digits(3755))
