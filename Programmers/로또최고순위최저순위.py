def solution():
    # lottos = [44, 1, 0, 0, 31, 25]
    # win_nums = [31, 10, 45, 1, 6, 19]
    # lottos = [0, 0, 0, 0, 0, 0]
    # win_nums = [38, 19, 20, 40, 15, 25]
    lottos = [45, 4, 35, 20, 3, 9]
    win_nums = [20, 9, 3, 45, 4, 35]

    win_dict = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    undecisioned_cnt = lottos.count(0)
    matched_cnt = 0

    for num in lottos:
        if num in win_nums:
            matched_cnt += 1

    before_rank = win_dict[matched_cnt]
    after_rank = win_dict[matched_cnt + undecisioned_cnt]

    answer = [after_rank, before_rank]
    print(answer)

if __name__ == '__main__':
    solution()