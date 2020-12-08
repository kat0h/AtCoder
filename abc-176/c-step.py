N = int(input())
A = list(map(int, input().split(sep=' ')))

step = [0]
step_sum = 0
for i in range(1, N):
    step.append(max(0, (A[i-1]+step[i-1])-A[i]))
    step_sum += step[i]

print(step_sum)
