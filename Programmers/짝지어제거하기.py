# stack 특징 살려서 풀기..

def solution(s):
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        elif stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    return 0 if len(stack) != 0 else 1


if __name__ == '__main__':
    s = 'cdcd'
    print(solution(s))