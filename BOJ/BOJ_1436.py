n = int(input())
cnt = 1
num = 666
while True:
    if cnt == n:
        break

    num += 1
    if str(num).find('666') != -1:
        cnt += 1

print(num)