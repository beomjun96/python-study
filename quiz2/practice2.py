class Employee:
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = nai
    
    def pay(self):
        pass

    def data_print(self):
        pass

    def irumnai_print(self):
        pass

class Regular(Employee):
    def __init__(self,irum, nai, salary):
        super().__init__(irum, nai)
        self.salary = salary

    def __str__(self):
        return "이름:{}, 나이:{}, 월급{}".format(self.irum, self.nai, self.salary)

class Salesman(Regular):
    def __init__(self,irum,nai,salary,sales,commission):
        super().__init__(irum, nai, salary)
        self.sales = sales
        self.commission = commission

    def __str__(self):
        return "이름:{}, 나이:{}, 수령액:{}".format(self.irum, self.nai, int(self.salary + self.sales*self.commission))

class Temporary(Employee):
    def __init__(self,irum,nai, ilsu, ildang):
        super().__init__(irum, nai)
        self.ilsu = ilsu
        self.ildang = ildang


    def __str__(self):
        return "이름:{}, 나이:{}, 월급:{}".format(self.irum, self.nai, self.ilsu * self.ildang)



t=Temporary("홍길동", 25, 20, 15000)
s=Regular("한국인", 27, 3500000)
u=Salesman("손오공", 29, 1200000, 5000000, 0.25)    

print(t)
print(s)
print(u)
