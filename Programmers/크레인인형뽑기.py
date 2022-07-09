def solution(board, moves):
    result = []
    fix_board = []
    answer = 0

    for i in range(len(board)):
        fix_board.append([_[i] for _ in board if _[i] != 0])

    for _ in fix_board:
        _.reverse()

    moves = [_-1 for _ in moves]
    pop_num = 0

    for i in moves:
        if len(fix_board[i]) != 0:
            pop_num = fix_board[i].pop()
            if len(result) != 0 and pop_num == result[-1]:
                result.pop()
                answer += 2
            else:
                result.append(pop_num)

    print(answer)

if __name__ == '__main__':
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    solution(board, moves)