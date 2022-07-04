num = int(input())

result = 1
cnt = 1
while num != 1:
    result += 6 * cnt
    cnt += 1
    if result >= num:
        break

print(cnt)