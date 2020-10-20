n, x, t = [int(i) for i in input().split(" ")]

if (n % x) == 0:
    ans = (n // x)*t
else:
    ans = (n // x+1)*t

print(ans)
