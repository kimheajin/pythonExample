# Type
# 파라미터의 데이터 타입이 리턴됩니다.
# 시간 복잡도는 O(1)입니다.
print(type([7, 5, 2, 3, 6])) # => <class 'list'>
print(type(5))               # => <class 'int'>
print(type(3.14))            # => <class 'float'>
print(type(True))            # => <class 'bool'>
print(type("True"))          # => <class 'str'>

# max, min
# max : 파라미터 중 가장 큰 값이 리턴
# min : 파라미터 중 가장 작은 값이 리턴
# 파라미터의 개수를 n이라고 볼 때, max 함수와 min 함수의 시간 복잡도는 O(n)입니다.
print(max(2, 5))             # => 5
print(max(2, 7, 5))          # => 7
print(min(2, 5))             # => 2
print(min(2, 7, 5, 11, 6))   # => 2

# str
# 숫자를 문자열로 바꿀 수 있습니다.
# 파라미터를 n이라고 하고 n의 자릿수를 d라고 함
# str 함수의 시간 복잡도는 O(log n) 으로 나타낼 수도 있고 O(d)로 나타낼 수도 있습니다.
my_str = str(257138)
print(my_str)                # => 257138
print(type(my_str))          # => <class 'str'>

# append, insert, del, index, reverse
# append : 리스트 끝에 새로운 값이 추가됩니다. 시간 복잡도는 O(1)입니다.
# insert, del, index, reverse : 모두 O(n)입니다.

my_list = [7, 5, 2, 3, 6]

my_list.append(9)            # 끝에 9 추가
print(my_list)               # => [7, 5, 2, 3, 6, 9]

my_list.insert(2, 11)        # 2번 인덱스에 11 추가
print(my_list)               # => [7, 5, 11, 2, 3, 6, 9]

del my_list[2]               # 2번 인덱스 값 삭제
print(my_list)               # => [7, 5, 2, 3, 6, 9]

my_index = my_list.index(9)  # 리스트에서 9의 인덱스
print(my_index)              # => 5

my_list.reverse()            # 리스트 뒤집기
print(my_list)               # => [9, 6, 3, 2, 5, 7]

# sort, sorted
# sorted : 정렬된 새로운 리스트가 리턴
# sort : 그 리스트 자체를 정렬시켜 준다
# 두 메소드의 시간 복잡도는 모두 O(nlg n)입니다.
my_list = [7, 5, 2, 3, 6]

print(sorted(my_list))       # => [2, 3, 5, 6, 7]
print(my_list)               # => [7, 5, 2, 3, 6]

my_list.sort()
print(my_list)               # => [2, 3, 5, 6, 7]

# slicing
# 리스트 슬라이싱을 하면 리스트의 일부를 받아 올 수 있습니다.
# 리스트 슬라이싱의 시간 복잡도는 슬라이싱의 범위 길이에 비례합니다.
# my_list[a:b]를 하면 시간 복잡도는 O(b−a)입니다.
my_list = [7, 5, 2, 3, 6]

print(my_list[1:4])          # => [5, 2, 3]
print(my_list[:4])           # => [7, 5, 2, 3]
print(my_list[1:])           # => [5, 2, 3, 6]
print(my_list[:])            # => [7, 5, 2, 3, 6]
print(my_list[::2])          # => [7, 2, 6]


# len
# 리스트, 사전, 문자열 등의 길이가 리턴됩니다.
# 시간 복잡도는 O(1)입니다.
my_list = [7, 5, 2, 3, 6]
my_dict = {'a': 2, 'b': 3, 'c': 5, 'd': 7}
my_string = 'hello world'

print(len(my_list))          # => 5
print(len(my_dict))          # => 4
print(len(my_string))        # => 11
