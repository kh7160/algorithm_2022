n = int(input())
visited = [False] * (n+1)
nums = list(map(int, [input() for _ in range(n)]))
is_cycle = False
nums.insert(0, 0)
answer = []
# print(f'visited, nums : {visited, nums}')


def dfs(node):
    global is_cycle
    # print(f'node, visited[node], answer : {node, visited[node], answer}')
    if not visited[node]:
        visited[node] = True
        answer.append(node)
    else:
        if node == first: # 방문 node일 경우 처음 시작과 동일한지 체크
            is_cycle = True
        return

    dfs(nums[node])
    if not is_cycle:
        visited[node] = False
        answer.remove(node)


for i in range(1, n+1):
    first = i
    is_cycle = False
    dfs(i)
    # print(f'answer : {answer}')

answer.sort()
print(len(answer))
for _ in answer:
    print(_)