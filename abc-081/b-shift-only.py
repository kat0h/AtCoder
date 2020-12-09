_ = int(input())
A = list(map(int, input().split(sep=' ')))
C = []

for i in A:
    c = 0
    while i % 2 == 0:
        i /= 2
        c += 1
    C.append(c)

print(min(C))
