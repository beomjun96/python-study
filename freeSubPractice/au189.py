# http://toglobalmate.com/contents/pop_test.htm 참고

print("2020 호주독립기술이민자격 점수체크표")

sum = 0

while True:
    # 나이점수
    age = int(input("나이를 입력해주세요:"))
    if age >= 18 and age <= 24:
        print("나이점수 : 25")
        sum += 25
        print("총 점수 : ",sum)
    
    elif age >= 25 and age <= 32:
        print("나이점수 : 30")
        sum += 30
        print("총 점수 : ",sum)

    elif age >= 33 and age <= 39:
        print("나이점수 : 25")
        sum += 25
        print("총 점수 : ",sum)

    elif age >= 40 and age <= 44:
        print("나이점수 : 15")
        sum += 15
        print("총 점수 : ",sum)

    # 영어점수
    en_kinds = int(input("시험 종류 번호를 선택해주세요 \n1. IELTS\n2.PTE\n"))
    if en_kinds == 1:
        en_point = float(input("영어 점수를 입력해주세요:"))
        if en_point >= 8.0:
            print("Superior 영어점수 : 20")
            sum += 20
            print("총 점수 : ", sum)
        elif en_point >=7.0:
            print("Proficient 영어점수 : 10")
            sum += 10
            print("총 점수 : ", sum)


    if en_kinds == 2:
        en_point = float(input("영어 점수를 입력해주세요:"))
        if en_point >= 79:
            print("Superior 영어점수 : 20")
            sum += 20
            print("총 점수 : ", sum)
        elif en_point >=65:
            print("Proficient 영어점수 : 10")
            sum += 10
            print("총 점수 : ", sum)

    # 호주에서 경력
    auWorksAge = int(input("호주에서 경력(최근 10년간 신청직업과 밀접한 경력)을 입력해주세요 (년 단위): "))
    if auWorksAge >= 5:
        print("경력점수 : 15")
        sum += 15
        print("총 점수 : ",sum)

    elif auWorksAge >=3:
        print("경력점수 : 10")
        sum += 10
        print("총 점수 : ",sum)

    elif auWorksAge >=1:
        print("경력점수 : 5")
        sum += 5
        print("총 점수 : ",sum)

    # 학력
    education = int(input("학력 번호를 입력해주세요\n1. 박사학위\n2. 학사학위\n3. 호주에서 Diploma/Trade Qualification 또는 기술심사기관이 인정하는 학위\n"))
    if education == 1:
        print("학력 점수 : 20")
        sum += 20
        print("총 점수 : ",sum)

    elif education == 2:
        print("학력 점수 : 15")
        sum += 15
        print("총 점수 : ",sum)

    elif education == 3:
        print("학력 점수 : 10")
        sum += 10
        print("총 점수 : ",sum)
    
    # 호주에서 학업
    auStudyYear = input("2 academic years(호주에서 학업), 16개월 이상 (y/Y or n/N) : ")
    if auStudyYear == "y" or auStudyYear == "Y":
        print("학업 점수 : 5")
        sum += 5
        print("총 점수 : ",sum)
    else:
        print("학업 점수: 0")
        print("총 점수 : ",sum)

    #과학기술 호주 고학력자
    pd_pdh = input("과학기술분야 호주대학(2년 이상) 석사(Research) 또는 박사학위 취득자 (y/Y or n/N) : ")
    if pd_pdh == "y" or pd_pdh == "Y":
        print("고학력자 점수 : 10")
        sum += 10
        print("총 점수 : ",sum)
    else:
        print("고학력자 점수: 0")
        print("총 점수 : ",sum)

    #NAATI 통역 or 번역 자격
    trance = input("NAATI 통역 or 번역 자격 Paraprofessional 이상   (y/Y or n/N) : ")
    if trance == "y" or trance == "Y":
        print("통역 점수 : 5")
        sum += 5
        print("총 점수 : ",sum)
    else:
        print("통역 점수: 0")
        print("총 점수 : ",sum)

    #PY(최근 4년내)
    py = input("Professional Year(최근 4년내) 12개월 이상 코스 수료  (y/Y or n/N) : ")
    if py == "y" or py == "Y":
        print("PY 점수 : 5")
        sum += 5
        print("총 점수 : ",sum)
    else:
        print("PY 점수: 0")
        print("총 점수 : ",sum)


    #지역 점수
    region = input("지정 Regional 지역 거주 및 학습 2년 이상 (y/Y or n/N) : ")
    if region == "y" or region == "Y":
        print("지역 점수 : 5")
        sum += 5
        print("총 점수 : ",sum)
    else:
        print("지역 점수: 0")
        print("총 점수 : ",sum)

    #배우자 점수
    partner = int(input("배우자 점수\n1. 만 45세 미만 / Competent English 이상 / 기술심사 통과 (배우자직업은 189, 491친척후원 경우 기술이민 MLTSSL / 190, 491주정부후원 경우 기술이민 MLTSSL, STSOL OR ROL)\n2. 파트너가 없는 싱글인 경우\n3. Competent English을 소지한 파트너가 있는 경우\n4. 그 밖에 경우\n번호를 선택해주세요 : "))
    if partner == 1:
        print("배우자 점수 : 10")
        sum += 10
        print("총 점수 : ",sum)

    elif partner == 2:
        print("배우자 점수 : 10")
        sum += 10
        print("총 점수 : ",sum)

    elif partner == 3:
        print("배우자 점수 : 5")
        sum += 5
        print("총 점수 : ",sum)

    elif partner == 4:
        print("배우자 점수 : 0")
        sum += 0
        print("총 점수 : ",sum)

    Q = input("다시 입력하시겠습니까? (y/Y or n/N) : ")
    if Q =='n' or Q == 'N':
        break

