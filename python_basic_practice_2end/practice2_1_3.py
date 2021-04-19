string, num1 = input("문자열과 정수를 입력해주세요:").split()
num1 = int(num1)

if len(string)<=num1 :
    print(string[::-1]) # 정수보다 문자열길이가 작으면 문자열 전체를 거꾸로 출력
else :
    print(string[:len(string)-(num1+1):-1]) # 끝부터 입력받은 숫자만큼 뒤에서부터 출력