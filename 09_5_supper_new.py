# (4:19:31) 9-9.super
class Unit:
    def __init__(self):
        print("Unit 생성자")
class Flayable:
    def __init__(self):
        print("Flayable 생성자")
class FlayableUnit(Unit,Flayable):
    def __init__(self):
        super().__init__()  # 앞에 있는 Class 호출된다 , self정보 안보내도됨
        # Flayable.__init__(self)
        # Unit.__init__(self)

dropship = FlayableUnit()