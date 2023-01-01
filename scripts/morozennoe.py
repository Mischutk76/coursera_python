k = int(input())

if k >= 3:
    for i in range(k // 5 + 1):
        if (k - 5 * i) % 3 == 0:
            print('Yes')
        else:
            print('NO')
else:
    print('NO')
