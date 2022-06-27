# 10-20+30-40-50+60
sentence = input()

minus_split = sentence.split('-')
minus_result = -sum([sum(map(int, _.split('+'))) for _ in minus_split[1:]])
plus_split = [_ for _ in map(int, minus_split[0].split('+'))]
# print(f'plus_split : {plus_split}, minus_split : {minus_split}, minus_result : {minus_result}')
plus_result = sum(plus_split)
# print(f'plus_result : {plus_result}, minus_result : {minus_result}')
print(plus_result + minus_result)