def is_evenly_divisible(number):
    # if (number % 2) == 0:
    # else:
    # return False
    return (number % 2) == 0


# 테스트
print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(218))
print(is_evenly_divisible(317))


i = 100

while i >= 100 & i % 23 != 0:
    print(i)
    i += 1


print(i)
