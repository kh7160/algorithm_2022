n, k = map(int, input().split(' '))
coin = []
for i in range(n):
    coin.append(int(input()))

# 파이썬 reverse
# list[::-1] - 리스트, 튜플, 문자열, 딕셔너리X
# reverse() - 리스트, 튜플X, 문자열X, 딕셔너리X, 반환 None
# reversed() - 리스트, 튜플, 문자열, 딕셔너리X, 반환 O (다만 인자로 넘겨준 자료구조가 넘어오는 것은 아님)
coin.reverse()
# print(f'coin.reverse() : {coin}')
result = 0

for num in coin:
    div, mod = divmod(k, num)
    # print(f'div : {div}, mod : {mod}')
    result += div
    k = mod

print(result)