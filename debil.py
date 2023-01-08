n, new_n = int(input()), int(input())
max_total, total = 1, 1
max_number = 0
total_distance = 0
min_distance = None
while True:
    if n == 0 or new_n == 0:
        break
    if new_n > n and max_number < new_n:
        max_number = new_n
    else: total = 1 ##2
    if max_number == n:
        total += 1
        if total >= 2:
            total_distance += 1
        if min_distance is None or total_distance < min_distance:
            min_distance = total_distance
        n = new_n
    new_n = int(input())
    n = new_n
if total >= 2:
    print(total_distance)
else:
    print(0)
