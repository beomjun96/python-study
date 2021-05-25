class Unit():
    def __init__(self, rank, size, life):
        self.name = self.__class__.__name__     #클래스 이름 호출하기
        self.rank = rank
        self.life = life
        self.size = size

    def show_status(self):
        print("이름: {}\n등급: {}\n사이즈: {}\n라이프: {}".format(self.name, self.rank, self.size, self.life))




class Goblin(Unit):
    def __init__(self, rank, size, life, attack_type, damage):
        super().__init__(rank, size, life)
        self.attack_type = attack_type
        self.damage = damage

    def show_status(self):
        super().show_status()
        print("공격 타입: {}".format(self.attack_type))
        print("데미지: {}".format(self.damage))

    def attack(self):
        print("[{}]이 공격합니다! 상대방 데미지({})".format(self.name, self.damage))

class SphereGoblin(Goblin):
    def __init__(self, rank, size, life, attack_type, damage, sphere_type):
        super().__init__(rank, size, life, attack_type, damage)
        self.sphere_type = sphere_type

    def show_status(self):
        super().show_status()
        print("창 타입: {}".format(self.sphere_type))



class Hero(Unit):
    def __init__(self, rank, size, life, goblins = None):       #고블린을 리스트로 받는지는 잘 모르겠음 문제는 그러니까...이렇게 품
        super().__init__(rank, size, life)
        if goblins == None:     # 고블린이 없다면 공백으로 둠
            self.goblins = []
        
        else:
            self.goblins = goblins

    # 영웅이 소유한 고블린 출력
    def show_own_goblins(self):
        numOfGoblins = []
        numOfSphereGoblins = []
        for i in self.goblins:
            if isinstance(i, Goblin) == True:      # class안에 있는지 확인해서 True False 출력
                numOfGoblins.append(i)

        for j in self.goblins:
            if isinstance(j, SphereGoblin) == True:
                numOfSphereGoblins.append(j)

        print("현재 영웅이 소유한 고블린은 {}명, 창 고블린은 {}명입니다.".format(len(numOfGoblins)-len(numOfSphereGoblins), len(numOfSphereGoblins)))       #창 고블린이 고블린에 포함이 되서 고블린 수 구할때 창고블린 빼줌


    # 영웅이 소유한 고블린 총 공격
    def make_goblins_attack(self):
        for i in self.goblins:
            i.attack()      # 고블린 이름에서 attack 호출

    # 새로운 고블린 추가하기
    def add_goblins(self, new_goblins):
        for i in new_goblins:           # 한번에 담긴 리스트 고블린 입력 받으면 list' object has no attribute 'attack' 에러 뜸
            if i not in self.goblins:    # 고블린 리스트에 같은 이름의 새로운 고블린이 없으면 추가
                self.goblins.append(i)

            else:
                print("이미 추가된 고블린입니다.")

    # 기존 고블린 지우기
    def remove_goblins(self, old_goblins):
        for j in old_goblins:
            if j in self.goblins:    # 고블린 리스트에 같은 이름의 고블린이 있으면 삭제
                self.goblins.remove(j)

            else:
                print("소유하고 있지 않은 고블린입니다.")


# 고블린 오브젝트 생성
goblin_1 = Goblin("병사", "Small", 100, "근접 공격", 15)
goblin_2 = Goblin("병사", "Small", 100, "근접 공격", 15)
sphere_goblin_1 = SphereGoblin('병사', 'Small', 100, '레인지 공격', 10, '긴 창')
        
# 영웅 오브젝트 생성 후, 고블린 오브젝트 할당       
hero_1 = Hero("영웅", "Big", 300, [goblin_1, goblin_2, sphere_goblin_1])

print("# 새로운 고블린 추가 전")
hero_1.show_own_goblins()
hero_1.make_goblins_attack()

# 새로운 고블린 생성
goblin_3 = Goblin("병사", "Small", 100, "근접 공격", 20)
sphere_goblin_2 = SphereGoblin("병사", "Small", 100, "레인지 공격", 5, "긴 창")

# 새로운 고블린 추가
hero_1.add_goblins([goblin_3, sphere_goblin_2])

print("\n# 새로운 고블린 추가 후")
hero_1.show_own_goblins()
hero_1.make_goblins_attack()

# 추가한 고블린 삭제
hero_1.remove_goblins([goblin_3, sphere_goblin_2])

print("\n# 추가한 고블린 삭제 후")
hero_1.show_own_goblins()
hero_1.make_goblins_attack()

# 영웅에게 소유되지 않은 고블린 생성
goblin_4 = Goblin("병사", "Small", 100, "근접 공격", 20)

# 이미 소유한 고블린 추가
print("\n# 에러 메세지 발생")
hero_1.add_goblins([goblin_1])
hero_1.remove_goblins([goblin_4])
