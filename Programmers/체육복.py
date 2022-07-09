def solution(n, lost, reverse):
    set_lost = set(lost)
    set_reverse = set(reverse)
    set_intersection = set_lost.intersection(set_reverse)
    lost = list(set_lost.difference(set_intersection))
    reverse = list(set_reverse.difference(set_intersection))
    answer = n - len(lost)
    for std in lost:
        print(f'std : {std}, reverse : {reverse}')
        if std in reverse:
            reverse.remove(std)
        elif std - 1 in reverse:
            answer += 1
            reverse.remove(std - 1)
        elif std + 1 in reverse:
            answer += 1
            reverse.remove(std + 1)

    print(answer)

if __name__ == '__main__':
    # n = 5
    # lost = [2,4]
    # reverse = [1,3,5]
    # n = 5
    # lost = [2,4]
    # reverse = [3]
    n = 3
    lost = [3]
    reverse = [1]
    solution(n, lost, reverse)