N = int(input())
i = 1

while 1:
    if N > 0:
        if i > N:
            break
    print(i, end=' ')
    i *= 2
