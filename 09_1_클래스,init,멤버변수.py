# (3:38:08) 9-1.클래스
# (3:47:04) 9-2._init_
# (3:48:34) 9-3.멤버변수
# (3:53:07) 9-4.메소드
# (3:59:29) 9-5.상속
# (4:02:54) 9-6.다중상속
# (4:10:08) 9-7.메소드 오버라이딩
# (4:17:03) 9-8.pass
# (4:19:31) 9-9.super
# (4:23:50) 9-10.스타크래프트 프로젝트 전반전
# (4:33:47) 9-11.스타크래프트 프로젝트 후반전
# (4:44:42) 9-12.퀴즈 #8

########################################################################
# (3:38:08) 9-1.클래스
########################################################################

# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음


# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력
#
# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력{1}\n".format(hp,damage))
#
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
#
# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력{1}\n".format(tank_hp,tank_damage))
#
# def attarck(name, location, damage):
#     print("{} : {}방향으로 적군을 공격합니다. [공격력 {}]".format(
#             name, location, damage))
#
# attarck(name, "1시", damage)
# attarck(tank_name, "1시", tank_damage)

'''일반유닛'''
class Unit:
    def __init__(self, name, hp, damage):  # 마린,탱크는 객체 (인스턴스)
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40,5)
# marine2= Unit("마린", 40,5)
# marine3 = Unit("마린", 40,5)
#
# tank= Unit("탱크", 150,35)
# wraith1 = Unit("레이스", 80, 5)
#
# print("유닛이름: {}, 공격력 :{}".format(wraith1.name, wraith1.damage))
#
# # 마인드 컨트롤 : 상대방 유닛을 내것으로 만드는 것(빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80,5)
# wraith2.clocking = True
#
# if wraith2.clocking == True:
#     print("{}는 현재 클로킹 상태 입니다.".format(wraith2.name))

# if wraith1.clocking == True:
#     print("{}는 현재 클로킹 상태 입니다.".format(wraith1.name))

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0}:{1} 방향으로 적군을 공격합니다. [공격력 {2}]"
              .format( self.name, location, self.damage))
    def damaged(self, damage):
        print("{0}:{1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp<=0:
            print("{0}: 파괴되었습니다.".format(self.name))


firebat1 = AttackUnit("서종학",50,20)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)


########################################################################
# (3:59:29) 9-5.상속
########################################################################