# 두 개의 정수를 입력받아 두 정수 사이(두 정수를 포함)에 3의 배수이거나 5의 배수인 수들의 합과 평균을 출력하는 프로그램을 작성하시오.
# 평균은 반올림하여 소수 첫째자리까지 출력한다.
# 입력 예: 10 15
# 출력 예: sum : 37 avg : 12.3

num1, num2 = map(int, input("두개 정수 입력:").split())
sum = 0
count = 0
temp =0

if num1 > num2:         # num2 가 더 큰수로 치환
    temp = num1
    num1 = num2
    num2 = temp

while num1 <= num2:     # num2까지 반복
    if num1%3==0 or num1%5==0:
        sum = sum + num1    # 3, 5 배수 인 수 합
        count += 1          # 평균 구할 때 몇개 더했는지 확인
    num1 += 1

avg = sum/count

print("sum: {} avg: {}".format(sum, round(avg,1)))
    
