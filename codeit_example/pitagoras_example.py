# 피타고라스의 정의는 a제곱과 b제곱의 값이 c제곱의 값고 같아야 한다.
# 또한, a는 b보다 작으며 b는 c보다 작아야 한다.

for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 - a - b
        if a * a + b * b == c * c and a < b < c:
            print(a * b * c)
