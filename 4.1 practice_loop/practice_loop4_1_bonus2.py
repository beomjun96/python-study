# 아래와 같은 모양으로 출력하는 프로그램을 작성하시오.
# 사용자에게 숫자를 입력받아 입력 받은 높이 만큼의 삼각형을 출력하시오.
# 입력 예: 5
# *****
#  ****
#   ***
#    **
#     *

num = int(input("정수를 입력하시오:"))

for line in range(num,0,-1):
    print(" "*(num-line) + "*"*line)
