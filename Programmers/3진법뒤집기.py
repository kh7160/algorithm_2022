import math


def solution(n):
    answer = 0
    third_num = ''

    while True:
        div, mod = divmod(n, 3)
        third_num += str(mod)
        n = div

        if n < 3:
            if div != 0:
                third_num += str(div)
            break

    final_third = list(third_num)
    final_third.reverse()
    final_third_dict = {_:final_third[_] for _ in range(len(final_third))}
    # print(final_third_dict)
    for key, value in final_third_dict.items():
        answer += int(value) * int(math.pow(3, key))

    print(answer)
    return answer

if __name__ == '__main__':
    n = 3

    solution(n)