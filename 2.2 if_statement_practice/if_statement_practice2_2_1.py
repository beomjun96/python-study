# "FizzBuzz"문제
#    1에서 100까지의 숫자를 출력하되,
#    만약 해당 숫자가 '3'으로 나누어지면 숫자 대신에 "Fizz"를 출력하고,
#    만약 해당 숫자가 '5'로 나누어지면 숫자 대신에 "Buzz"를 출력하며,
#   만약 해당 숫자가 '3'과 '5'로 모두 나누어지면 숫자 대신에 "FizzBuzz"를 출력
# 입력 예1: 5
# 출력 예1: "Buzz"
# 입력 예2: 3
# 출력 예2: "Fizz"
# 입력 예3: 15
# 출력 예3: "FizzBuzz"

num = int(input("1~100까지의 숫자를 입력:"))

if num <= 100:
# 3이랑 5로 동시에 나눠져야하므로 나머지가 0
    if num%3 ==0 and num%5 ==0:
        print("FizzBuzz")
    elif num%3 ==0:
        print("Fizz")
    elif num%5 ==0:
        print("Buzz")

else:
    print("1~100까지의 수를 입력해주세요:")