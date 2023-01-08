N = int(input())
i = 1
while N >= i:
    if i == N:
        print('YES')
        break
    i *= 2
if i > N:
    print('NO')
