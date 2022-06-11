def solution():
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi", "muzi frodo"]
    k = 2
    # id_list = ["con", "ryan"]
    # report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    # k = 3
    answer = [0 for _ in range(len(id_list))]
    report = set(report)

    # 필요 사항
    # from, to list
    # k번 이상 목록

    from_to_dict = {}
    k_up_dict = {}

    for report_one in report:
        key, val = report_one.split(" ")

        # 신고당한 횟수 체크
        k_up_dict[val] = (k_up_dict[val] + 1) if k_up_dict.get(val) is not None else 1
        # 신고한 사람 리스트 정리
        from_to_dict[key] = (from_to_dict[key] + [val]) if from_to_dict.get(key) is not None else [val]

    # print(from_to_dict)
    # print(k_up_dict)

    mail_list = [_ for _ in k_up_dict.keys() if k_up_dict[_] >= k]
    # print(mail_list)

    for i in range(len(id_list)):
        if id_list[i] in from_to_dict.keys():
            for j in from_to_dict[id_list[i]]:
                if j in mail_list:
                    answer[i] += 1

    print(answer)
if __name__ == '__main__':
    solution()