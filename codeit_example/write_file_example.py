# 덮어 쓸 경우
# with open("new_file.txt", "w", encoding="UTF-8") as f:
# 기존의 파일에 추가하는 경우
# (참고: a는 기존 파일이 있으면 그곳에 추가를 하는것이며, 기존 파일이 없다면 새로운 파일을 만들어 그곳에 추가를 하는 것이다.)
with open("new_file.txt", "a", encoding="UTF-8") as f:

    f.write("Hello\n")
    f.write("World\n")
