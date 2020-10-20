S = input()

ans, j = 0, 0
for i in S:
    if i == "R":
        j += 1
    else:
        ans = max(j, ans)

print(ans)
