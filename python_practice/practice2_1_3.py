string, num1 = input("문자열과 정수를 입력해주세요:").split()
num1 = int(num1)

if len(string)<=num1 :
    print(string[::-1])
else :
    print(string[len(string)-1:len(string)-(num1+1):-1])