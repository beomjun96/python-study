# 2진수를 입력받아 10진수로 변환하여 출력하는 프로그램을 작성하시오.
# 입력 예: 10101
# 출력 예: 21

num = input("2진수 입력:")
sum = 0
lenth = len(num)-1                  # 2**0 까지 계산해야함.

for x in num:
    sum= sum  + int(x)*2**lenth
    lenth -= 1
print(sum)