num1, num2, num3 = map(int,input("정수 3개를 입력해주세요:").split())

if num1>num2 and num1>num3 :   #첫 번째 수 num1이 가장 커야함
    print("True")
else :
    print("False")

if num1==num2==num3 :         #세 수가 모두 같아야함
    print("True")
else :
    print("False")