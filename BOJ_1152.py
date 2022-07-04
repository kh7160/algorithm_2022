s = input()
s = s.strip(' ')
s_list = s.split(' ') if len(s) > 0 else []
print(len(s_list))