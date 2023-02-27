# 리스트(list)
numbers = [2, 3, 5, 7, 11, 13]
names = ["일", "이", "삼", "사"]

# 인덱싱(indexing)
# -를 인덱스앞에 붙이면 뒤에서 부터 출력된다.
print(numbers[-5])

#리스트 슬라이싱(list Slicing)
# ':' 을 사용하면 리스트를 자를 수 있다.
print(numbers[0:4])
print(numbers[2:])
new_list =numbers[:3]
print(new_list)

# 리스트의 값을 바꿀 수 있다.
numbers[1] = numbers[5]
numbers[2] = numbers[1] + numbers[4]
print(numbers)

# len함수는 해당 리스트의 길이를 출력해준다.
print(len(numbers))
# append를 하면 ()괄호 안의 숫자를 리스트의 제일 마지막 부분에 추가한다.
numbers.append(5)
numbers.append(8)
print(len(numbers))

# del을 사용하면 해당 리스트의 값을 삭제 후 값은 앞으로 당겨진다.
del numbers[6]
print(numbers)

# insert(넣고싶은 자리, 넣고싶은 값) 을 해주면, 리스트 내에서 원하는 자리에 값을 추가할 수 있다.
# 또한, 값을 추가함과 동시에 해당 값의 뒤에 값들은 한 칸씩 뒤로 밀리게 된다.
numbers.insert(0, 0)
print(numbers)

# 정렬 함수
# sorted(정렬하고싶은 리스트 변수) 는 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트를 리턴한다.
# new_list = sorted(numbers)

# reverse=True를 할 경우 반대로 정렬하게된다.(내림차순)
# new_list = sorted(numbers, reverse=True)
print(new_list)

# sort의 경우, 아무것도 리턴하지 않고 기존 리스트를 정렬하는 기능만 실행한다.
# 때문에, sort를 사용하면 numbers의 리스트 내용이 변경된다.
numbers.sort()

# 이또한 sort(reverse=True)를 사용하면 내림차순정렬이 된다.
print(numbers)

