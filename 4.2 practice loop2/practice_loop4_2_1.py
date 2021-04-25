# 1부터 100까지의 정수 중 한 개를 입력받아 100 보다 작은 배수들을 차례로 출력하다가 10 의 배수가 출력되면 프로그램을 종료하도록 프로그램을 작성하시오.
# 입력 예: 7
# 출력 예: 7 14 21 28 35 42 49 56 63 70

num = int(input("정수를 입력:"))
count = 1
out =1

if num >= 1 and num<=100:           # 1~100 정수 한개인지 확인
    while out <100 and out%10!=0:   # 배수가 100보다 작을때 까지 출력하다가 10의 배수면 멈춤.
        out = num * count           # 배수 출력
        if out>100:                 # 배수가 100보다 크면 종료
            break
        print(out, end=" ")
        count += 1

else:
    print("1~100 정수를 입력해주세요.")
    


# num = int(input("정수를 입력:"))
# mul =1 

# for x in range(1,11):
#     if mul <100:
#         mul = num * x
#         if mul > 100:
#             break
#         print(mul, end=" ")
#         if mul%10 == 0:
#             break
