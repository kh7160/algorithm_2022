input_list = list(map(int, input().split(' ')))
result = int((input_list[0] / (input_list[2] - input_list[1]))) + 1 if (input_list[2] - input_list[1]) > 0 else -1
print(result)