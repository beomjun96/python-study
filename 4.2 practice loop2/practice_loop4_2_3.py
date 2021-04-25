# 자연수 n을 입력받아 "출력 예"와 같이 공백으로 구분하여 출력되는 프로그램을 작성하시오.
# 입력: 3
# 1 2 3 
#   4 5 
#     6 

num = int(input("정수를 입력하시오:"))
count = 1
for i in range(0, num):
    print(' '*i, end='')
    for j in range(num,i,-1):
        print(count,end='')
        count += 1
    print()