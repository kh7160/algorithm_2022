s = input()
s = s.upper()

cnt_dict = {}

for ch in s:
    if ch not in cnt_dict:
        cnt_dict[ch] = s.count(ch)

# arr = [(0,10),(1,14),(2,2),(3,24)]
# str = max(arr,key = lambda x:x[1])
max_value = max(cnt_dict.values())
result = list(filter(lambda x:cnt_dict[x] == max_value, cnt_dict.keys()))
# print(result)
print('?' if len(result) > 1 else result[0])