class User:
    def say_hello(some_user):
        print("HI, I'M {}".format(some_user))


user1 = User()
user2 = User()
user3 = User()

user1.name = "김대위"
user1.email = "captaion@codeit.kr"
user1.password = "12345"

user2.name = "강영훈"
user2.email = "gangyonhun@codeit.kr"
user2.password = "12345"

user3.name = "최지웅"
user3.email = "jiwong@codeit.kr"
user3.password = "12345"

print(user1.email)
print(user2.password)

User.say_hello(user1.name)
User.say_hello(user2.name)
User.say_hello(user3.name)