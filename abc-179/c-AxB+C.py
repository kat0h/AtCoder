N = int(input())
counter = 0

for i in range(1, N+1):
    for j in range(1, (N-1)//i+1):
        counter += 1

print(counter)
