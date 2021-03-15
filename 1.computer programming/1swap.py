'''
두 변수 안의 값을 버꾸기
'''
number1 = 10
number2 = 20

print(number1) #10
print(number2) #20

number3 = number1
number1 = number2
number2 = number3

print(number1) 
print(number2) 

# ??????
# number1 = 20
# number2 = 10

# print('변경 후')
# print(number1) #20
# print(number2) #10

'''
number1, number2 = number2, number1 도 스왑가능함
