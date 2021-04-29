# 컴퓨터가 0~9 사이의 숫자 3개를 중복되지 않게 선택
# 숫자야구
# ex) 컴퓨터가 선택한 숫자 : 207
#     사용자가 선택한 숫자 : 527
#     결과 1strike 1ball 1out
import random
strike = 0
ball = 0
out = 0

user_num = []
com_num = []

for i in range(0,3):
    com_num.append(random.randint(0,9))                             # set을 쓰던, for로 len == 3 이 되던 해서 중복성 빼야함. 주말에 


while out <= 999:
    
    if strike != 3:
        user_num = list(map(int,input("0~9 사이의 숫자 3개를 중복되지 않게 선택:").split()))
        strike = 0
        ball = 0
        out = 0
        for i in range(0,3):
            for j in range(0,3):
                if i == j:                          # 위치가 같을 때
                    if user_num[i] == com_num[j]:   # 위치가 같고 값도 같을때
                        strike += 1
                        break
                elif i != j:                        
                    if user_num[i] == com_num[j]:   # 위치가 다르지만 같은 숫자가 있을 때
                        ball +=1
                        break
            if strike == 0 and ball ==0:
                out += 1
        print("{} strike {} ball {} out".format(strike, ball, out))       



    else:
        print("게임승리!!")
        break

        
    
