s = input()
s = s.upper()

cnt_dict = {}

for ch in s:
    if ch not in cnt_dict:
        cnt_dict[ch] = s.count(ch)

# arr = [(0,10),(1,14),(2,2),(3,24)]
# str = max(arr,key = lambda x:x[1])
max_value = max(cnt_dict.values())
cnt = 0
for key, value in cnt_dict.items():
    if value == max_value:
        cnt += 1
        result = key

print('?' if cnt > 1 else result)