# 나이를 입력받아 20살 이상이면 "adult"라고 출력하고 그렇지 않으면 몇 년후에 성인이 되는지를 "○ years later"라는 메시지를 출력하는 프로그램을 작성하시오.
# 입력 예: 18
# 출력 예: 2 years later

age = int(input("나이를 입력해주세요:"))

if age>=20:
    print("adult")
else :
    print(20-age,"years later")