n, m = map(int, input().split(' '))
lst = [_+1 for _ in range(n)]
answer = []


def backtrack(step):
    if step == m:
        print(*answer)
        return

    for i in lst:
        if i not in answer:
            answer.append(i)
            backtrack(step+1)
            answer.pop()


backtrack(0)