def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=lambda x:x*3)
    print(numbers)
    answer = str(int(''.join(numbers)))
    print(answer)
    return answer

if __name__ == '__main__':
    numbers = [6, 10, 2]
    numbers = [3, 30, 34, 5, 9]
    numbers = [3, 30, 32, 5, 9]
    solution(numbers)