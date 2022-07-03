t = input()
p = []
# print(t)
for _ in range(int(t)):
    result = ''
    rs_list = input().split(' ')
    # print(rs_list)
    r = int(rs_list[0])
    s = rs_list[1]
    for ch in s:
        result += ch*r
    p.append(result)

for _ in p:
    print(_)