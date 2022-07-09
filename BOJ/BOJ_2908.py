input_list = [list(reversed(_)) for _ in input().split(' ')]
a, b = int(''.join(input_list[0])), int(''.join(input_list[1]))
# print(input_list)
print(a if a > b else b)