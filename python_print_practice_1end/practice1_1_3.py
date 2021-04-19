num1, num2 = map(int, input("숫자 2개를 입력해주세요:").split()) #변수 한번에 입력 받고 정수로 받기


print(num1,">",num2,"---", int(num1>num2))  #그냥 비교연산자 쓰면 True, False 로 출력되서 자료형을 int로 바꾸니 1,0 으로 출력됨
print(num1,"<",num2,"---", int(num1<num2))
print(num1,">=",num2,"---", int(num1>=num2))
print(num1,"<=",num2,"---", int(num1<=num2))