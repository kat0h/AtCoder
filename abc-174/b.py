import math

n, d = [int(i) for i in input().split(' ')]

x = [0]*n
y = [0]*n
for i in range(n):
    x[i], y[i] = [int(j) for j in input().split(' ')]

distance = [math.sqrt(x[i]**2+y[i]**2) for i in range(n)]

ret = sum(i <= d for i in distance)
print(ret)
