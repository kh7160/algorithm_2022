from collections import deque

def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    while True:
        max_ = max(priorities)
        first = priorities.popleft()
        # print(f'max_, first : {max_, first}')
        if first != max_:
            priorities.append(first)
            location = location - 1 if location != 0 else len(priorities)-1
        else:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
        # print(f'location : {location}')
        
    # print(f'answer : {answer}')
    return answer

if __name__ == '__main__':
    priorities = [2, 1, 3, 2]
    # priorities = [1, 1, 9, 1, 1, 1]
    location = 2
    # location = 0
    solution(priorities, location)