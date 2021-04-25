# 10개의 정수를 입력받아 리스트에 저장한 후 짝수 번째 입력된 값의 합과 홀수 번째 입력된 값의 평균을 출력하는 프로그램을 작성하시오.
# 평균은 반올림하여 소수첫째자리까지 출력한다.
# 입력 예: 95 100 88 65 76 89 58 93 77 99
# 출력 예:
# sum : 446
# avg : 78.8

num_list = list(map(int,input("10개 정수 입력:").split())) 

even_sum = 0
odd_sum = 0
count = 1

for x in num_list:
    if count%2 == 1:
        odd_sum = odd_sum + x
        count += 1
    else:
        even_sum = even_sum + x
        count += 1

avg = odd_sum/5

print("sum:",even_sum)
print("avg:",round(avg,1))

