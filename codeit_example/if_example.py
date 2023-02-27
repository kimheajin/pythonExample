i = 1
count = 0
while i <= 120:
    if 120 % i == 0:
        print(i)
        count += 1
    i += 1

print("{}의 약수는 총 {}개입니다.".format(i-1, count))