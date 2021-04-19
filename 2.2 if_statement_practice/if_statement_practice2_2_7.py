# 가상의 두 사람(A, B)이 가위 바위 보 중 하나를 내서 승패를 가르는 가위 바위 보 게임을 작성하십시오.
# 이 때 ["가위", "바위", "보"] 리스트를 활용합니다.
# 입력 예: "가위" "바위"
# 출력 예: "B가 이겼습니다."

a, b = input("A랑 B 가위바위보 내주세요:").split()
lis = ["가위", "바위", "보"]

if a == lis[0]:             # A 가위
    if b == lis[0]:             # B 가위
        print("비김")
    elif b==lis[1]:             # B 바위
        print("B가 이김")
    elif b==lis[2]:             # B 보
        print("A가 이김")
elif a== lis[1]:             # A 바위
    if b == lis[0]:             # B 가위
        print("A가 이김")
    elif b==lis[1]:             # B 바위
        print("비김")
    elif b==lis[2]:             # B 보
        print("B가 이김")
elif a== lis[1]:             # A 보
    if b == lis[0]:             # B 가위
        print("B가 이김")
    elif b==lis[1]:             # B 바위
        print("A가 이김")
    elif b==lis[2]:             # B 보
        print("비김")