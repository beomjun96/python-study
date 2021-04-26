# 사용자에게 base문자열을 첫 줄에 입력받고, 다음으로 찾고자하는 문자 1개를 입력받아 문자열 내의 검색 문자의 모든 위치를 출력하는 프로그램을 작성하시오.
# 첫 번째 위치는 0번이며 리스트에 없는 문자가 입력되면 "none" 라는 메시지를 출력하고 끝내는 프로그램을 작성하시오.
# 예제: "my name is dean" 을 base 문자열로 입력하고, 찾고자 하는 문자를 'd'로 입력하면 11을 출력해주면 된다.
# 만약, 찾으려는 문자가 2개 이상인 경우에는 모든 위치를 출력해준다.


base = input("입력 문자열:")
word = input("찾고 싶은 문자:")

index = 0
count = 0
for x in base:
    if x == word:
        print(index, end=" ")
        count =+ 1
    index +=1

if count ==0:
    print("none")
