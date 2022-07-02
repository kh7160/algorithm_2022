def solution(dartResult):
    bonus = {'S':1, 'D':2, 'T':3}
    result = [0]
    n = 0
    for idx, _ in enumerate(dartResult):
        if _ in bonus:
            result.append(int(dartResult[n:idx]) ** bonus[_])
        if _ == '*':
            result[-2:] = [num * 2 for num in result[-2:]]
        if _ == '#':
            result[-1:] = [-num for num in result[-1:]]
        if not str(_).isdigit():
            n = idx+1
    answer = sum(result)
    return answer

if __name__ == '__main__':
    # dartResult = '1S2D*3T'
    # dartResult = '1D2S#10S'
    # dartResult = '1D2S0T'
    # dartResult = '1S*2T*3S'
    dartResult = '1D2S3T*'
    solution(dartResult=dartResult)