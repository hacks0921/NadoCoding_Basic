# (2:58:59) 8-1.표준입출력
# (3:10:12) 8-2.다양한 출력포맷
# (3:17:45) 8-3.파일입출력
# (3:26:27) 8-4.pickle
# (3:30:22) 8-5.with
# (3:33:33) 8-6.퀴즈 #7

##############################################################
# (2:58:59) 8-1.표준입출력
# 시험성적
# scores = {"수학":0, "영어":50,"코딩":100}
# for subject, score in scores.items():
#     # print(subject,score)
#     print(subject.ljust(8),str(score).rjust(4)) # 8개 공간 확보후 왼쪽 정렬, 4개 공간 확보후 오른쪽 정렬

# 대기 순번표
# 001,002,003,004...
# for num in range(1,21):
#     print("대기번호: ", str(num).zfill(3)) #3크기만큼 공간 확보
#
# answer = input("아무값이나 입력하세요:")
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")

# 사용자 입력으로 입력을 받으면 모두 str으로 된다


##############################################################
# (3:10:12) 8-2.다양한 출력포맷
##############################################################
# 빈자리는 빈공간으로 두고 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0:>10}".format(500))  #
# print("{0:>10}".format(-500))  #
# # 양수일때는 + 표시, 음수일떄는 -표시
# print("{0:>+10}".format(500))
# print("{0:>+10}".format(-500))
# # 왼쪽 정렬하고, 빈공간으로_채움
# print("{0:_<+10}".format(500))
# print("{0:_<10}".format(500))
# #3자리마다 콤마를 찍어주기
# print("{0:,}".format(10000000))
# #3자리마다 콤마를 찍어주기
# print("{0:+,}".format(10000000))
# print("{0:+,}".format(-10000000))
# print("{0:,}".format(-10000000))
# #3자리 마다 콤마 직어주기, 부호도 붙이고, 자리수 확보하기
# # 돈이 많으면 행복하니 빈자리는 ^표시로 채워주기
# print("{0:^<+30,}".format(10000000000))
# #소숫점 출력
# print("{0:f}".format(5/3))
# #소숫점 특정 자리수까지 출력 ->소숫점 3째 자리에서 반올림
# print("{0:.2f}".format(5/3))

##############################################################
# (3:17:45) 8-3.파일입출력
##############################################################

# score_file = open("score.txt","w", encoding="utf8")
# print("수학: 0", file=score_file)
# print("영어: 50", file=score_file)
# score_file.close()

# score_file = open("score.txt","a",encoding="utf8")  # a : append 계속해서 추가
# score_file.write("과학: 80")
# score_file.write("\n코딩: 80")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())   #전체 다 읽어오기
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) # 줄별로 읽기, 한줄일고 커서는 다음줄로 이동
# print(score_file.readline()) # 줄별로 읽기, 한줄일고 커서는 다음줄로 이동
# print(score_file.readline()) # 줄별로 읽기, 한줄일고 커서는 다음줄로 이동
# print(score_file.readline()) # 줄별로 읽기, 한줄일고 커서는 다음줄로 이동
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()


# score_file = open("score.txt","r",encoding="utf8")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close()

##############################################################
# (3:26:27) 8-4.pickle
##############################################################

import pickle
# profile_file = open("profile.pickle","wb") #wb 바이너리 파일
# profile =  {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle")
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)

##############################################################
# (3:30:22) 8-5.with
##############################################################
# import pickle
#
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")
# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

# 파일 퀴즈
# X 주차 주간보고
# 부서:
# 이름:
# 업무 요약 :
#
# 1~50주차까지 보고서 파일 생성 프로그램

# for i in range(1,5):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as f:
#         f.write("-{0} 주차 주간보고 - ".format(i))
#         f.write("\n부서:")
#         f.write("\n이름:")
#         f.write("\n업무 요약")
