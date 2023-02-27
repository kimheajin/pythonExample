# with open하여 오픈할 파일은 항상 위에다가 해주는 것이 좋다.
# -> while문 같은 반복문 안에 위치한다면 계속해서 open하기 때문에 데이터가 많이 사용되게 된다.
with open("vocabulary.txt", "a", encoding="UTF-8") as f:
    while True:
        english_word = input("영어 단어를 입력하세요: ")
        if english_word == "q":
            break

        korean_word = input("한국어 뜻을 입력하세요: ")
        # else:
        #     korean_word = input("한국어 뜻을 입력하세요: ")
        #     if english_word != "" and korean_word != "":
        #         f.write(english_word + ": ")
        #         f.write(korean_word + "\n")
        if korean_word == "q":
            break

        if english_word != "" and korean_word != "":
            f.write("{}: {}\n".format(english_word, korean_word))
