# 10개의 정수를 입력받아 100 미만의 수 중 가장 큰 수와 100 이상의 수 중 가장 작은 수를 출력하는 프로그램을 작성하시오.
# List 데이터 구조를 활용하시오.
# 입력 예: 88 123 659 15 443 1 99 313 105 48
# 출력 예: 99 105

num_list = list(map(int,input("10개 정수 입력:").split()))          # 왜 map(int,input().split()) 헸는데 리스트에 정수로 안들어갈까?
under = []                                  # 100미만 수
up = []                                     # 100이상 수

for x in  range(0,10):                      # num_list 모든 인덱스 확인.
    if num_list[x]<100:                     # 100보다 작으면 under에 추가
        under.append(num_list[x])
    else:                                   # 100이상이면 up에 추가
        up.append(num_list[x])


big = under[0]                              # big에 under 0번 저장
small = up[0]                               # small에 up 0번 저장

for x in under:                             # under 리스트 다 비교해서 가장 큰 값 big에 저장
    if big < x:
        big = x
for y in up:                                # up 리스트 다 비교해서 가장 작은 값 저장
    if small > y:
        small = y

print(big, small)

