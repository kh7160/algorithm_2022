import itertools

n, m = map(int, input().split(' '))
card = list(map(int, input().split(' ')))
diff_min = 999999999
comb_card = list(itertools.combinations(card, 3))
for comb in comb_card:
    if diff_min > m - sum(comb) >= 0:
        answer = sum(comb)
        diff_min = m - sum(comb)

print(answer)