# 다음 표 를 딕셔너리로 구성하라, 아이스크림의 이름은 딕셔너리의 "key"이고
# 희망 가격과 남은 수량은 리스트로 구성한 후 딕셔너리의 'value'로 사용하라.

icecream_list = {'Melona': [1000, 10],'Pollapo': [1200, 7],'Ppangppare' :[1800, 6],'Tankboy': [1200, 5], 'Hothunting':[1200, 4], 'Worldcorn': [1500, 3]}

icecream = input("아이스크림 이름:")
print(icecream_list[icecream])