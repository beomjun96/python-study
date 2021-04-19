# 0 이상의 정수들이 공백으로 구분되어 반복적으로 주어진다. 0이 입력되면 반복문을 멈추고 그 전까지 입력받은 수들에 대하여 홀수의 개수와 짝수의 개수를 출력하는 프로그램을 작성하시오.
# 입력 예: 9 7 10 5 33 65 0
# 출력 예: odd : 5 even : 1
'''
num = 1
odd=0
even =0
while num == 0:
    num=input().split()    # 계속~ 입력 받을 텐데 우짜지
    num = 
'''

num = list(map(int, input("정수를 입력:").split()))
odd=0
even=0
ln = 0

while num[ln] != 0:
    if num[ln]%2 ==0:
        even +=1
    else:
        odd +=1
    ln +=1
print("odd:{} even:{}".format(odd, even))

# 공백으로 구분되어 입력받는데 0이 입력되면 멈추기 어떻게 하는지 물어보기
# 공백으로 받기가 split 밖에 안되는거 같은데 모르겠음.