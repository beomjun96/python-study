# 소수(prime number)란 1보다 큰 자연수 중 1과 자기 자신 두 개만을 약수로 갖는 수를 말한다.
# 자연수 M과 N을 입력받아 M부터 N까지 소수의 개수를 구하여 출력하는 프로그램을 작성하시오.
# M이상 N이하의 자연수 중 소수가 몇 개인지 구하여 출력한다.
# 입력 예: 10 100
# 출력 예: 21
def is_prime(n):
    for i in range(2, n):
        if ( n%i == 0 ):
            return False
    return True


num1, num2 = map(int, input("자연수 2개 입력:").split())
count=0

for x in range(num1, num2+1):
    if is_prime(x) == True:         #num1부터 num2 까지 대입해서 소수면 카운트 증가
        count +=1
print(count)
    
