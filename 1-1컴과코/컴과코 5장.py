#컴과코 5장

#3가지의 기본 제어 구조
#순차 구조 : 명령들이 순차적으로 실행됨
#선택 구조 : 둘 중 하나의 명령을 선택하여 실행
#반복 구조 : 동일한 명령이 반복되면서 실행

#if - else문
#조건식이 참이면 문장1을 실행, 거짓이면 문장2 실행
#조건식 오른쪽에 콜론 : 이 위치
#문장1과 문장2는 무조건 들여쓰기를 해야함 tab, shift + tab 활용, 들여쓰기 정도가 동일해야함

#if 조건식 :
# 문장1
#else :
# 문장2
"""
x = int(input("점수: "))
if x >= 60 :
    print("합격")
else :
    print("불합격")


#예제
x = int(input("정수:"))

if x % 2 == 0 :
    print("짝수")
else :
    print("홀수")

score = 90
if score >= 90 :
    print("합격")
    print("장학금 받을수있당!!!!!!!!")
#여러 개의 문장을 실행할 수 있고 이를 블록이라함, 블록 내의 문장은 들여쓰기가 동일해야

#영화 나이 제한 검사
print("안녕하세요? 두근두근 영화관입니다.")
age  = int(input("나이 :"))

if age >= 15 :
    print("이 영화를 보실 수 있습니다.")
else :
    print("이 영화를 보실 수 없습니다.")

#논리 연산자
#and 모두 참이면 참
#or 하나만 참이면 참
#x가 참이면 거짓, 거짓이면 참

#윤년 판단
x = int(input("연도: "))

if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0) :
    print(f"{x}년은 윤년입니다.")
else :
    print("윤년이 아닙니다.")

#동전 던지기 게임
import random
print("동전 던지기 게임을 시작합니다.")
x = random.randrange(2)
if x == 0 :
    print("앞면입니다.")
else :
    print("뒷면입니다.")
print("게임이 종료되었습니다.")
#들여쓰기 없이 밑에다가 쓰면 어떤 조건식? 문장? 이어도 결과로 나옴
#random.randrange(b) 0부터 b까지의 수, b는 포함하지 않는다!!!!!!!!
#random.randrange(a, b) a부터 b까지의 수, b는 포함하지 않는다!!!!!!

#조건을 연속하여 쓰기
x = int(input("정수: "))
if x > 0 :
    print("양수입니다.")
else :
    if x == 0 :
        print("0입니다.")
    else :
        print("음수입니다.")

x = int(input("정수: "))
if x > 0 :
    print("양수입니다.")
elif x == 0 :
    print("0입니다.")
else :
    print("음수입니다.")
#연속 if문
#elif 조건 :
#해당하는 조건이 한 개도 없을 때 마지막에 else :

#종달새가 노래할까?
import random

t = random.randint(1, 24)
s = random.choice([True, False])

print(f"좋은 아침입니다. 지금 시각은 {t}시 입니다.")

if s :
    print("현재 날씨가 화창합니다.")
else :
    print("현재 날씨가 화창하지 않습니다.")

if (6 <= t < 9) and s :
    print("종달새가 노래를 한다.")
else :
    print("종달새가 노래를 하지 않는다.")

#중첩 if문
x = int(input("정수: "))

if x >= 0 :
    if x == 0 :
        print("0입니다.")
    else :
        print("양수입니다.")
else :
    print("음수입니다.")

#로그인 프로그램.1
x = "ilove"

y = input("아이디: ")

if x == y :
    print("환영합니다.")
else :
    print("꺼져")

#.2
a = input("아이디: ")

if a == "ilove" :
    print("환영")
else :
    print("ㄲㅈ")

#축구게임
import random
x = random.choice(["왼쪽", "중앙", "오른쪽"])
 
a = input("어디: ")

if x == a :
    print("성공")
else :
    print("실패")

#연습문제5.1
x = int(input("온도: "))
if x >= 25 :
    print("반바지")
else :
    print("긴바지")

#5.2
score = int(input("시험점수: "))
if score >= 90 :
    print("a")
elif score >= 80 :
    print("b")
elif score >= 70 :
    print("c")
elif score >= 60 :
    print("d")
else :
    print("e")

#5.3
import random
x = random.randint(1, 100)
y = random.randint(1, 100)

z = int(input(f"{x}+{y}="))
if (x - y) == z :
    print("정답")
else :
    print("당신은 바보입니다. ㅋ ㅋ ㅋ ㅋ ㅋ ㅋ")

#5.4
x = int(input("정수: "))

if (x % 2 == 0) and (x % 3 == 0) :
    print("2와 3으로 나누어 떨어집니다.")
else :
    print("떨어지지 않습니다ㅋ")

#5.5
x = int(input("1:"))
y = int(input("2:"))
z = int(input("3:"))

if x >= y and x >= z :
    a = x
elif y >= x and y >= z :
    a = y
else :
    a = z
print(f"가장 큰 숫자는 {a}입니다.")
#아니근데 : 이거를 붙여야하는이유가 뭐야 194줄에

#5.6
x = int(input("강아지의 나이:"))

if x <= 2 :
    y = x * 10
else :
    y = 20 + ((x - 2) * 4)
print(f"강아지의 나이를 사람 나이로 환산하면 {y}살 입니다.")

#5.7
import random
x = random.randint(10, 99)
y = int(input("수 입력: "))

a = y // 10
b = y % 10
c = x // 10
d = x % 10

print(f"당첨 번호는 {x}입니다.")
if a == c and b == d :
    print("추카 백만원")
elif a == c or b == d :
    print("추카 오십마넌")
else :
    print("똥!")

#5.8
x = float(input("키: "))
y = float(input("몸무게: "))

bmi = y / ((x * x)) * 10000

print(f"당신의 bmi = {bmi}")
if bmi <= 18.4 :
    print("저체중 입니다.")
elif bmi <= 24.9 :
    print("적정 체중입니다.")
else :
    print("과체중 입니다.")

#5.9
x = int(input("출생 년도: "))

y = x % 10

if y ==  0 or y == 5 :
# y in [0, 5] :
#range(x, y) 이게 범위표현하는거 [x, y] 이거는 그냥 그 수가 들어있는거
    z = "월"
elif y ==  1 or y == 6 :
    z = "화"
elif y ==  2 or y == 7 :
    z = "수"
elif y ==  3 or y == 8 :
    z = "목"
elif y ==  4 or y == 9 :
    z = "금"
print("")
print(f"{z}요일에 접종가능합니다.")
"""
#5.10
import random
a = ["가위", "바위", "보"] #가위 바위 보 리스트
x = random.randint(0, 2)   #컴퓨터가 뽑은 값
y = input("가위, 바위, 보를 입력하시오: ") #사용자가 입력한 값

