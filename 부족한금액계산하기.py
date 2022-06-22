def solution(price, money, count):
    answer = 0
    price_list = [_*price for _ in range(1, count+1)]
    sum_of_price_list = sum(price_list)

    answer = sum_of_price_list - money if sum_of_price_list > money else 0
    print(answer)

if __name__ == "__main__":
    price = 3
    money = 20
    count = 4
    solution(price, money, count)