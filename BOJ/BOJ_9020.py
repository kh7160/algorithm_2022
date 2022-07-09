def get_prime_lists(n = 10000):
    chk = [False, False] + [True] * (n-1)
    primes = []
    for i in range(2, n+1):
        if chk[i]:
            primes.append(i)
            for j in range(i*2, n+1, i):
                chk[j] = False

    return chk, primes


n = int(input())
chk, primes = get_prime_lists()
for i in range(n):
    result = []
    gold_num = int(input())

    for j in range((gold_num//2)+1, 1, -1):
        if chk[j] and chk[gold_num-j]:
            result = [j, gold_num-j]
            break

    result = (result[0], result[1]) if result[0] < result[1] else (result[1], result[0])
    print(result[0], result[1])
