# 초를 입력 받아서 시간과 분으로 변환하는 프로그램을 작성하시오.
# 입력 예: 3598
# 출력 예: 59분 58초

second = int(input("초를 입력해주세요:"))
minute = 0
hour = 0


if second>=0 and second%1==0:       # 초니까 0보다 커야하고 정수로 입력받아야함. > 양의 정수
    while second > 3600:           
        second = second -3600
        hour += 1                   # 시간 증가

    while second >60:
        second = second -60
        minute += 1                 # 분 증가
    print("제대로된 초를 입력해 주세요.")

print('{}시간 {}분 {}초'.format(hour,minute,second))  #format 순서대로 시분초 들어감.