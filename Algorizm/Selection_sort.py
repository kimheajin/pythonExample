def selection_sort(shake_list):

    count = 0
    while len(shake_list) > count:

        num_min = shake_list[count]
        for num in range(count, len(shake_list)):

            if num_min > shake_list[num]:
                save_small = shake_list[num]
                shake_list[num] = num_min
                shake_list[count] = save_small
                num_min = save_small

        count += 1

    return shake_list


print(selection_sort([3, 5, 1, 2, 4]))