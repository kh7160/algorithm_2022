s = input()
target = 'abcdefghijklmnopqrstuvwxyz'
result = []
for ch in target:
    try:
        # index 함수는 값이 없을 경우 ValueError, 문자열, 리스트, 튜플 자료형에서 사용 가능하고 딕셔너리 자료형에는 사용할 수 없어 AttributeError 에러가 발생한다.
        # find 함수는 값이 없을 경우 -1, 문자열을 찾을 수 있는 변수는 문자열만 사용이 가능하다. 리스트, 튜플, 딕셔너리 자료형에서는 find 함수를 사용할 수 없다.
        result.append(s.index(ch))
    except ValueError:
        result.append(-1)

for _ in result:
    print(_, end=' ')