# 3개의 정수를 입력받아 조건문을 이용하여 입력받은 수들 중 최소값을 출력하는 프로그램을 작성하시오.
# 입력 예: 18 -5 10
# 출력 예: -5

'''
num1, num2, num3 = map(int, input("숫자 세개 입력하세요:").split())

#num1이 가장 큰 수 일때
if num1>=num2 and num2>=num3:
    print(num3)
elif num1>=num2 and num2<=num3:
    print(num2)

#num2가 가장 큰 수 일때
if num2>=num1 and num1>=num3:
    print(num3)
elif num2>=num1 and num1<=num3:
    print(num2)

#num3이 가장 큰 수 일때
if num3>=num1 and num1>=num2:
    print(num2)
elif num3>=num1 and num1<=num2:
    print(num1)

'''
############## 이렇게 구하면 세 숫자가 모두 같을 때, 
#num2, num3이 num1 보다 작을 때 다른 값도 나옴

num1, num2, num3 = map(int, input("숫자 세개 입력하세요:").split())
num_min =0

if num1 < num2:
    num_min = num2
    num2 = num1
    num1 = num_min

if num1 < num3:
    num_min = num3
    num3 = num1
    num1 = num_min

if num2 < num3:
    num_min = num3
    num3 = num2
    num2 = num_min

print(num3)

# 제일 작은 수를 한쪽으로 옮기면서 최종적으로 num3이 제일 작게 만들기