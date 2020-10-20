S = input()

ans, j = 0, 0
for i in S:
    if i == "R":
        j += 1
    else:
        j = 0
        ans = max(j, ans)

print(ans)
