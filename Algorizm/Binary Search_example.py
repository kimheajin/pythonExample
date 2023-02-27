def binary_search(element, some_list):
    count = 0
    for some in some_list:
        count += 1

    bigyo = round((0 + count) / 2)
    c = 0
    while count > c:

        if some_list[bigyo] == element:
            return bigyo

        if some_list[bigyo] > element:
            bigyo = round(0 + bigyo / 2)

        else:
            bigyo = round(bigyo + count / 2)
        c += 1


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
