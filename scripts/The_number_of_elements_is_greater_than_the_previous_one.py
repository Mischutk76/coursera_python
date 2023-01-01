x = int(input())
total = 0
e = x
while x != 0:
    if x > e:
        total += 1
    e = x
    x = int(input())
print(total)
