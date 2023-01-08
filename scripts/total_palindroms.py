n = int(input())
total = 0
for i in range(1, n+1):
    i_string = ''
    for symbol in str(i):
        i_string = symbol + i_string
    if i == int(i_string):
        total += 1
print(total)
