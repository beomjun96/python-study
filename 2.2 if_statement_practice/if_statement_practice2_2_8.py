# 다음의 결과와 같이 입력된 문자가 대문자일 경우 소문자로, 소문자일 경우 대문자로 변경하고,
# 알파벳이 아닐 경우엔 그냥 출력하는 코드를 작성하십시오.
# 입력 예1: A
# 출력 예1: a
# 입력 예2: 가나다
# 출력 예2: 가나다

word = input("문자 입력:")
large = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
small = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

if word in large:               #대문자 list에 있는지
    chgnum = large.index(word)  #word의 대문자 list 인덱스 번호 찾기
    print(small[chgnum])        #인덱스 번호 small에서 출력
elif word in small:
    chgnum = small.index(word)
    print(large[chgnum])
else:
    print(word)