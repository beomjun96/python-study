string = input("문자열을 입력해주세요:")

if len(string)>100:  #문자열 길이 100이하
    print("100자가 넘습니다. 다시입력해주세요.")
else :
    print(string*2) #문자열 두번 반복