def solution(record):
    answer = []
    id_dict = {}
    sentence_list = []
    sentences = [sentence.split(' ') for sentence in record]
    for sentence in sentences:
        if sentence[0] == 'Enter':
            sentence_list.append([sentence[1], '님이 들어왔습니다.'])
            id_dict[sentence[1]] = sentence[2]
        elif sentence[0] == 'Leave':
            sentence_list.append([sentence[1], '님이 나갔습니다.'])
        elif sentence[0] == 'Change':
            id_dict[sentence[1]] = sentence[2]

    for _ in sentence_list:
        answer.append(id_dict[_[0]]+_[1])

    # print(answer)
    return answer

if __name__ == '__main__':
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    solution(record)