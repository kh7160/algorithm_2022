def solution(sizes):
    answer = 0
    for _ in sizes:

        if _[0] < _[1]:
            _[1], _[0] = _[0], _[1]

    # print(sizes)
    weight = max([_[0] for _ in sizes])
    height = max([_[1] for _ in sizes])

    answer = weight * height
    # print(answer)

    return answer

if __name__ == '__main__':
    # sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
    # sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
    sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
    solution(sizes)