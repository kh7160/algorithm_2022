from itertools import combinations

def solution(nums):

    answer_set = set(nums)

    answer = len(answer_set) if len(answer_set) < len(nums)//2 else len(nums)//2

    print(answer)

if __name__ == "__main__":
    # nums = [3,1,2,3]
    # nums = [3,3,3,2,2,4]
    # nums = [3,3,3,2,2,2]

    solution(nums)