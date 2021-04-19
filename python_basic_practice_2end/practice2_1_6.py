# while로 반복해서 문자열을 받고 if로 20개 이하로 제한 한 후 거르면서 10개 받기
# string 0~9까지 저장 될거
# endswith(끝나는문자, 문자열의시작, 문자열의끝)로 끝나는 단어 찾아 참, 거짓으로 출력
# 참 거짓을 if로 확인해서 참만 출력

'''
num = 1
strlist = []
while num <= 10:
    string = input("문자열을 입력해주세요.")
    if len(string) <= 20:
        strlist.append(string) #strlist에 길이가 20보다 작은 문자열 추가
        print(strlist[num-1],"이(가)입력되었습니다.") #
        num=num+1
    else:
        print("20자가 넘습니다. 다시 입력해주세요.")


word = input("검색할 끝 문자를 입력해주세요:")
for x in range(10):
    if strlist[x].endswith(word):  #strlist의 리스트 0 번부터 9번까지 입력된 단어의 끝부분이 문자(word) 같으면 참
        print(strlist[x])
        '''

        
num = 1
strlist = []
while num <= 10:
    string = input("문자열을 입력해주세요.")
    if len(string) <= 20:
        strlist.append(string) #strlist에 길이가 20보다 작은 문자열 추가
        print(strlist[num-1],"이(가)입력되었습니다.") 
        num=num+1
    else:
        print("20자가 넘습니다. 다시 입력해주세요.")


word = input("검색할 끝 문자를 입력해주세요:")
for x in range(10):
    if strlist[x][-1] == word:  #strlist의 리스트 0 번부터 9번까지 입력된 단어의 끝부분이 문자(word) 같으면 참
        print(strlist[x])