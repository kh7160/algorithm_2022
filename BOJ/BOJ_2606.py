com_num = int(input())
edge_num = int(input())

edges = [[] for _ in range(com_num+1)]
visited = [False for _ in range(com_num+1)]
answer = 0


def dfs(com):
    global answer
    # print(f'com, visited[com], edges[com] : {com, visited[com], edges[com]}')
    if visited[com]:
        return

    answer += 1
    visited[com] = True
    for _ in edges[com]:
        dfs(_)


for _ in range(edge_num):
    fr, to = map(int, input().split(' '))
    edges[fr].append(to)
    edges[to].append(fr)
    # print(f'fr, to, edges : {fr, to, edges}')


for num in range(com_num):
    if not visited[num+1]:
        dfs(num+1)
        break

print(answer-1)