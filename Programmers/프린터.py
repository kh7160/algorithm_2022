from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    max_ = max(queue)
    while True:
        left_ = queue.popleft()
        print(f'queue, location : {queue, location}')
        if max_ == left_:
            answer += 1
            if location == 0:
                break
            else:
                print(f'max_queue, location : {queue, location}')
                max_ = max(queue)
                location = location - 1 if location > 0 else len(queue)-1
                continue

        queue.append(left_)
        location = location - 1 if location > 0 else len(queue)-1
        print(f'queue, location : {queue, location}')

    print(f'answer : {answer}')
    return answer


if __name__ == '__main__':
    priorities = [2,1,3,2]
    location = 2
    # priorities = [1, 1, 9, 1, 1, 1]
    # location = 0
    solution(priorities=priorities, location=location)