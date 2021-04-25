# icecream 딕셔너리에서 최소 가격의 아이스크림 이름을 출력하라.

icecream = {'Tankboy': 1200, 'Ppangppare': 1800, 'Worldcorn': 1500, 'Melona': 1000}

min = min(icecream.values())

for x in icecream:
    if icecream.get(x) == min:
        print(x)