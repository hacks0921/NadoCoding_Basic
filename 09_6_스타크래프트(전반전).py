# (4:23:50) 9-10.스타크래프트 프로젝트 전반전
# (4:33:47) 9-11.스타크래프트 프로젝트 후반전
# (4:44:42) 9-12.퀴즈 #8

#####################################
'''일반유닛'''
class Unit:   ## 부모 Class
    def __init__(self, name, hp, speed):  # 마린,탱크는 객체 (인스턴스)
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{} 유닛이 생성되었습니다".format(name))

    def move(self, loaction):
        print("[지상유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, loaction, self.speed))

    def damaged(self, damage):
        print("{0}:{1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp<=0:
            print("{0}: 파괴되었습니다.".format(self.name))


class AttackUnit(Unit):  ## 자식 Class
    def __init__(self, name, hp, speed, damage ):
        Unit.__init__(self, name, hp, speed )  # Unit Class에서 Name, HP를 상속 받는다
        self.damage = damage

    def attack(self, location):
        print("{0}:{1} 방향으로 적군을 공격합니다. [공격력 {2}]"
              .format( self.name, location, self.damage))


class Flyable:  #날수있는 기능
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, loaction):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2} ]"
              .format(name, loaction, self.flying_speed))

## 공중 유닛 # 다중 상속
class FlayableAttactUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, flying_speed, damage ):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중유닛이동]")
        self.fly(self.name, location)

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)
#스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가 , 체력 10 감소
    def stimpack(self):
        if self.hp>10:
            self.hp -=10
            print("{0} : 스팀팩을 사용합니다".format(self.name))
        else:
            print("{0} :체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

class Tank(AttackUnit):
    size_developed = False

    def __init__(self):
        AttackUnit.__init__(self,"탱크",150,1,35)
        self.size_mode = False

    def set_size_mode(self):
        if Tank.size_developed == False:
            return
        # 현재 시스모드가 아닐떄 --> 시즈모드
        if Tank.size_mode == False:
            print("{0} : 시즈모드로 전환합니다". format(self.name))
            self.damage *=2
            self.size_mode == True

        else:
            print("{0} : 시즈모드로 해제 합니다". format(self.name))
            self.size_mode == False

class Wraith(FlayableAttactUnit):
    def __init__(self):
        FlayableAttactUnit.__init__("레이스",80 ,20 ,5)
        self.clocked = False #클로킹 모드 해제 상태

    def clocking(self):
        if self.clocked == True:
            print("{} : 클로킹 모드 해제 합니다".format(self.name))
        else:
            print("{} : 클로킹 모드 설정 합니다".format(self.name))
            self.clocked = True