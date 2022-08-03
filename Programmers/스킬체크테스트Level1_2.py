def solution(a, b):
    answer = ''
    day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    map_day = {
        1:'FRI',
        2:'SAT',
        3:'SUN',
        4:'MON',
        5:'TUE',
        6:'WED',
        0:'THU',
    }
    tot = 0
    for month in range(a):
        print(f'month, day[month], tot : {month, day[month], tot}')
        tot += day[month]
    tot += b
    print(tot)
    answer = map_day[tot%7]

    return answer

if __name__ == '__main__':
    a, b = 5, 24
    # a, b = 1, 3
    print(solution(a, b))