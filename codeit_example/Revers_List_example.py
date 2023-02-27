numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
# save_num = []
for num in range(len(numbers)):
#     save_num.append(numbers[int(len(numbers)-num)-1])
#     print(save_num)
    right = len(numbers) - num - 1
    numbers[right], numbers[num] = numbers[num], numbers[right]


# numbers = save_num
print("뒤집어진 리스트: " + str(numbers))