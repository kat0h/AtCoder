a, b, c, d = [int(i) for i in input().split(" ")]

ans = max([a*c, a*d, b*c, b*d])

print(ans)
