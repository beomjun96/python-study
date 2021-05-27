# http://toglobalmate.com/contents/pop_test.htm 참고

print("호주독립기술이민자격 점수체크표")

sum = 0

# while True:
#     # 나이점수
#     age = int(input("나이를 입력해주세요:"))
#     if age >= 18 and age <= 24:
#         print("나이점수 : 25")
#         sum += 25
#         print("총 점수 : ",sum)
    
#     elif age >= 25 and age <= 32:
#         print("나이점수 : 30")
#         sum += 30
#         print("총 점수 : ",sum)

#     elif age >= 33 and age <= 39:
#         print("나이점수 : 25")
#         sum += 25
#         print("총 점수 : ",sum)

#     elif age >= 40 and age <= 44:
#         print("나이점수 : 15")
#         sum += 15
#         print("총 점수 : ",sum)

#     # 영어점수
#     en_kinds = input("시험 종류 번호를 선택해주세요 \n1. IELTS\n2.PTE")
#     if en_kinds == 1:
#         en_point = float(input("영어 점수를 입력해주세요:"))
#         if en_point >= 8.0:
#             print("Superior 영어점수 : 20")
#             sum += 20
#             print("총 점수 : ", sum)
#         elif en_point >=7.0:
#             print("Proficient 영어점수 : 10")
#             sum += 10
#             print("총 점수 : ", sum)


#     if en_kinds == 2:
#         en_point = float(input("영어 점수를 입력해주세요:"))
#         if en_point >= 79:
#             print("Superior 영어점수 : 20")
#             sum += 20
#             print("총 점수 : ", sum)
#         elif en_point >=65:
#             print("Proficient 영어점수 : 10")
#             sum += 10
#             print("총 점수 : ", sum)

#     # 호주에서 경력
#     auWorksAge = int(input("호주에서 경력(최근 10년간 신청직업과 밀접한 경력)을 입력해주세요 (년 단위): "))
#     if auWorksAge >= 5:
#         print("경력점수 : 15")
#         sum += 15
#         print("총 점수 : ",sum)

#     elif auWorksAge >=3:
#         print("경력점수 : 10")
#         sum += 10
#         print("총 점수 : ",sum)

#     elif auWorksAge >=1:
#         print("경력점수 : 5")
#         sum += 5
#         print("총 점수 : ",sum)

#     # 학력
#     education = int(input("학력 번호를 입력해주세요\n1. 박사학위\n2. 학사학위\n3. 호주에서 Diploma/Trade Qualification 또는 기술심사기관이 인정하는 학위"))
#     if education == 1:
#         print("학력 점수 : 20")
#         sum += 20
#         print("총 점수 : ",sum)

#     elif education == 2:
#         print("학력 점수 : 15")
#         sum += 15
#         print("총 점수 : ",sum)

#     elif education == 3:
#         print("학력 점수 : 10")
#         sum += 10
#         print("총 점수 : ",sum)
    
    # 호주에서 학업
    auStudyYear = input("2 academic years, 16개월 이상 (y/Y or n/N) : ")
    if auStudyYear == "y" or auStudyYear == "Y":
        print("학업 점수 : 5")
        sum += 5
        print("총 점수 : ",sum)