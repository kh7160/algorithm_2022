from collections import deque

places = input().replace('[','').replace(']','').replace(' ','').replace('"','').split(',')
map_ = []
for i in range(0, len(places), 5):
    map_.append(places[i:i+5])

places = []
for map_one in map_:
    places.append([list(_) for _ in map_one])

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(place):
    start = []
    
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                start.append([i,j])
    # print(f'start : {start}')
    for st in start:
        queue = deque([st])
        visited = [[0]*5 for _ in range(5)]
        dist_ = [[0]*5 for _ in range(5)]

        while queue:
            sx, sy = queue.popleft()
            visited[sx][sy] = 1
            # print(f'sx, sy : {sx, sy}')
            for k in range(4):
                sdx = sx + dx[k]
                sdy = sy + dy[k]
                if (0 <= sdx < 5) and (0 <= sdy < 5) and visited[sdx][sdy] == 0 and place[sdx][sdy] != 'X':
                    # print(f'sdx, sdy : {sdx, sdy}')
                    queue.append([sdx, sdy])
                    visited[sdx][sdy] = 1
                    dist_[sdx][sdy] = dist_[sx][sy] + 1

                    if place[sdx][sdy] == 'P' and dist_[sdx][sdy] <= 2:
                        # print(f'sx, sy, sdx, sdy : {sx, sy, sdx, sdy}')
                        return 0

    return 1

def solution(places):
    answer = []
    
    for _ in places:
        # print(_)
        answer.append(bfs(_))

    # print(answer)
    return answer

if __name__ == '__main__':
    solution(places)