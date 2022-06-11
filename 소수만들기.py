def isOdd(num):

    cnt = 1

    for i in range(1, num//2 + 1):
        if (num % i) == 0:
            cnt += 1

        if cnt > 2:
            break

    return True if cnt == 2 or num == 1 else False

def solution():
    nums = [1,2,7,6,4]
    num = 0
    result = 0

    for i in range(len(nums)):
        num += nums[i]
        for j in range(i+1, len(nums)):
            num += nums[j]
            for k in range(j+1, len(nums)):
                num += nums[k]
                oddYn = isOdd(num)
                result += 1 if oddYn is True else 0
                num -= nums[k]
            num -= nums[j]
        num -= nums[i]

    print(result)
if __name__ == '__main__':
    solution()