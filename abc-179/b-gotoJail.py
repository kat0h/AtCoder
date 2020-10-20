i = int(input())

ans = "No"
zoro = 0
for j in range(i):
    inp = [int(k) for k in input().split(" ")]
    if inp[0] == inp[1]:
        zoro += 1
    else:
        zoro = 0
    if zoro >= 3:
        ans = "Yes"
print(ans)
