n, new_n = int(input()), int(input())
max_total, total = 1, 1
while True:
    if n == 0 or new_n == 0:
        break
    while n > new_n:
        total += 1
        n = new_n
        if total > max_total:
            max_total = total
        new_n = int(input())
        if new_n == 0:
            break
    total = 1
    while n < new_n:
        total += 1
        n = new_n
        if total > max_total:
            max_total = total
        new_n = int(input())
        if new_n == 0:
            break
    total = 1
    while n == new_n:
        total = 1
        new_n = int(input())
        if new_n == 0:
            break
print(max_total)
