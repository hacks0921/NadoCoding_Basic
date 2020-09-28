# (1:22:31) 5-1.리스트
# (1:31:35) 5-2.사전
# (1:40:46) 5-3.튜플
# (1:43:19) 5-4.세트
# (1:48:44) 5-5.자료구조의 변경
# (1:50:47) 5-6.퀴즈 #4
################################################################################
# (1:22:31) 5-1.리스트
# 지하철 칸별로 10명,20명,30명
# subway = [10,20,30]
#
# subway = ["유재석", "박명수", "조세호"]
# subway.append("하하")
# print(subway.index("조세호")+1)  # 인덱스가 어디 인지 확인
# print(subway)
# subway.insert(1, "정형돈")  # 원하는 위치에 추가 가능
# print(subway)
# print(subway.pop()) # 뒤에 있는 사람을 한명씩 꺼냄
# print(subway.count("유재석"))   #같은 이름이 몇개 있는지 확인

# num_list = [5,4,3,1,2]
# num_list.sort() # 순서
# print(num_list)
# a= num_list
# print(a)
# num_list.sort(reverse=True) # 순서
# print(num_list)
# b= num_list
# print(a,b)

# num_list.reverse()  # 순서 뒤집기
# print(num_list)
#
# mix_list = ["조세호",20,True]  # 글자, 숫자, 블리안 모두 가능
# print(mix_list)
#
# num_list.extend(mix_list) # 리스트를 합치기
# print(num_list)

################################################################################
# (1:31:35) 5-2.사전

# cabinet = {3:"유재석", 100:"김태호"}

# print(cabinet[3])
# print(cabinet[5])  # 프로그램 에러 발생
# print(cabinet.get(3))
# print(cabinet.get(5),"사용가능") # None으로 나오고 진행 가능
#
# print(3 in cabinet)  # True
# print(5 in cabinet)  # False
#
# cabinet = {"a-3":"유재석", "b-100":"김태호"}
# print(cabinet)
# print(cabinet["a-3"])
# print(cabinet["b-100"])
#
# cabinet["a-3"] ="김종국" # dictionary에 추가
# cabinet["c-20"] ="조세호" # dictonary에 추가
# print(cabinet)
#
#
# #key 출력
# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items())
#
# print(cabinet)
# del(cabinet['a-3'])  --> key를 기준으로 삭제
# print(cabinet)
#
# #목욕탕 폐점  전체 삭제
# cabinet.clear()
# print(cabinet)

################################################################################

# (1:40:46) 5-3.튜플

# menu = ("돈까스","치스까스") # 안바뀌는 데이터
# print(menu[0])
# print(menu[1])
#
# name = "김종국"
# age = 20
# hobby ="코딩"
# print(name,age,hobby)
# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name,age,hobby)

##################################################################
# (1:43:19) 5-4.세트
# my_set = {1,2,3,3,3}
# print(my_set)
#
# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석","박명수"])
#
# # 교집합 (java python을 모두 할수 있는 개발자
# print(java & python)
# print(java.intersection(python))   # 교집합
#
# # 합집합
# print(java | python)
# print(java.union(python))
#
# # 차집합
# print(java - python)
# print(java.difference(python))
#
# #python 할줄아는 사람
# python.add("김태호")
# print(python)
#
# java.remove("김태호")
# print(java)
######################################################################
# (1:48:44) 5-5.자료구조의 변경
# menu = {"커피","우유","주스"}
# print(menu, type(menu))
#
# menu = list(menu)
# print(menu, type(menu))
#
# menu = tuple(menu)
# print(menu, type(menu))
#
# menu = set(menu)
# print(menu, type(menu))

################################################################################
# (1:50:47) 5-6.퀴즈 #4

# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,1))

from random import *
users = range(1, 21)
print(type(users))
print(users)
users = list(users)  # 리스트로 만들어줌
print(type(users))
print(users)
shuffle(users)
print(users)
winners = sample(users,4) #4명중에 1명은 치킨 3명은 커피
print("치킨 당첨자: {}".format(winners[0:3]))
print("커피 당첨자: {}".format(winners[1:]))
