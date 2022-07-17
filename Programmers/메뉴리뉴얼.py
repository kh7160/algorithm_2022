# Counter

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for num in course:
        order_li = []
        for order in orders:
            comb_list = list(combinations(list(order), num))
            for comb in comb_list:
                comb = sorted(comb)
                comb = ''.join(comb)
                order_li.append(comb)

        comb_ct = Counter(order_li).most_common()
        answer += [k for k, v in comb_ct if v > 1 and v == comb_ct[0][1]]

    answer.sort()
    # print(answer)
    return answer


if __name__ == '__main__':
    # orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    # course = [2,3,4]
    # orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
    # course = [2,3,5]
    orders = ["XYZ", "XWY", "WXA"]
    course = [2,3,4]
    solution(orders, course)