# kor = int(input("국어, 수학, 영어 점수를 차례대로 입력해주세요:\n"))
# mat = int(input())
# eng = int(input())
# sum = kor+mat+eng

# print("kor",kor)
# print("mat",mat)
# print("eng",eng)
# print("sum",sum)
# print("avg",sum/3)

kor, mat, eng = map(int, input("국어, 수학, 영어 점수를 차례대로 입력해주세요:").split())  #map 자료형 정해서 입력, split 한번에 입력가능
sum = kor+mat+eng

print("kor",kor)
print("mat",mat)
print("eng",eng)
print("sum",sum)
print("avg",sum/3) #3과목 평균

'''왜 안될까? -> 스페이스바로 입력.... '''
