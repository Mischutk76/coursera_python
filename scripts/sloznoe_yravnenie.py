a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a == b == 0:
    print('INF')
elif a == 0 and b != 0:
    print('NO')
else:
    x = -b / a
    if c != 0 and x == -d / c:
        print('NO')
    elif x != int(x):
        print('NO')
    else:
        print(int(x))
