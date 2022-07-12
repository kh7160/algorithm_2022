# n = int(input())
def draw(n):
    if n == 1:
        return ['*']

    rect = draw(n//3)
    # print(f'rect : {rect}')
    fin_rect = []
    for i in rect:
        fin_rect.append(i * 3)
    for i in rect:
        fin_rect.append(i + ' ' * (n // 3) + i)
    for i in rect:
        fin_rect.append(i * 3)
    # print(f'fin_rect : {fin_rect}')
    return fin_rect


if __name__ == '__main__':
    result = draw(27)
    print('\n'.join(result))