z = a[x] #컴퓨터가 뽑은 값을 리스트 인덱스 값으로 변환

print(f"컴퓨터: {z}")
#print(f"컴퓨터: {a[x]}")

if z == y :
    print("비겼습니다.")
elif (x == 0 and y == "바위") or (x == 1 and y == "보") or (x == 2 and y == "가위") :
    print("이겼습니다.")
else :
    print("졌습니다.")

항공우주공학과 202613969 컴퓨터 과학과 코딩 도미란 입니다.

안녕하세요 정미숙 교수님
항공우주공학과 202613969 도미란입니다.

다름이 아니라 '두근두근 파이썬 5장 연습문제 13번'을 풀던 중 리스트 인덱스(정수)와 문자열을 대응시키는 방식에 대해 깊이 고민하게 되어 질문 드립니다.
요즘 일교차가 심하니 건강에 유의하시길 바랍니다.

제가 작성한 코드는 사용자의 입력을 문자로 받고 컴퓨터의 난수(0-2)를 리스트 인덱스로 변환하여 승패를 판정하는 방식입니다.
하지만 교재에 별도의 모범 답안이 없어, 제가 구현한 논리가 책에 의도된 방향과 부합한지 확인하고 싶어 메일 드립니다.

혹시 실례가 되지 않는다면 이 문제에 대해 교수님께서 생각하시는 가장 이상적인 구현 방향이나 참고할만한 피드백을 주실 수 있을까요?

항상 좋은 강의 감사드립니다!
바쁘신 와중 저의 메일을 읽어주셔서 감사합니다.

전화번호 : 010 9431 8063
이메일 : rdmblg02@gmail.com
항공우주공학과 202613969 도미란 올림
