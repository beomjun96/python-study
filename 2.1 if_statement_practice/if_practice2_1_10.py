# 공백을 포함한 문자열을 입력받아 각 단어로 분리하여 문자열 배열에 저장한 후 입력순서의 반대 순서로 출력하는 프로그램을 작성하시오. 문자열의 길이는 100자 이하이다.
# 입력 예: C++ Programing jjang!!
# 출력 예:
# jjang!!
# Programing
# C++

str_list = input("100자 이하 문자열을 입력해주세요:").split()
str_list_len = len(str_list)

#리스트 각각의 인덱스에 저장된 값 합치고 길이가 100이하인지 확인
if len(' '.join(str_list)) <= 100:  
    for i in range(str_list_len,0,-1):
# 길이가 리스트의 인덱스 끝번보다 1 크기때문에 -1해준다.
        print(str_list[i-1])


else:
    print("100자가 넘습니다. 다시 입력해주세요")