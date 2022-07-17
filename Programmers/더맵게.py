# heapq
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        print(f'scoville : {scoville}')
        min_sco = heapq.heappop(scoville)
        if min_sco >= K:
            break

        if len(scoville) == 0:
            answer = -1
            break

        scd_min_sco = heapq.heappop(scoville)
        new_sco = min_sco + scd_min_sco * 2
        heapq.heappush(scoville, new_sco)
        answer += 1

    print(answer)
    return answer


if __name__ == '__main__':
    # scoville = [1, 2, 3, 9, 10, 12]
    scoville = [1,1]
    k = 0
    solution(scoville=scoville, K=k)
