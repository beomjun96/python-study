# 10개의 정수를 입력받아 그 중 가장 작은 수를 출력하는 프로그램을 작성하시오.
# 입력 예: 5 10 8 55 6 31 12 24 61 2
# 출력 예: 2

num_list = list(map(int,input("10개정수 입력:").split()))

min = num_list[0]

for x in num_list:
    if x < min:
        min = x

print(x)