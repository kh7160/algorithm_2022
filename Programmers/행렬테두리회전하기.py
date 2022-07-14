def solution(rows, columns, queries):
    answer = []
    sqr = [[i + (j*columns) for i in range(1, columns+1)] for j in range(rows)]
    for x1, y1, x2, y2 in queries:
        tmp = sqr[x1-1][y1-1]
        sqr_min = tmp
        # 좌측변 위로 이동
        for i in range(x1-1, x2-1):
            sqr[i][y1-1] = sqr[i+1][y1-1]
            sqr_min = min(sqr_min, sqr[i][y1-1])
        # 아랫변 좌측 이동
        for j in range(y1 - 1, y2 - 1):
            sqr[x2-1][j] = sqr[x2-1][j+1]
            sqr_min = min(sqr_min, sqr[x2-1][j])
        # 우측변 아래 이동
        for i in range(x2-1, x1-1, -1):
            sqr[i][y2-1] = sqr[i-1][y2-1]
            sqr_min = min(sqr_min, sqr[i][y2-1])
        # 윗변 우측 이동
        for j in range(y2-1, y1-1, -1):
            sqr[x1-1][j] = sqr[x1-1][j-1]
            sqr_min = min(sqr_min, sqr[x1-1][j])
        sqr[x1-1][y1] = tmp
        # for _ in sqr:
        #     print(_)
        # print()

        answer.append(sqr_min)
    return answer


if __name__ == '__main__':
    # rows, columns = 6, 6
    # queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
    # rows, columns = 3, 3
    # queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
    rows, columns = 3, 4
    queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
    solution(rows, columns, queries)