def dfs(i,j):
    global is_region
    global cnt
    if i == n or j == n or i < 0 or j < 0:
        return

    if n_map[i][j] and not chk[i][j]:
        # print(f'i, j, n_map[i][j], chk[i][j] : {i, j, n_map[i][j], chk[i][j]}')
        cnt += 1
        is_region = True
        chk[i][j] = True

        # 위
        dfs(i - 1, j)
        # 오른쪽
        dfs(i, j + 1)
        # 아래
        dfs(i + 1, j)
        # 오른쪽
        dfs(i, j - 1)

    else:
        return


n = int(input())
n_map = []
answer = 0
cnt = 0
cnt_lst = []
for i in range(n):
    n_map.append(list(map(int, list(input()))))

chk = [[False] * len(_) for _ in n_map]
is_region = False

for i in range(n):
    for j in range(n):
        dfs(i,j)
        if is_region:
            is_region = False
            cnt_lst.append(cnt)
            cnt = 0
            answer += 1

print(answer)
cnt_lst.sort()
for _ in cnt_lst:
    print(_)