# 복싱체급은 몸무게가 50.80kg 이하를 Flyweight 61.23kg 이하를 Lightweight, 72.57kg 이하를 Middleweight, 88.45kg 이하를 Cruiserweight, 88.45kg 초과를 Heavyweight라고 하자.

# 몸무게를 입력받아 체급을 출력하는 프로그램을 작성하시오.

# 입력 예: 87.3

# 출력 예: Cruiserweight

weight = float(input("몸무게 소수점 두자리까지 입력해주세요:"))

if weight <=50.80:          # 50.80kg보다 작을 때
    print("Flywight")
elif weight <=61.23:          # 50.80kg보다 크고 61.23kg보다 작을 때
    print("Lightweight")
elif weight <=72.57:          # 61.23kg보다 크고 72.57kg보다 작을 때
    print("Middleweight")
elif weight <= 88.45:          # 72.57kg보다 크고 88.45kg보다 작을 때
    print("Cruiserweight")
else:                        #  88.45k보다 클 때
    print("Heavweight")

