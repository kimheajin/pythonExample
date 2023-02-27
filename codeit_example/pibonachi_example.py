i = 1
num1 = 1
num2 = 1
sum = 0
while i <= 50:
    if i % 2 == 0:
        print(num2)
        num2 += num1
    else:
        print(num1)
        num1 += num2

    i += 1

