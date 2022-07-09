# 에라토스테네스의 체
def get_prime_list(n):
    chk = [False, False] + [True] * (n - 1)
    primes = []
    for i in range(2, n + 1):
        primes.append(i)
        if chk[i]:
            for j in range(2 * i, n + 1, i):
                chk[j] = False

    return chk


chk = get_prime_list(123456 * 2)
while True:
    n = int(input())
    if n == 0:
        break

    print(sum([_ for _ in chk[n + 1:n * 2 + 1] if _ == True]))
