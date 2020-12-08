N = int(input())
A = [int(i) for i in input().split(sep=' ')]

cusum = [0]
for i in range(N):
    cusum.append(cusum[i] + A[i])

result = 0
for i in range(1, N):
    result += A[i-1] * (cusum[N]-cusum[i])

print(result % (10**9+7))
