# 1~12사이의 정수를 입력받아 평년의 경우 입력받은 월을 입력받아 평년의 경우 해당 월의 날수를 출력하는 프로그램을 작성하시오.
# 평년의 경우 1월부터 12월까지 일수는 각각 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31일이다.
# 입력 예: 2
# 출력 예: 28

'''
month_day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = int(input("달(month)를 입력하세요:"))
print(month_day_list[month-1])
'''

month = int(input("달(month)를 입력하세요:"))

if month ==1 :
    print("31")
elif month == 2:
    print("28")
elif month == 3:
    print("31")
elif month == 4:
    print("30")
elif month == 5:
    print("31")
elif month == 6:
    print("30")
elif month == 7:
    print("31")
elif month == 8:
    print("31")
elif month == 9:
    print("30")
elif month == 10:
    print("31")
elif month == 11:
    print("30")
elif month == 12:
    print("31")