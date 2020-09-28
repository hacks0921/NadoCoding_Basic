# (1:57:33) 6-1.if
# (2:05:08) 6-2.for
# (2:09:33) 6-3.while
# (2:14:59) 6-4.continue 와 break
# (2:19:11) 6-5.한 줄 for
# (2:22:51) 6-6.퀴즈 #5


# (1:57:33) 6-1.if
# weather =input("오늘 날씨는 어떄요???")
# if weather =="비" or weather =="눈":
#     print("우산을 챙기세요")
# elif weather =="미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

# temp = int(input("기온은 어떄요?"))
# if 30 <= temp:
#     print("너무 더워요, 나가지 마세요")
# elif 10 <= temp and temp <30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요 나가지마세요")

# (2:05:08) 6-2.for

# for waitting_no in [0, 1, 2, 3, 4]:
#     print("대기번호: {0}".format(waitting_no))
# for waitting_no in range(1,5+1):
#     print("대기번호: {0}".format(waitting_no))
#
# starbucks = ["아이언맨","토르","아이엠그루트"]
# for customer in starbucks:
#     print( "{}, 커피가 준비되었습니다.".format(customer))
#

# (2:09:33) 6-3.while

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0},커피가 준비되었습니다 {1}번 남았어요".format(customer,index))
#     index -=1
#     if index == 0:
#         print("커피가 폐기되었습니다.")

############################################################################

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0},커피가 준비되었습니다 호출{1}회".format(customer, index))
#     index +=1

############################################################################

# customer ="토르"
# person = "unknown"
#
# while person != customer:
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")

# (2:14:59) 6-4.continue 와 break

# absent =[2,5] # 결석
# for student in range(1,11): #1,2,3,4,5,6,7,8,9,10
#     if student in absent:  # absent리스트 안에 sutden 리스트가 있는지 있는지 확인
#         continue
#     print("{0},책을 읽어봐".format(student))
#
############################################################################

# absent = [2, 5]  # 결석
# no_book =[7]
# for student in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
#     if student in absent:  # absent리스트 안에 sutden 리스트가 있는지 있는지 확인
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지.{0}는 교무실로 따라와".format(student))
#         break
#     print("{0},책을 읽어봐".format(student))


############################################################################
# (2:19:11) 6-5.한 줄 for

# # 출석 번호가 1,2,3,4 앞에 100을 붙이기로 함 -->101,102,103,104
# student = [1,2,3,4,5]
# print(student)
# student = [i+100 for i in student]
# print(student)
#
# # 학생 이름을 길이로 변환
# student =["Iron man", "Thor", "I am Grouth"]
# student = [len(i) for i in student]
# print(student)
#
# # 학생 이름을 대문자로 변환
# student =["Iron man", "Thor", "I am Grouth"]
# student = [i.upper() for i in student]
# print(student)

########퀴즈5########
# 조건1: 승객별 운행 소요시간은 5~50분 난수
# 조건2: 소요시간 5~15분 사이에 승객만 매칭
# (출력문 예제)
# [0] 1번쨰 손님 (소요시간: 15분)
# [ ] 1번쨰 손님 (소요시간: 15분)
# [0] 1번쨰 손님 (소요시간: 15분)
# ...

# from random import *
# cnt = 0
# for i in range(5,51):  #1~50이라는 정소
#     time = randrange(5,51)
#     if 5 <= time < 15:  # 5~15분 이내 손님 탑승 승객수 증가 처리, 매칭 성공
#         print("[0]{0}번째 손님 (소요시간: {1}분".format(i,time))
#         cnt +=1
#     else: # 매칭 실패
#         print("[ ]{0}번째 손님 (소요시간: {1}분".format(i,time))
# print("총 탑승 승객: {0}분".format(cnt))
#
