# (2:28:36) 7-1.함수
# (2:30:09) 7-2.전달값과 반환값
# (2:37:50) 7-3.기본값
# (2:41:32) 7-4.키워드값
# (2:43:07) 7-5.가변인자
# (2:47:55) 7-6.지역변수와 전역변수
# (2:53:58) 7-7.퀴즈 #6

################################################################

################################################################
# (2:28:36) 7-1.함수
# def open_account():
#     print("새로운 계좌 생성")
#
# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {}원 입니다.". format(balance+money))
#     return balance+money
#
# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {}원 입니다.".format(balance-money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {}원 입니다.".format(balance))
#         return balance
#
# def withdraw_night(balance, money):
#     commision = 100
#     return commision, balance-money-commision
#
# balance = 0
# balance = deposit(balance, 1000)
# commision, balance = withdraw_night(balance, 500)
# print(commision, balance)
# print("수수료 {}원이며, 잔액은 {}원 입니다.".format(commision,balance))

################################################################
# (2:37:50) 7-3.기본값
################################################################
# def profile(name, age, lang):
#     print("이름: {0}\t,나이: {1}\t,주 사용 언어: {2}"
#           .format(name,age, lang))
#
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")
#
# def profile(name, age=17, lang="파이썬"):
#     print("이름: {0}\t,나이: {1}\t,주 사용 언어: {2}"
#           .format(name,age, lang))
#
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")
# profile("서종학")
#
# profile("문재인", lang="하하하", age = 25)

# def profile(name, age, lang1,lang2, lang3, lang4, lang5):
#     print("이름:{}, 나이{}".format(name,age), end="")
#     print(lang1, lang2, lang3, lang4, lang5)
#
# profile("유재석", 20, "파이썬", "c++", "C", "CCC", "xx")

#
# def profile(name, age, *langage):  ### 가변 인자
#     print("이름:{}, 나이{}  ".format(name, age), end="")
#     for lang in langage:
#         print(lang +"\t" , end="")
#     print()
#
# profile("유재석", 20, "파이썬", "c++", "C", "CCC", "xx")
#
################################################################
# (2:47:55) 7-6.지역변수와 전역변수 (어디서든지)
################################################################
#
# gun = 10
# def checkpoint(soldiers): #경계근무
#     # gun = 20
#     global gun # 전역 공간에 있는 gun을 사용 하겠음
#     gun = gun - soldiers  # 10-2 = 8
#     print("[함수내] 남은 총: {0}".format(gun))
#
# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers  # 10-2
#     print("[함수내] 남은 총: {0}".format(gun))
#     return gun
#
# print("전체총:{0}".format(gun))
# checkpoint(2)
# print(gun)
# gun = checkpoint_ret(gun,2)
# print("남은총:{}".format(gun))


################################################################
# (2:53:58) 7-7.퀴즈 #6
################################################################

def std_weight(hegiht, gender):
    if gender =="남자":
        return hegiht*hegiht*22
    else:
        return hegiht*hegiht*21


hegiht = 175
gender = "남자"
weight = round(std_weight(hegiht/100, gender),2)
print("키 {0}cm {1}의 표준체중은 {2}kg 입니다.".format(hegiht, gender, weight))
