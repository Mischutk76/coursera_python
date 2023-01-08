n = int(input())
total = 1
n_1 = n
total_2 = 0
while n != 0:
    n = int(input())
    if n == n_1:
        total += 1
    else:
        total = 1
    n_1 = n
    if total_2 < total:
        total_2 = total
print(total_2)
