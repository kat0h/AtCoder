import math
_ = input()
x = [abs(float(i)) for i in input().split(" ")]

m = 0.0
for i in x:
    m = i + m

y = 0.0
for i in x:
    y = i**2 + y
y = math.sqrt(y)

c = max(x)

print(m)
print(y)
print(c)
