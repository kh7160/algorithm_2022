def isYaksu(num):
    cnt = 0

    for i in range(1,(num//2)+1):
        if num % i == 0:
            cnt += 1

    cnt += 1

    # print(f'num : {num}, cnt : {cnt}')

    return True if cnt % 2 == 0 else False

def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        answer = answer + num if isYaksu(num) else answer - num

    print(answer)

    return answer

if __name__ == "__main__":
    left = 13
    right = 17
    solution(left, right)