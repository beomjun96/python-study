min_height, min_weight = map(int, input("민수의 키와 몸무게를 입력해주세요:").split())
gi_height, gi_weight = map(int, input("기영이의 키와 몸무게를 입력해주세요:").split())

if min_height>gi_height and min_weight>gi_weight:
    print("True")
else:
    print("False")
