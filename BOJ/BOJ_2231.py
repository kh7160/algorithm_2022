n = int(input())
answer = []

for i in range(n+1):
    if n == i + sum(list(map(int, list(str(i))))):
        answer.append(i)
        break

print(0 if not answer else answer[0])