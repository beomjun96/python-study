class Machine:
    def __init__(self, cupCount=1):
        self.cupCount = cupCount

    def showData(self):
        return


class CoinIn(Machine):
    def __init__(self, cupCount ,coin, change):
        super().__init__(cupCount)
        self.coin = coin
        self.change = change
        if self.cupCount == 0:
            print("can't not divide with 0.")
            

        
    def culc(self, cupCount):
        super().cupCount = cupCount
        cof_price = 200
        if super().cupCount * cof_price >= self.coin:
            self.change = super().cupCount*cof_price - self.coin
            return self.change

        else:
            return "요금이 부족합니다.(커피 한잔에 200원"


word = 0
while word!="n" or word!="N":
    coin = int(input("코인을 입력하세요:"))
    cup = int(input("몇 잔을 원하세요:"))

    input_data = CoinIn()
    print(input_data.culc())


    word = input("다시 입력하시겠습니까? (Stop: 'n' or 'N')")

