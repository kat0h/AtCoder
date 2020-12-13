N, M, T = list(map(int, input().split()))

A = []
B = []
for i in range(M):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

n = N

n = n - A[0]
flag = (n > 0)
n = min(n + (B[0] - A[0]), N)

for i in (range(1, M)):
    if not (flag):
        break
    n = n - (A[i] - B[i-1])
    flag = (n > 0)
    n = min(n + (B[i] - A[i]), N)

if (flag):
    n = n - (T - B[M-1])
    flag = (n > 0)

if (flag):
    print("Yes")
else:
    print("No")
