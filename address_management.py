# --------------------
# 1. 친구 리스트 출력
# 2. 친구추가
# 3. 친구삭제
# 4. 이름변경
# 9. 종료
# 메뉴를 선택하시오: 2
# 이름을 입력하시오: 홍길동
# --------------------
# 1. 친구 리스트 출력
# 2. 친구추가
# 3. 친구삭제
# 4. 이름변경
# 9. 종료
# 메뉴를 선택하시오: 1
# ['홍길동']
# --------------------

menu = 0
friend = []

while menu !=9:
    print("-"*20)
    print("1. 친구 리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("9. 종료")
    
    menu = int(input("메뉴를 선택하시오:"))

    if menu == 1:
        print(friend)
    elif menu == 2:
        friend.append(input("이름을 입력하시오:"))
    elif menu == 3:
        name = input("이름을 입력해주세요:")
        if name in friend:
            friend.remove(name)
        else:
            print("이름없음")
    elif menu == 4:
        oldname = input("예전 이름을 입력해주세요:")
        if oldname in friend:
            idx = friend.index(oldname)
            friend[idx] = input("새로운 이름은 입력해주세요:")
        else:
            print("이름없음")
    elif menu !=9:
        print("없는 메뉴입니다.")
    else:
        print("종료")

    


