a = int(input())
b = int(input())
res_a = 0**(b // a)
res_b = 0**(a // b)
res_draw = (a // b) * (b // a)
res = a * res_a + b * res_b + res_draw * a
print(res)
