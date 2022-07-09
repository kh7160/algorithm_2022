def solution(n):
    for i in range(1,n+1):
        # print(f'n % i = {n} % {i} = {n%i}')
        if n % i == 1:
            answer = i
            break

    print(answer)

if __name__ == "__main__":
    n = 3
    solution(n)