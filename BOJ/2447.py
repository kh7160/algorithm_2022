fin = int(input())

def draw_rect(n, pattern):
    if fin == n:
        return

    for i in range(len(pattern)):
        pattern[i] = pattern[i] * 3
        print(pattern[i])

    for i in range(len(pattern)):
        print(pattern[i], end='')
        if i % 3 == 2:
            print()

    draw_rect(n*3, pattern)

if __name__ == '__main__':
    pattern = ['*','*','*','*',' ','*','*','*','*']
    draw_rect(1, pattern)
