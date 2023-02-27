with open('data/chicken.txt', 'r', encoding='UTF-8') as f:
    number_sum = 0
    day_count = 0
    for read in f:
        month_12_money = read.strip().split(": ")
        number_sum += int(month_12_money[1])
        day_count += 1

    print(number_sum / day_count)
