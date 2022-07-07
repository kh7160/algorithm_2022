import math

def search_odd(num):
    if num == 1:
        return False

    # print(f'num : {num}, int(math.sqrt(num)) : {int(math.sqrt(num))}')
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False

    return True

m, n = map(int, input().split(' '))

for i in range(m, n+1):
    if search_odd(i):
        print(i)