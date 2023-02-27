IZA_MONEY = 0.12
tacks_money = 50000000
year = 1989
apartment_2016 = 1100000000
while year <= 2016:
    print(round(tacks_money * IZA_MONEY))
    tacks_money = tacks_money * (1 + IZA_MONEY)
    print(tacks_money)
    year += 1

if apartment_2016 >= tacks_money:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(apartment_2016 - tacks_money))
elif apartment_2016 <= tacks_money:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(tacks_money - apartment_2016)))
