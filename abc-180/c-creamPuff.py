N = int(input())

a, b, i = [], [], 1
endstatus = 1
while endstatus:
    if (N % i) == 0:
        a.append(i)
        b.append(N//i)
    i += 1
    if (i*i) > N:
        endstatus = 0

ans = a+b[::-1]
ans = sorted(set(ans), key=ans.index)
for j in ans:
    print(j)
