# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최소값을 찾는 프로그램을 작성하시오.
# 예를 들어 M=60, N=100이 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로,
# 이들 소수의 합은 620이고, 최소값은 61이 된다.

def is_prime(n):                    # 소수 찾기
    for i in range(2, n):
        if ( n%i == 0 ):
            return False
    return True


M , N = map(int, input("자연수 2개 입력:").split())
sum = 0
min = N                             # 가장 큰 수를 min으로 설정해 다른 수랑 차례로 비교해서 최솟값 찾기

for x in range(M,N+1):
    if is_prime(x) == True:
        if x < N:
            min = x
            break                   # 첫번째 소수가 최소값이므로 반복문 바로 나오기.

for x in range(M,N+1):
    if is_prime(x) == True:
        sum = sum + x

print("이들 소수의 합은 {}이고, 최소값은 {}이 된다.".format(sum,min))
