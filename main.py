k = int(input())
m = int(input())
n = int(input())
if n <= k:
    min_time = 2 * m
else:
    if n % k == 0:
        min_time = n // k * (2 * m)
    else:
        min_time = 2 * n // k * m + m
print(min_time)
