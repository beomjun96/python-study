# 100 이하의 두 개의 정수를 입력받아 작은 수부터 큰 수까지 차례대로 출력하는 프로그램을 작성하시오.
# 입력 예: 5 10
# 출력 예: 5 6 7 8 9 10

num1, num2 = map(int, input("두개 정수 입력:").split())


if num1 <= 100 and num2<= 100:          # 두 수가 100이하여야 함.
    if num1 < num2:
        for x in range(num1, num2+1):
            print(x, end=" ")

    if num1 == num2:
        print("두 수가 같습니다.")
    
    if num1 > num2:
        for x in range(num2,num1+1):
            print(x, end=" ")
 
    
else:
    print("다시 입력해주세요.")


