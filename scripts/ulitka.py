from math import ceil
h = int(input())
a = int(input())
b = int(input())

z = ceil((h - a) / (a - b)) + 1

print(z)
 