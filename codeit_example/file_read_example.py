with open('codeit_example/data/chicken.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(line.strip())

# strip()을 사용하면 앞과 뒤의 띄워쓰기, 개행을 모두 지울 수있다.