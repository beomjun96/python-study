string, num1 = input("문자열(100자 이하)과 정수를 입력해주세요:").split()
num1 = int(num1) # 정수로 변환

if len(string)>100:
    print("100자가 넘습니다. 다시입력해주세요.")
else :
    print(string.replace(string[num1-1],"")) # 해당위치 문자 제거

#반복문으로 그 문자만 제거해서 풀 수 있음.

