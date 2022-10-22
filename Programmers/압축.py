def solution(msg):
    answer = []
    msg_dict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15,
                'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    msg = list(msg)
    dict_cosnt = 27
    while len(msg) != 0:
        word = ''
        bf_word = ''
        for i in range(len(msg)):
            word += msg[i]
            if word in msg_dict.keys():
                bf_word = word
                if i == len(msg)-1:
                    answer.append(msg_dict[word])
                    msg = []
                continue
            else:
                msg = msg[i:]
                # print(f'msg : {msg}')
                answer.append(msg_dict[bf_word])
                msg_dict[word] = dict_cosnt
                # print(f'msg_dict : {msg_dict}')
                dict_cosnt += 1
                break

    print(answer)
    return answer


if __name__ == '__main__':
    msg = 'KAKAO'
    # msg = 'TOBEORNOTTOBEORTOBEORNOT'
    # msg = 'ABABABABABABABAB'
    solution(msg)