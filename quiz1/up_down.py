# 1~100 사이의 숫자를 하나 생성하고, 사용자가 정답을 맞추는 프로그램
# 몇 회만에 정답을 맞췄는지 출력

import random
land_num = random.randint(1,100)
user_num = -1
count = 0

while land_num != user_num:
    user_num = int(input("숫자 입력>"))
    if user_num <= 100:
        if land_num > user_num:
            print("더 큰수를 입력하세요:")
            count += 1
        elif land_num == user_num:
            print("정답입니다!!, {}번 만에 맞추셨습니다.".format(count))
            count +=1
            break
        else:
            print("더 작은 수를 입력하세요:")
            count += 1
        

    else:
        print("1~100 사이의 숫자를 골라주세요.")
        continue
