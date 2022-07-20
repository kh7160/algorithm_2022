# stack?

def chk_right(u):
    chk = 0

    for ch in u:
        chk += 1 if ch == '(' else -1
        if chk < 0:
            return False

    return True

def solution(p):
    # 1단계
    print('step 1')
    if not p:
        return ''

    # 2단계
    print('step 2')
    first = p[0]
    cnt = 0
    for idx, ch in enumerate(p):
        if ch == first:
            cnt += 1
        else:
            cnt -= 1

        if cnt == 0:
            u = p[:idx+1]
            v = p[idx+1:]
            break
    print(f'u, v : {u, v}')

    # 3단계
    print('step 3')
    if chk_right(u):
        print('chk_right')
        return u + solution(v)

    # 4단계
    print('step 4')
    answer = '('
    s_v = solution(v)
    print(f's_v : {s_v}')
    answer += s_v
    answer += ')'
    u = u[1:len(u)-1]
    print(f'u[1:len(u)-1] : {u}')
    u = ''.join([')' if _ == '(' else '(' for _ in u])
    print(f'u[1:len(u)-1] : {u}')
    answer += u
    print(f'answer : {answer}')
    return answer

if __name__ == '__main__':
    # p = "(()())()"
    # p = ")("
    # p = "()))((()"
    # p = "((((())()))))))((("
    p = "))))((((((()())()))("
    sol_p = solution(p)
    print(sol_p)