with open('vocabulary.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        right_answer = line.strip().split(": ")
        en_word, kr_word = right_answer[0], right_answer[1]
        check_answer = input('{}: '.format(kr_word))

        if check_answer == en_word:
            print('맞았습니다!')
        else:
            print('아쉽습니다. 정답은 {}입니다.'.format(en_word))
