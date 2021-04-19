# 정수를 계속 입력받다가 100 이상의 수가 입력이 되면 마지막 입력된 수를 포함하여 합계와 평균을 출력하는 프로그램을 작성하시오.
# 평균은 반올림하여 소수 첫째자리까지 출력한다.

num=0
sum=0
count = 0
while num <100:                              # 100이상 받으면 마지막 입력 된 수 포함하여 계산
    num= int(input("정수를 입력하시오."))     # 정수 입력 받기
    sum = sum + num
    count += 1

avg = sum/count
print(round(avg,1))