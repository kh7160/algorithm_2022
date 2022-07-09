def select_hand(clicked_num, left_num, right_num, hand):
    phone_num = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2),
                 '*': (3, 0), 0: (3, 1), '#': (3, 2)}

    left_position = phone_num[left_num]
    right_position = phone_num[right_num]
    clicked_position = phone_num[clicked_num]

    left_diff = abs(clicked_position[0] - left_position[0]) + abs(clicked_position[1] - left_position[1])
    right_diff = abs(clicked_position[0] - right_position[0]) + abs(clicked_position[1] - right_position[1])

    return 'R' if right_diff < left_diff else \
           'L' if left_diff < right_diff else \
           'R' if hand == 'right' else 'L'

def solution():
    # numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    # hand = 'right'
    # numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    # hand = 'left'
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    hand = 'right'
    left_num = '*'
    right_num = '#'
    answer = ''

    which_hand = {1:'L',4:'L',7:'L',3:'R',6:'R',9:'R',2:'?',5:'?',8:'?',0:'?'}

    for num in numbers:
        print(f'num : {num}, left_num : {left_num}, right_num : {right_num}')
        clicked = which_hand.get(num)
        if clicked != '?':
            answer += clicked
            print(f'answer : {answer}')
            if answer[-1] == 'L':
                left_num = num
            else:
                right_num = num
        else:
            answer += select_hand(num, left_num, right_num, hand)
            print(f'answer : {answer}')
            if answer[-1] == 'L':
                left_num = num
            else:
                right_num = num

    print(f'answer : {answer}')

if __name__ == "__main__":
    solution()