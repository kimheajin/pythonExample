# split
my_string = "1. 2. 3. 4. 5. 7"
print(my_string.split(". "))

# split은 ()안의 패턴을 기준으로 앞 뒤로 나누는 기능이다.
full_name = "Kim, yuna"
name_date = full_name.split(", ")
first_name = name_date[0]
last_name = name_date[1]
print(first_name, last_name)

# 공백 같은 것들만 지우고 싶을 경우 split()이라고 하면 공백을 기준으로 나눈 값을 return해준다.
# 또한, ""안의 숫자를 split으로 분할하여 저장할 경우 결국 분할된 수도 String형이기에 덧셈을 할 경우 String의 덧셈이 되고만다.
numbers = "    \n\n    2    \t  3    \n 5    11   \n\n".split()
# 그래서 숫자의 덧셈을 하고싶을 경우 int()형으로 형변환을 해주어야 한다.
print(int(numbers[0]) + int(numbers[1]))