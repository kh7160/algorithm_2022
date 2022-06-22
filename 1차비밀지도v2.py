def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        # zip
        # bin
        a12 = str(bin(i | j)[2:])
        print(bin(i))
        print(int(bin(i), 2))
        # rjust
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer

if __name__ == "__main__":
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    # n = 6
    # arr1 = [46, 33, 33 ,22, 31, 50]
    # arr2 = [27 ,56, 19, 14, 14, 10]
    answer = solution(n, arr1=arr1, arr2=arr2)
    print(answer)