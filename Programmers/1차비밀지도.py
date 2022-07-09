def toSecond(arr):
    result = []
    second = ""
    for num in arr:
        while True:
            div, mod = divmod(num, 2)
            # print(f'div, mod = {div}, {mod}')
            if div < 2:
                second += str(mod)
                second += str(div)
                break
            else:
                second += str(mod)
                num = div

        for i in range(len(arr)-len(second)):
            second += "0"

        second = list(second)
        second.reverse()
        result.append(second)
        second = ""

    return result

def solution(n, arr1, arr2):
    answer = []
    arr1 = toSecond(arr1)
    arr2 = toSecond(arr2)
    # print(f'arr1 = {arr1}\narr2 = {arr2}')
    result = ""
    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                result += '#'
            else:
                result += ' '

        answer.append(result)
        result = ""

    print(answer)
    return answer

if __name__ == "__main__":
    # n = 5
    # arr1 = [9, 20, 28, 18, 11]
    # arr2 = [30, 1, 21, 17, 28]
    n = 6
    arr1 = [46, 33, 33 ,22, 31, 50]
    arr2 = [27 ,56, 19, 14, 14, 10]
    solution(n, arr1=arr1, arr2=arr2)