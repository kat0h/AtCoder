N = int(input())
A = [int(i) for i in input().split(" ")]

s = 0
for i in range(1, N):
    for j in range(0, i):
        s += (A[i] - A[j])**2

print(s)
