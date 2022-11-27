def solution(elements):
    answer = 0
    el_len = len(elements)
    elements = elements * 2
    sum_set = set()
    for i in range(el_len):
        # sum_set = set()
        for j in range(el_len):
            sum_set.add(sum(elements[j:j+i+1]))
        # print(sum_set)
    answer = len(sum_set)
    # print(answer)
    return answer


if __name__ == '__main__':
    elements = [7,9,1,1,4]
    solution(elements)