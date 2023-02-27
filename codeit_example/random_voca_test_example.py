import random as rd

all_line = {}
with open("vocabulary.txt", "r", encoding="UTF-8") as f:

    for line in f:
        all_line.append(line.strip())
        # data = line.strip().split(": ")
        # en_word, kr_word = data[0], data[1]
        # all_line[en_word] = kr_word

    while True:
        random_ptn = rd.randint(1, int(len(all_line)))
        word = all_line[random_ptn-1].split(": ")
        en_word, kr_word = word[0], word[1]

        # keys = list(all_line.keys())
        # index = rd.randint(0, len(keys)-1)
        # en_word = keys[index]
        # kr_word = all_line[en_word]

        check_answer = input('{}: '.format(kr_word))
        if check_answer == "q":
            break

        elif check_answer == en_word:
            print('맞았습니다!')
        else:
            print('아쉽습니다. 정답은 {}입니다.'.format(en_word))
