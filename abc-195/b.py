import math
# 入力
a, b, w = [float(i) for i in input().split(' ')]
w = w * 1000

# 最小
valmin = 0
x = w // b
amari = w - a * x
if amari == 0:
    valmin = x
else:
    if (b - a) > amari:
        valmax = x + 1
    else:
        valmax = x + math.ceil(amari / (b - a))

# 最大
# valmax = 0
# y = w // a
# amari = w - a * y
# if amari == 0:
#     valmin = y
# else:
#     if ()


# 出力
valmin = int(valmin)
valmax = int(valmax)
# if (valmax * valmin) == 0:
#     print('UNSATISFIABLE')
# else:
print(valmax)
