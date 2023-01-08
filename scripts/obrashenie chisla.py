a = int(input())
a_reversed = 0
digit = 1
last_digit = 0

while a >= 10:
    last_digit = a % 10
    a_reversed += last_digit * digit
    digit *= 10
    a = a // 10

a_reversed += last_digit * digit

print(a_reversed)
