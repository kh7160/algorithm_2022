def chess(bb):
    cnt_1 = 0
    cnt_2 = 0

    even, odd = 'B', 'W'
    for i in range(8):
        for j in range(0, 8, 2):
            if bb[i][j] != even:
                cnt_1 += 1
        for j in range(1, 8, 2):
            if bb[i][j] != odd:
                cnt_1 += 1
        even, odd = odd, even

    even, odd = 'W', 'B'
    for i in range(8):
        for j in range(0, 8, 2):
            if bb[i][j] != even:
                cnt_2 += 1
        for j in range(1, 8, 2):
            if bb[i][j] != odd:
                cnt_2 += 1
        even, odd = odd, even

    return min(cnt_1, cnt_2)


n, m = map(int, input().split(' '))
bb = [list(input()) for _ in range(n)]
answer = []

for i in range(n-8+1):
    for j in range(m-8+1):
        cc = [_[j:j+8] for _ in bb[i:i+8]]
        answer.append(chess(cc))

print(min(answer))