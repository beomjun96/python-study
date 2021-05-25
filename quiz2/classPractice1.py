class Machine():
    def __init__(self, cupCount = 1):
        self.cupCount = cupCount

    def showData(self):
        if self.cupCount == 0:
            print("can't not divide with 0.")
        
        else:
            if culcChangeCulc >= 0:
                print("커피 {}잔과 잔돈 {}원".format(self.cupCount, culcChangeCulc))

            else:
                print("요금이 부족합니다(커피 한잔에 200원)")


class CoinIn():
    def __init__(self, coin):
        self.coin = coin
        self.change = None  # 돈을 넣을 때 거스름돈을 입력하지 않고 계산 후 출력만 받음

    def culc(self, cupCount):
        self.cupCount = cupCount
        self.change = self.coin - self.cupCount * 200
        return self.change



while True:
    coin = int(input("코인을 입력하세요:"))
    cup = int(input("몇 잔을 원하세요:"))

    culcChange = CoinIn(coin)
    culcChangeCulc = culcChange.culc(cup)

    machineShow = Machine(cup)
    machineShow.showData()

    word = input("다시 입력하시겠습니까? (Stop: 'n' or 'N')")
    if word == "n" or word =="N":
        break
