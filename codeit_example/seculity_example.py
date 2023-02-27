def mask_security_number(security_number):

    # 내가 한 방법
    # if security_number[6] == "-":
    #     save_list = security_number[:10]
    # else:
    #     save_list = security_number[:9]
    #
    # return save_list + "****"

    # 답안 1
    # num_list = list(security_number)
    # for i in range(len(num_list) - 4, len(num_list)):
    #     num_list[i] = '*'
    # return ''.join(num_list)

    # 답안 2
    return security_number[:-4] + '****'


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))