# kor = int(input("국어, 수학, 영어 점수를 차례대로 입력해주세요:\n"))
# mat = int(input())
# eng = int(input())
# sum = kor+mat+eng

# print("kor",kor)
# print("mat",mat)
# print("eng",eng)
# print("sum",sum)
# print("avg",sum/3)

kor, mat, eng = map(int, input("국어, 수학, 영어 점수를 차례대로 입력해주세요:").split())
sum = kor+mat+eng

print("kor",kor)
print("mat",mat)
print("eng",eng)
print("sum",sum)
print("avg",sum/3)

'''왜 안될까? -> 스페이스바로 입력.... '''
