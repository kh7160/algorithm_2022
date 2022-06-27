n = int(input())
time = list(map(int, input().split(' ')))

# print(f'time : {time}')
time.sort()
# print(f'time.sort() : {time}')

time_sum = [sum(time[:i]) for i in range(1,len(time)+1)]
# print(f'time_sum : {time_sum}')
print(sum(time_sum))