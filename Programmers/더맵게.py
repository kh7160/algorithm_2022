import heapq

def solution(scoville, K):
    answer = 0
    while len(scoville) > 1:
        # print(f'scoville : {scoville}')
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        if first < K or second < K:
            heapq.heappush(scoville, first + (second * 2))
            answer += 1
        else:
            break

    if len(scoville) == 1:
        if heapq.heappop(scoville) < K:
            answer = -1
        
    print(f'answer : {answer}')
    return answer


if __name__ == '__main__':
    # scoville = [1, 2, 3, 9, 10, 12]
    scoville = [0,0,0,0]
    # scoville = []
    K = 3
    solution(scoville, K)