# 삼각형의 높이 N을 입력받아서 아래와 같이 문자 'A'부터 차례대로 왼쪽 대각선으로 채워서 삼각형 모양을 출력하는 프로그램을 작성하시오.
# 입력 예 : 5
#         A
#       B F
#     C G J
#   D H K M
# E I L N O

print(ord("A"))   # A 아스키코드 65

askcode1 = 65
askcode = 65
a_askcode = 65
count = 0

num = int(input("정수를 입력하시오:"))
num_count = num-1


for i in range(1, num+1):
    print(' '*(num-i),end='')

    # 첫번째 영어
    print(chr(askcode),end='')
    fill_askcode = askcode + num_count
    # 첫번째 영어 이후 채우기
    for j in range(0,count):
        print(chr(fill_askcode),end="")
        num_count -= 1
        fill_askcode = fill_askcode + num_count
        

    num_count = num-1
    count += 1           
    askcode += 1
    a_askcode = askcode
    
    print()
