def recur(n):
    if n == 0 or n == 1:
        return 1

    return n * recur(n - 1)

if __name__ == '__main__':
    n = int(input())
    result = recur(n)
    print(result)