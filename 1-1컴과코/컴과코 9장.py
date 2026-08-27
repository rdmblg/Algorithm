#컴과코 9장
#리스트

#리스트 mylist = [10, 20, 30, 40, 50]
#튜플 myTuple = (10, 20, 30, 40, 50)
#딕셔너리 myDict = {1:"one", 2:"two",3:"three"}
#세트 mySet = {"one", "two", "three"}

#리스트 선언
#list = [] 대괄호 안에 데이터를 나열, 데이터와 데이터는 쉼표로 분리
#빈 리스트 생
#리스트 출력
#print(list)


friend = ["궁딩이", "방딩이", "엉덩이", "엉뎅이"]
print(friend)


#리스트 항목 접근하기
#인덱스 사용
#인덱스 0부터 1,2
letter = ['A','B','C']
print(letter[0])
print(letter[1])
print(letter[2])

#리스트 길이(항목 개수)
#len()
print(len(letter))

s = "Hello World!"
print(len(s))

#리스트의 길이보다 더 큰 인덱스를 사용하면 오류남

#in 연산자
#어떤 값이 리스트 내부에 있는지 확인
print('A' in letter)
print('D' in letter)

print('D' not in letter)

#in 연산자는 문자열에서 특정 문자열이 있는지 검사하는데도 사용
print('e' in 'Hello')

#리스트 방문
#리스트에서 가장 중요한 작업은
#리스트에 저장된 데이터를 하나씩 꺼내서 어떤 처리를 하는 것

for i in letter:
    print(i)

#인덱스를 사용하여 항목들을 꺼낼 수도 있음

for i in range(len(letter)) :
    print(letter[i])
#len(letter)가 만약 3이면 코드는 range(3)이 되는데 이 때 0,1,2라는 묶음을 만들어냄
#letter[0], letter[1], letter[2]
#len으로 전체 개수를 알아낸 다음 range를 이용해 0부터 개수-1까지의 인덱스 명단을 뽑아냄

#리스트 항목 교체
letter[1] = 'BB'

print(letter)

#리스트 추가하기
letter.append("D")
print(letter)
s
#리스트 중간에 추가하기
letter.insert(1,"B")
print(letter)

#. 점의 의미
#파이썬에서 모든 것은 객체이다
#객체 안에 있는 무엇인가를 사용할때는
#객체의 이름을 쓰고 점(.)을 붙인 후에 함수의 이름을 적는다.
#letter.append("바보")

#항목 삭제하기
#리스트에서 항목 삭제
#remove() pop()
#remove(항목) pop(인덱스)

letter.remove("BB")
print(letter)
#remove에서 항목을 삭제할 때는 첫번째 항목이 삭제됨

letter.pop(3)
print(letter)

#지우고자 하는 항목이 없다면 프로그램이 오류를 발생
if "A" in letter:
    letter.remove("A")
print(letter)

#항목 삭제하기
#인덱스 0에서 있는 항목을 삭제하고 변수에 저장
x = letter.pop(0)
print(letter)
#리스트 0에 있는 값을 빼내서 x에 저장

y = letter.remove("C")
print(letter)

#리스트 탐색하기(인덱스 찾기)
letter.append("A")
letter.append("B")
letter.append("C")
print(letter)

if "A" in letter:
    x = letter.index("A")

print(x)

#리스트 합치기
former = ["D", "E"]
print(former + letter)
print(letter * 2)

#슬라이싱
#리스트에서 한 번에 여러 개의 항목을 추출하는 기법
print(letter[0:2])
#0부터 2-1까지

#인덱스 생략
print(letter[:2])
#처음부터 2-1까지

print(letter[1:])
#1부터 끝까지

print(letter[:])
#처음부터 끝까지

#내장 함수
#min 리스트에서 최소값을 찾는다
#max 리스트에서 최대값을 찾는다
#sum 리스트 안의 값들의 합계를 반환한다
print(min(letter))
print(max(letter))
#문자열은 사전에 나온 순서대로 비교

#리스트 정렬하기
#변수명.sort()
numbers = [9, 6, 7, 1, 8, 4, 5, 3, 2]
print(numbers)
numbers.sort()
print(numbers)

#정렬된 새로운 리스트가 필요하면 sorted(변수명) 이용
new_list = sorted(numbers)
print(new_list)

new_list = numbers.sort()
print(new_list)

#리스트 정렬하기
new_list = sorted(numbers, reverse = True)
print(new_list)

letter.sort(reverse = True)
print(letter)

#통계치 계산하기
import statistics
listt = [2, 3, 3, 4, 5, 5, 5, 5, 6, 6, 6, 7]
print(f"입력 리스트={listt}")
print(f"평균={sum(listt)/len(listt)}")
print(f"평균={statistics.mean(listt)}")
print(f"중간값={statistics.median(listt)}")
print(f"최빈값={statistics.mode(listt)}")
print(f"표준편차={statistics.stdev(listt)}")

