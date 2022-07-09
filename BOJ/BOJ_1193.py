num = int(input())

direction = True
add = 1
tot = 0
while True:

    tot += add
    if tot >= num:
        # print(f'tot : {tot}, add : {add}, direction : {direction}')
        break

    add += 1
    direction = not direction

start = tot - add + 1
if direction:
    a, b = add, 1
else:
    a, b = 1, add

for i in range(start, num):
    if direction:
        a, b = a - 1, b + 1
    else:
        a, b = a + 1, b - 1

print(f'{a}/{b}')