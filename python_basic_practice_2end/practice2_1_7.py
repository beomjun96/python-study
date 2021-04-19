s1, s2, num = input("문자열").split() #문자열 2개 정수 입력받음
num = int(num) # num 자료형이 문자형이므로 정수로 바꿔줌

if num>=1 and len(s2)<=100 : #1개 이상 입력받고 2번째 문자열은 100이하로 받아야함
    ts1 = s1+s2 # 문자열 2개 연결
    ts2 = s1[0:num] + s2[num:] #A는 입력받은 정수까지, B는 입력받은 정수부터 출력되어 합쳐짐
print(ts1)
print(ts2)