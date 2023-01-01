N = int(input())
h = N // 3600 % 24
m = str(N // 60 % 60 // 10) + str(N // 60 % 60 % 10)
s = str(N % 60 // 10) + str(N % 60 % 10)
print(h, ':', m, ':', s, sep='')
