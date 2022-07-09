def solution():
    # a = [1,2,3,4]
    # b = [-3,-1,0,2]
    a = [-1,0,1]
    b = [1,0,-1]
    answer = 0

    for i in range(len(a)):
        answer += a[i] * b[i]

    print(answer)

if __name__ == '__main__':
    solution()