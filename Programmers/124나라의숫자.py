def solution(n):
    answer = ''
    div = n
    while div != 0:
        div, mod = divmod(div, 3)
        if mod == 0:
            div, mod = div - 1, 4
        answer += str(mod)

    return answer[::-1]

if __name__ == '__main__':
    n = 16
    print(solution(n))