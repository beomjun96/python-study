# 2진수를 10진수로 

binary = input("2진수 입력:")
sum = 0
lenth = len(binary)-1


for x in binary:
    sum= sum  + int(x)*(2**lenth)
    lenth -= 1
print(sum)