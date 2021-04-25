# 10개의 정수를 입력받아 리스트에 저장한 후 내림차순으로 정렬하여 출력하시오.
# 입력 예: 95 100 88 65 76 89 58 93 77 99
# 출력 예: 100 99 95 93 89 88 77 76 65 58

num_list = list(map(int,input("10개 정수 입력:").split())) 

# num_list.sort(reverse=True)

# print(num_list)

def sort(list_a):
    small = []
    equal = []
    bigger = []

    if len(list_a) > 1:
        idx = list_a[0]
        for x in list_a:
            if x < idx:
                small.append(x)
            elif x == idx:
                equal.append(x)
            elif x > idx:
                bigger.append(x)
        return sort(bigger)+equal+sort(small)           #이부분이 이해가 안됨
    else:
        return list_a

print(sort(num_list))