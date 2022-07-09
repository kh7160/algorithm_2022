phone = {
    'ABC':3,
    'DEF':4,
    'GHI':5,
    'JKL':6,
    'MNO':7,
    'PQRS':8,
    'TUV':9,
    'WXYZ':10
}

s = input()
s_list = list(s)
result = 0
for _ in s_list:
    for key, value in phone.items():
        if _ in key:
            result += value

print(result)