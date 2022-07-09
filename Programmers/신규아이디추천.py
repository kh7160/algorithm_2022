def solution():
    # new_id = "...!@BaT#*..y.abcdefghijklm"
    # new_id = "z-+.^."
    # new_id = "=.="
    # new_id = "123_.def"
    new_id = "abcdefghijklmn.p"

    # 1단계 대문자 => 소문자
    new_id = new_id.lower()
    print(new_id)

    # 2단계 소문자, 숫자, -, _, . 제외 문자 제거
    new_id = "".join(filter(lambda x: x in ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z','-','_','.',
                                            '1','2','3','4','5','6','7','8','9','0']
                    , new_id))
    print(new_id)

    # 3단계 마침표 2개 연속 나오면 1개로 대체
    while new_id.count("..") != 0:
        new_id = new_id.replace("..", ".")
    print(new_id)

    # 4단계 마침표가 처음이나 마지막에 있을 경우 제거
    new_id_list = list(new_id)
    if len(new_id_list) > 0:
        if new_id_list[0] == '.':
            new_id_list.pop(0)

    if len(new_id_list) > 0:
        if new_id_list[len(new_id_list)-1] == '.':
            new_id_list.pop(len(new_id_list)-1)

    new_id = "".join(new_id_list)
    print(new_id)

    # 5단계 new_id가 빈문자열일 경우 "a" 대입
    new_id = "a" if len(new_id) == 0 else new_id
    print(new_id)

    # 6단계 new_id 가 16자리 이상일 경우 15자리 이후 제거, 마지막 마침표일 경우 마침표 제거
    if len(new_id) > 15:
        new_id = new_id[:15]

    new_id_list = list(new_id)
    if new_id_list[len(new_id_list)-1] == '.':
        new_id_list.pop(len(new_id_list)-1)

    new_id = "".join(new_id_list)
    print(new_id)

    # 7단계 new_id의 길이가 2 이하일 경우 마지막 문자를 길이가 3이 될 때 까지 더한다.
    new_id_list = list(new_id)
    while len(new_id_list) < 3:
        new_id_list.append(new_id_list[-1])

    new_id = "".join(new_id_list)
    print(new_id)

if __name__ == '__main__':
    solution()