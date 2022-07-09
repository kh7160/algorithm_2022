def solution(s):
    answer = 999999999

    for i in range(1,len(s)+1):
        j = 0
        cnt = 1
        result = ''
        # print(f'step : {i}')
        while True:
            # print(s[j:j+i])
            if j-i >= 0 and s[j-i:j] == s[j:j+i]:
                # print(f's[j-i:j], s[j:j+i] = {s[j-i:j]}, {s[j:j+i]}')
                cnt += 1
            else:
                result += (str(cnt) + s[j-i:j]) if cnt != 1 else s[j-i:j]
                cnt = 1

            j = j+i
            if j >= len(s):
                result += (str(cnt) + s[j-i:j]) if cnt != 1 else s[j-i:j]
                break

        # print(f'result : {result}')
        answer = min(answer, len(result))

    print(answer)
    return answer

if __name__ == '__main__':
    s = "aabbaccc" # 2a2ba3c
    # s = "ababcdcdababcdcd"
    # s = "abcabcdede"
    # s = "abcabcabcabcdededededede"
    # s = "xababcdcdababcdcd"
    solution(s)