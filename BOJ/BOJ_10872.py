def recur(n):
    if n == 1 or n == 0:
        return 1

    return n * recur(n-1)


n = int(input())
print(recur(n))

