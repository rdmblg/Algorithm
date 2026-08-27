# infile = open("새 텍스트 문서.txt","r")
# infile.close()
#r은 읽기모드, 파일의 처음부터 읽기
#w는 쓰기모드, 파일의 처음부터 쓰고 파일이 없으면 생성, 존재하면 기존 내용은 지워짐
#a는 추가모드, 파일의 끝에 쓰고 없으면 생성
#r+는 읽기와 쓰기 모드, 모드를 변경하려면 seek()가 호출되어야함

# infile = open("새 텍스트 문서.txt", "r", encoding="utf-8") #현재 작업 폴더의 phones.txt파일을 읽기 용도로
# #d드라이브의 루트 폴더에 있는 파일을 열려면
# #oepn("d:/새 텍스트 문서.txt", "r")
# lines = infile.read()
# #infile.read(10)하면 10개 문자만 읽음
# print(lines)
# #오류 났을 시 encoding="utf-8" 넣기

# infile.seek(0)
# #파일의 포인터를 맨 처음으로 다시 돌려놓음
# lines = infile.readlines()
# #readline()으로 읽으면 리스트로, 파일의 한 줄 내용이 리스트 각 항목(문자열)으로
# print(lines)

# infile.seek(0)

# for line in infile:
# #파일의 첫 번째 줄부터 끝까지 한 줄씩 자동으로 line변수에 할당
#   line = line.rstrip()
# #rstrip()은 문자열 우측의 \n을 삭제(줄바꿈 기호 삭제)
#   print(line)
# infile.close()

# outfile = open("새 텍스트 문서1.txt", "w", encoding="utf-8")

# outfile.write("홍길동 010-1234-5678\n")
# outfile.write("김철수 010-1234-5679\n")
# outfile.write("김영희 010-1234-5680\n")

# outfile.close()

# outfile = open("새 텍스트 문서.txt", "a", encoding="utf-8")

# outfile.write("엉뎅이\n")
# outfile.write("엉덩이\n")
# outfile.write("궁뎅이\n")

# outfile.close()

# text = "속담을, 저장한, 파일"
# result = text.split()
# print(result)

# infile = open("망고조아.txt","r", encoding="utf-8")

# for line in infile:
#   line = line.rstrip()
#   word_list = line.split()
#   for word in word_list:
#     print(word)
# infile.close()
#split 띄어쓰기 기준으로 문자열을 나눔
#나눈 문자열 항목으로 리스트를 만듦

#입력 파일 이름과 출력 파일 이름을 받는다.
# infilename = input("입력 파일 이름:")
# outfilename = input("출력 파일 이름:")

# #입력과 출력을 위한 파일을 연다.
# infile = open(infilename, "r", encoding="utf-8")
# #입력으로 파일을 받는다
# outfile = open(outfilename, "w", encoding="utf-8")
# #출력으로 새 파일을 만든다, 파일이 있으면 덮어 씌운다

# #전체 파일을 읽는다.
# s = infile.read()

# #전체 파일을 쓴다.
# outfile.write(s)

# #파일을 닫는다.
# infile.close()
# outfile.close()

#텍스트 파일만이 들어 있는 디렉토리에서 실행해야함
#1번 버전
# import os
# arr = os.listdir()
# #listdir 디렉토리(폴더)안에 있는 모든 파일과 폴더의 이름을 리스트 형태로 가져옴

# for f in arr:
#   infile = open(f, "r", encoding="utf-8")
# #arr디렉토리 안에 있는 파일들을 순서대로 연다
#   for line in infile :
#     #열린 파일들의 내용을 하나하나 확인한다.
#     e = line.rstrip()
#     if "Python" in e :
#       print(f, ":", e)
#       #만약 파일들의 내용들에 파이썬이라는 글자가 있으면 프린트한다. 파일명, 줄 명
#   infile.close()


# #2번 버전
# import os
# arr = os.listdir()
# #listdir 디렉토리(폴더)안에 있는 모든 파일과 폴더의 이름을 리스트 형태로 가져옴

# for f in arr:
#   if os.path.isfile(f): #추가됨, 폴더를 제외한 파일만을 대상으로 처리 
#     #is file?하고 물어보는 것 맞으면 True, 아니면 False를 뱉어냄
#     infile = open(f, "r", encoding="utf-8", errors="ignore")
# #erros="ignore"을 추가하면 인코딩 오류가 나는 문자를 적당히 넘겨줌
# #arr디렉토리 안에 있는 파일들을 순서대로 연다
#     for line in infile :
#     #열린 파일들의 내용을 하나하나 확인한다.
#       e = line.rstrip()
#       if "Python" in e :
#         print(f, ":", e)
#       #만약 파일들의 내용들에 파이썬이라는 글자가 있으면 프린트한다. 파일명, 줄 명
#   infile.close()

# import csv #csv모듈을 불러옴
# #csv 파일에 저장된 데이터를 가져올 때 csv.reader()을 사용
# #파일을 한 줄씩 읽어서 리스트(List)형태로 반환해줌

# f = open('csv.csv', encoding="utf-8") #csv파일을 열어서 f에 저장
# data = csv.reader(f) #reader() 함수를 이용하여 읽기
# #header = next(data) #헤더를 제거한다.
# for row in data :
#   print(row)
# f.close()

# import csv

# f = open('파일명.csv', encoding="utf-8")
# data = csv.reader(f)
# header = next(data)

# temp = 1000
# #그냥 임의의 변수 저장해놓고 온도가 걔보다 높을리는 없으니까 하나하나 비교해가면서 최저 온도 찾는거임
# for row in data :
#   if temp > float(row[3]):
#     temp = float(row[3])
# print(temp)
# f.close()