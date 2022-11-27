from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque()
    queue.append([begin, 0])

    while queue:
        bf, step = queue.popleft()
        for word in words:
            if bf == target:
                return step
            cnt = 0
            for i in range(len(word)):
                if bf[i] != word[i]:
                    cnt += 1
            if cnt == 1:
                queue.append([word, step+1])


if __name__ == '__main__':
    begin = 'hit'
    target = 'cog'
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(begin, target, words))