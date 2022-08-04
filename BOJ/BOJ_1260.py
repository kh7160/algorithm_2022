from collections import deque
import sys
sys.setrecursionlimit(10**6)

n,m,v = map(int, input().split(' '))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)
graph = graph[1:]
[_.sort() for _ in graph]


def dfs(node):
    if visited[node-1]:
        return

    visited[node-1] = True
    print(node, end=' ')
    for dot in graph[node-1]:
        dfs(dot)


def bfs(node):
    deq = deque([node])
    visited[node-1] = True

    while deq:
        node2 = deq.popleft()
        print(node2, end=' ')

        for dot in graph[node2-1]:
            if not visited[dot-1]:
                deq.append(dot)
                visited[dot - 1] = True
    

if __name__ == '__main__':
    visited = [False for _ in range(n)]
    dfs(v)
    print()
    visited = [False for _ in range(n)]
    bfs(v)