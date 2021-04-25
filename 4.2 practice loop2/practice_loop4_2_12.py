# 복호화 키와 암호 문자를 입력으로 받아 원문을 구하는 프로그램을 구현하시오. 복호화 키는 26개의 소문자로 주어지며, a,b,c,d... 를 순서대로 복호화 키 문자로 대치한다는 것을 뜻한다.
# 예를 들어, 복호화 키가 "eydbkmiqugjxlvtzpnwohracsf" 와 같이 주어진다고 하자,

# 그러면 이는 다음과 같다 - a 문자는 e, b 문자는 y, ..., z 문자는 f로 바꿔줌.

# 암호화 된 문자는 대소문자 혹은 공백이 올수 있고 대소문자는 대문자로 소문자는 소문자로 치환 규칙에 맞게 출력하고 ,

# 공백문자는 그대로 출력한다.

# 입력 예:

# eydbkmiqugjxlvtzpnwohracsf

# Kifq oua zarxa suar bti yaagrj fa xtfgrj

# 출력 예:

# Jump the fence when you seeing me coming

key = input("키 입력(소문자):")
string = input("암호문 입력:")
alph = "abcdefghijklmnopqrstuvwxyz"
idx = 0

string_len = len(string)
if len(key) == 26:
    for x in key:
        if x not in alph:
            print("소문자로만 입력해주세요.")
            break
    for i in range(0,string_len):
        if string[i].isupper==True:                 #여기가 문제인거 같음
            word=string[i].lower()
            if word in alph:
                num= alph.find(word)
                key_num=key[num]
                print(key_num.upper(),end='')
            elif string[i] ==' ':
                print(" ", end="")
        else:
            if string[i] in alph:
                num= alph.find(string[i])
                print(key[num],end='')
            elif string[i] ==' ':
                print(" ", end="")


else:
    print("26개가 안맞습니다.")
