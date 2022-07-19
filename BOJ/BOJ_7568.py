n = int(input())
people = []
rank = []
for _ in range(n):
    (x, y) = map(int, input().split(' '))
    people.append((x, y))

for i in range(len(people)):
    i_x, i_y = people[i][0], people[i][1]
    rank_i = 0
    for x, y in people:
        if i_x < x and i_y < y:
            rank_i += 1
    rank.append(rank_i+1)

print(*rank)