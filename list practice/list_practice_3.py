# 빈 리스트을 선언하고 정수를 차례로 입력받다가 0 이 입력되면 0 을 제외하고 그 때까지 입력된 정수를 가장 나중에 입력된 정수부터 차례대로 출력하는 프로그램을 작성하시오.
# 입력 예:
# 3
# 5
# 10
# 55
# 0
# 출력 예: 55 10 5 3

binlist = []
idx = 1

while idx !=0:
    idx = int(input("입력:"))
    if idx ==0:
        break
    binlist.append(idx)

print(binlist[::-1])