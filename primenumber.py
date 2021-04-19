# 소수 구하기
'''
num1 = int(input("숫자를 입력해주세요 :"))
x=0

for num2 in range(1,num1+1): # num1+1해야 자기 자신까지 반복함.
    if num1%num2 == 0:
        x += 1
if x==2:
    print("소수입니다.")
'''


# 교수님께서 알려주신것.
# False 랑 True 쓸 때 앞에 무조건 대문자로 써야함.
def is_prime(n):
    for i in range(2, n):
        if ( n%i == 0 ):
            return False
    return True
n = int(input("정수를 입력하시오: "))
print(is_prime(n))