# 학생들의 점수를 입력을 받다가 0이 입력되면 그 때까지 입력받은 점수를 10점 단위로 구분하여 점수대별 학생 수를 출력하는 프로그램을 작성하시오.
# 1명도 없는 점수는 출력하지 않는다.
# 입력 예: 63 80 95 100 46 64 88 0

grade_list = []
x=1
count = 0
cutline = []

while x !=0:
    x = int(input("성적 입력:"))
    grade_list.append(x)            # 0점 입력 받기 전까지 점수 저장
    count += 1

for x in range(0,11):
    cutline.append(0)               # 커트라인 인덱스 0번부터 100점~0점까지 0 저장

for grade in range(0,count):        # 점수 대 별로 학생수 카운트
    if grade_list[grade] == 100:
        cutline[0] += 1
    elif grade_list[grade] >=90:
        cutline[1] +=1
    elif grade_list[grade] >=80:
        cutline[2] +=1
    elif grade_list[grade] >=70:
        cutline[3] +=1
    elif grade_list[grade] >=60:
        cutline[4] +=1
    elif grade_list[grade] >=50:
        cutline[5] +=1
    elif grade_list[grade] >=40:
        cutline[6] +=1
    elif grade_list[grade] >=30:
        cutline[7] +=1
    elif grade_list[grade] >=20:
        cutline[8] +=1
    elif grade_list[grade] >=10:
        cutline[9] +=1
    elif grade_list[grade] >0:          #0이 입력되면 끝나야하고 출력값이 없어야 해서 0 초과
        cutline[10] +=1


for x in range(0,11):           # 점수대별 출력
    if cutline[x] != 0:
        print(100-10*x,":",cutline[x],"person")

