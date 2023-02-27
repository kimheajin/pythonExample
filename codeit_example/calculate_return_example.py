def calculate_change(payment, cost):
    # calcul_box = payment - cost
    # fifty_manwon = 50000
    # manwon = 10000
    # fifty_chunwon = 5000
    # chunwon = 1000

    # print("{}원 지폐: {}장".format(fifty_manwon, int(calcul_box / fifty_manwon)))
    # calcul_box = calcul_box - fifty_manwon*int(calcul_box / fifty_manwon)
    #
    # print("{}원 지폐: {}장".format(manwon, int(calcul_box / manwon)))
    # calcul_box = calcul_box - manwon*int(calcul_box / manwon)
    # print("{}원 지폐: {}장".format(fifty_chunwon, int(calcul_box / fifty_chunwon)))
    # calcul_box = calcul_box - fifty_chunwon * int(calcul_box / fifty_chunwon)
    # print("{}원 지폐: {}장".format(chunwon, int(calcul_box / chunwon)))

    change = payment - cost  # 거스름돈 총액

    fifty_count = change // 50000  # 50,000원 지폐
    ten_count = (change % 50000) // 10000  # 10,000원 지폐
    five_count = (change % 10000) // 5000  # 5,000원 지폐
    one_count = (change % 5000) // 1000  # 1,000원 지폐

    # 답 출력
    print("50000원 지폐: {}장".format(fifty_count))
    print("10000원 지폐: {}장".format(ten_count))
    print("5000원 지폐: {}장".format(five_count))
    print("1000원 지폐: {}장".format(one_count))


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)