def solution(N, stages):
    answer = []
    people = len(stages)
    stages_fail_rate = {}

    for stage in range(1,N+1):
        stage_cnt = stages.count(stage)
        if people != 0:
            stages_fail_rate[stage] = stage_cnt / people
            people -= stage_cnt
        else:
            stages_fail_rate[stage] = 0

    print(stages_fail_rate)
    answer = sorted(stages_fail_rate, key=lambda x:stages_fail_rate[x], reverse=True)
    
    print(answer)

    return answer

if __name__ == "__main__":
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    solution(N, stages)