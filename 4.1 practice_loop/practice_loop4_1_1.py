# for 문을 이용하여 1부터 입력받은 정수까지의 합을 구하여 출력하는 프로그램을 작성하시오.
# 100 이하의 양의 정수만 입력된다.
# 입력 예: 10
# 출력 예: 55

num = int(input("정수 입력:"))
sum =0

for i in range(num+1):
    sum = sum + i
print(sum)