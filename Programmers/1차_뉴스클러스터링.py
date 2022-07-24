from collections import Counter


def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z']

    str1_lst = [str1[idx:idx+2] for idx, val in enumerate(str1[:-1]) if (str1[idx] in alpha) and (str1[idx+1] in alpha)]
    str2_lst = [str2[idx:idx+2] for idx, val in enumerate(str2[:-1]) if (str2[idx] in alpha) and (str2[idx+1] in alpha)]

    str1_c = Counter(str1_lst)
    str2_c = Counter(str2_lst)
    print(f'str1_c, str2_c : {str1_c, str2_c}')
    union_c = list((str1_c | str2_c).elements())
    inter_c = list((str1_c & str2_c).elements())
    print(f'str1_c + str2_c : {union_c}')
    print(f'str1_c & str2_c : {inter_c}')
    answer = 65536 if len(union_c) == 0 else int((len(inter_c) / len(union_c)) * 65536)
    print(answer)
    return answer


if __name__ == '__main__':
    # str1 = 'FRANCE'
    # str2 = 'french'
    # str1 = 'aa1+aa2'
    # str2 = 'AAAA12'
    # str1 = 'handshake'
    # str2 = 'shake hands'
    # str1 = 'E=M*C^2'
    # str2 = 'e=m*c^2'
    solution(str1, str2)