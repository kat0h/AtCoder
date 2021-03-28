N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = [int(i) for i in input().split(' ')]

res = 1000000000000000000000000000000000000000000000000000000000000000000000000
for i in range(N):
    for j in range(N):
        res = min(res, max(A[i], B[j]) if i!=j else A[i] + B[j])
print(res)