#딕셔너리
#딕셔너리에는 값과 관련된 키가 있다
phone = {"홍채운" : "바보", "도해연" : "1345", "정진희" : "1456"}
#구분 괄호
#리스트 []
#딕셔너리 {}
#키 : 값

print(phone["홍채운"])

#딕셔너리에서 값 변경
phone["홍채운"] = '히히'
print(phone["홍채운"])

#딕셔너리에서 동적으로 항목 추가
pay={}

pay["바보"]='1234'
pay["궁딩이"]='1235'
pay["궁뎅이"]='1236'
print(pay)

#딕셔너리의 모든 키 출력하기
print(pay.keys())
print(pay.values())
print(pay.items())

#리스트 vs 딕셔너리
#키 = 인덱스

#딕셔너리 항목 방문
for i in sorted(pay.keys()):
    print(i, pay[i])
#i는 정렬된 key, pay[i]는 키에 맞는 값
#sorted는 정렬된 값, 키 순서, 궁뎅이 궁딩이 바보 순

#딕셔너리 항목 삭제
pay.pop("궁뎅이")
print(pay)

pay.clear()
print(pay)

#d.get(key, default)
#주어진 키를 가지고 값을 찾는다. 만약 없으면 default 값이 반환된다.

#편의점 재고 관리
import sys
listt = {"커피음료":"7", "펜":"3", "종이컵":"2", "우유":"1", "콜라":"4", "책":"5"}

while True :
    product = input("물건의 이름을 입력하시오: ")
    if product in listt :
        print(listt[product])
    elif product == "":
        print("종료")
        break   
    else :
        print("재고가 없습니다.")

#영한사전
listtt = {"one":"하나", "two":"둘", "three":"셋"}

while True :
    han = input("단어의 이름을 입력하시오(eng): ")
    if han in listtt :
        print(listtt[han])
    elif han == "":
        print("종료")
        break
    else :
        print("사전에 없습니다.")


dicto = {}

dicto["one"] = "하나"
dicto["two"] = "둘"
dicto["three"] = "셋"

while True:
    answer = input("단어를 입력하시오: ")
    if answer in dicto :
        print(dicto[answer])
    elif answer == "" :
        print("종료")
        break
    elif answer not in dicto :
        print("사전에 없습니다")
        y = input("단어를 추가하시겠습니까?")
        if y == "yes" :
            z = input("입력하실 영어 단어를 얘기해주세요")
            x = input("입력하실 영어 단어의 뜻을 얘기해주세요")
            dicto[z] = x
        else :
            print("종료")
            break

#딕셔너리에 키가 있는지 확인하려면 in연산자 사용
num = {"하나":1,"둘":2,"셋":3}
print('하나'in num)
print("스물"in num)

#일정 애플리케이션
dictt = {}

while True :
    x = input("날짜를 입력하시오: ")
    if x == "": break #아니이게돼?
    elif x not in dictt :
        y = input("일정을 입력하시오: ")
        dictt[x] = y
    else :
        print("올휴")
print(dictt)


#연습문제 1장
listt = []
y = 0
while len(listt) < 5:
    x = int(input("정수를 입력하시오: "))
    listt.append(x)
    
for i in range(len(listt)):
    y += listt[i] #리스트 인수 불러올 때는 대괄호 쓰기

print(y)


#연습문제 2장
counters = [0, 0, 0, 0, 0, 0]
import random

for i in range(1000):
    value = random.randint(0, 5)
    counters[value] = counters[value] + 1

for i in range(len(counters)):
    #print(f"주사위가 {i}인 경우는", str(counters[i]) + "번")
    print(f"주사위가 {i}인 경우는 {counters[i]}번")


#연습문제 3장
contacts = {}

while True :
    name = input("(입력모드)이름을 입력하시오: ")
    if not name : #변수가 비어있다면
        break
    tel = input("전화번호를 입력하시오: ")
    contacts[name] = tel

y = input("(검색모드)이름을 입력하시오: ")
if y in contacts :
    print(y ,"의 전화번호는" ,contacts[y], "입니다.")


#연습문제 4장
domains = {"kr" : "대한민국", "us" : "미국", "jp" : "일본", "de" : "독일", "sk" : "슬로바키아"}

for k, v in domains.items():
    print(k,": ", v)
"""

#연습문제 5장
problems = {"파이썬" : "최근에 가장 떠오르는 프로그래밍 언어", "홍채운" : "바보", "궁딩이" : "궁뎅이", "엉덩이" : "엉뎅이"}

for word in problems.keys():
    print(f"다음은 어떤 단어에 대한 설명일까요?\n{problems[word]}")
    answer = input("(1)파이썬 (2)홍채운 (3)궁딩이 (4)엉덩이\n")
    if word == answer :
        print("정답입니다!")
    else :
        print("당신은 바보입니다. ㅉ")






