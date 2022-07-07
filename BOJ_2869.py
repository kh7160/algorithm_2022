import math

a,b,v = map(int, input().split(' '))

v_diff_a = v - a
n = math.ceil(v_diff_a / (a - b))
# print(f'n:{n}, v_diff_a:{v_diff_a}')
print(int(n)+1)