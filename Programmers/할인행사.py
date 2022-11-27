from collections import Counter

def solution(want, number, discount):
    answer = 0
    ogn_dict = {}

    for want_, number_ in zip(want, number):
        ogn_dict[want_] = number_

    for idx in range(len(discount)-10+1):
        diff_dict = Counter(discount[idx:idx+10])
        if diff_dict == ogn_dict:
            answer += 1

    print(answer)
    return answer


if __name__ == '__main__':
    want = ["banana", "apple", "rice", "pork", "pot"]
    # want = ["apple"]
    number = [3, 2, 2, 2, 1]
    # number = [10]
    discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
    # discount = ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
    solution(want, number, discount)