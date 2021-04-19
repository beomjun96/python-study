# 년도를 입력받아 윤년(leap year)인지 평년(common year)인지 판단하는 프로그램을 작성하시오.
# 400으로 나누어떨어지면 윤년이다. 또는 4로 나누어떨어지고 100으로 나누어떨어지지 않으면 윤년이다. 나머지는 모두 평년이다.
# 입력 예: 2008
# 출력 예: leap year

year = int(input("년도를 입력해주세요:"))

if year%400 == 0:
    print("leap year")
elif year%100!=0 and year%4 ==0:
    print("leap year")
else:
    print("common year")