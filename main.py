n = int(input())
x, y = 0, 1
if n == 0:
    print(x)
elif n == 1:
    print(y)
else:
    i = 2
    while i <= n:
        x, y = y, x + y
        i += 1
    print(y)
