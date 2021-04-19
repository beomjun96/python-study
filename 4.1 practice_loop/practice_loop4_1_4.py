# 아래와 같이 나라 이름을 출력하고 숫자를 입력받아 해당하는 나라의 수도를 출력하는 작업을 반복하다가 해당하는 번호 이외의 숫자가 입력되면 "none"라고 출력한 후 종료하는 프로그램을 작성하시오.
# 각 나라의 수도 :
# 대한민국 = 서울(Seoul)
# 미국 = 워싱턴(Washington)
# 일본 = 동경(Tokyo)
# 중국 = 북경(Beijing)
# 예시 입력 예:

# Korea
# USA
# Japan
# China number? 1
# 출력 예: Seoul

# Korea
# USA
# Japan
# China number? 5
# none

num= 1
while 1<= num and num <=4:
    print("1. Korea")
    print("2. USA")
    print("3. Japan")
    print("4. China")
    num = int(input("number?"))
    if num == 1:
        print("Seoul")
    elif num== 2:
        print("Washington")
    elif num==3:
        print("Tokyo")
    elif num ==4:
        print("Beijing")
    else:       # 1,2,3,4 외 입력받을 때
        print("none")
        break    # 반복문 나가기
    