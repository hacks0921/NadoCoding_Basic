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
# (3:59:29) 9-5.상속
########################################################################
#
# '''일반유닛'''
# class Unit:   ## 부모 Class
#     def __init__(self, name, hp):  # 마린,탱크는 객체 (인스턴스)
#         self.name = name
#         self.hp = hp
#
# class AttackUnit(Unit):  ## 자식 Class
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)  # Unit Class에서 Name, HP를 상속 받는다
#         self.damage = damage
#
#     def attack(self, location):
#         print("{0}:{1} 방향으로 적군을 공격합니다. [공격력 {2}]"
#               .format( self.name, location, self.damage))
#     def damaged(self, damage):
#         print("{0}:{1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
#         if self.hp<=0:
#             print("{0}: 파괴되었습니다.".format(self.name))
#
#
# firebat1 = AttackUnit("서종학",50,20)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)


########################################################################
# (4:02:54) 9-6.다중상속
########################################################################


'''일반유닛'''
class Unit:   ## 부모 Class
    def __init__(self, name, hp):  # 마린,탱크는 객체 (인스턴스)
        self.name = name
        self.hp = hp

class AttackUnit(Unit):  ## 자식 Class
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)  # Unit Class에서 Name, HP를 상속 받는다
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


class Flyable:  #날수있는 기능
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, loaction):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2} ]".format(name, loaction, self.flying_speed))

## 공중 유닛 # 다중 상속 
class FlayableAttactUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_spped):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_spped)

# 발키리 : 공중 유닛, 한번에 14발 미사일 발사
valkyrie = FlayableAttactUnit("발키리", 200,5,6)
valkyrie.fly(valkyrie.name, "3시")

# FlayableAttactUnit("레이스", 100, 10, 3)
#
# firebat1 = AttackUnit("서종학",50,20)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)
