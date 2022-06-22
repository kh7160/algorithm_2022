import math
from itertools import combinations

def solution(nums):
    answer = 0
    comb_nums = list(map(sum, combinations(nums, 3)))
    # itertools.combinations
    # for - else
    for num in comb_nums:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                break
        else:
            answer += 1

    print(answer)

if __name__ == "__main__":
    # nums = [1,2,3,4]
    nums = [1,2,7,6,4]
    solution(nums)
