#컴과코 3장

#산술연산자
#덧셈 + 뺄셈 - 곱셈 * 나눗셈 //(나눗셈의 몫) 나눗셈 /(일상적인 나눗셈) 나머지 %
"""
#나머지 연산자 응용.1
n = int(input("정수를 입력하시오: "))
print(n % 2)

#.2
s = int(input("초단위 시간을 입력하시오 : "))
m = s // 60
r = s % 60
#m은 분이고 r은 초
print(m, r)

#커피 가게 매출 계산하기
xx = 2000
yy = 3000
zz = 3500

x = int(input("아메리카노 판매 개수 : "))
y = int(input("카페라떼 판매 개수 : "))
z = int(input("카푸치노 판매 개수 : "))

xxx = x * xx
yyy = y * yy
zzz = z * zz

#변수 한 개를 이용해서 작성
sales = x * xx
sales = sales + y * yy
sales = sales + z * zz

print("총 매출은", xxx + zzz + yyy, "입니다.")
print("총 매출은", sales, "입니다.")

#화씨 온도를 섭씨 온도로 변환하기
f = int(input("화씨 온도를 입력해주세요 : "))
c = (f-32)*(5/9) #소수점 없어도 되는 이유 : 파이썬에서 /는 항상 실수로 계산

print("화씨온도: ", f)
print("섭씨온도: ", c)

#자동 판매기 프로그램'
money = int(input("투입한 돈: "))
price = int(input("물건값: "))
print("투입한 돈: ", money)
print("물건값: ", price)


change = money - price
print("거스름돈: ",change)
five = change // 500
print("500원 동전의 개수: ", five)
change = change % 500
one = change // 100
print("100원 동전의 개수: ", one)

#지수 계산
# ** 제곱 연산자

#원리금 계산
money = 10000000
rate = 0.06
n = 5
print("5년 후 원리금 합계=", int(money*(1+rate)**n))

#2차 방정식 근 계산하기
x = float(input("첫번째 미지수의 계수: "))
y = float(input("두번째 미지수의 계수: "))
z = float(input("상수: "))

a = y ** 2 - 4 * x * z

print("2개의 실근이 있는 경우만 계산할 수 있습니다.")
o = (-y + a ** 0.5)/2 * x
t = (-y - a ** 0.5)/2 * x

print("2개의 실근:", o, t)

#BMI 계산하기
x = float(input("몸무게를 kg 단위로 입력하시오: "))
y = float(input("키를 미터 단위로 입력하시오: "))

bmi = x / (y ** 2)

print("당신의 BMI =", bmi)

#할당연산자
#변수에 값을 저장하는 연산자, =의 왼쪽은 반드시 변수여야하고 =의 오른쪽은 어떤 수식이어도 상관 없음
#x = y = 100 처럼 여러 개의 변수에 동일한 값을 저장하는 것도 가능
#x, y = 100, 200 여러 개의 변수에 서로 다른 값을 저장하는 것도 가능

#복합 연산자
#산술연산자 + 대입 연산자 = 복합 연산자
# x += y  ==  x = x + y
# x -= y  ==  x = x - y
# x *= y  ==  x = x * y
# x /= y  ==  x = x / y
# x %= y  ==  x = x % y

#관계 연산자
# x == y  x와 y가 같은가?  수학적 표기 =
# x != y  x와 y가 다른가?  수학적 표기 =/

#관계 연산자가 생성하는 값
#관계 수식은 참이나 거짓이라는 값을 생성
#참과 거짓은 True와 False로 표시

#문자열의 비교
x = "Happy"
y = "Happy"
print(x == y)

x = "apple"
y = "banana"
print(x < y)
print(x > y)
#사전에서 x가 y보다 앞에 있으면 트루, 아니면 폴스

#실수와 실수의 비교
a = 0.1 + 0.2
print(a == 0.3)
#비트 수가 제한되어 있기 때문에 실수를 정확하게 표현하지 못함

import math
a = 0.1 + 0.2
print(abs(a-0.3) < 0.00000001) #a와 0.3의 오차가 작으면(소수 8번째 자리 차이)
#abs는 절대값 계산

#컴퓨터의 데이터 표현
#사람 10진수, 컴퓨터 2진수
#10진수와 2진수의 상호 변환과정에서는 오차가 발생함
#아주 미세한 반올림 오차가 발생(10진수에서 1/3은 0.333...이지만 0.33으로 사용할 때 처럼)

math.isclose(3.14, 3.15)
math.isclose(3.141590003, 3.141590002)

#연산자의 우선 순위
# ** 지수 연산자
# ~ + - 단항 연산자
# * / % // 곱셈, 나눗셈, 나머지 연산자
# + - 덧셈 뺄셈
# >> << 비트 이동 연산자
# & 비트 AND 연산자
# ^ | 비트 XOR 연산자, 비트 OR 연산자

#평균구하기
x = int(input("첫 번째 수를 입력하시오: "))
y = int(input("두 번째 수를 입력하시오: "))
z = int(input("세 번째 수를 입력하시오: "))
avg = (x + y + z) / 3
print("평균=", avg)

#산수 퀴즈 프로그램
print("산수 퀴즈에 오신 것을 환영합니다.")
x = int(input("2 + 5 ="))
print(x == 2+5)
y = int(input("7 - 6 ="))
print(y == 7-6)
z = int(input("2 ** 3 ="))
print(z == 2**3)

#math 모듈 사용하기
import math

#원의 둘레 계산
r = 3
c = 2 * math.pi * r
print("원의 둘레=", c)

#팩토리얼 계산
print("7!=", math.factorial(7))

#2개의 실수가 거의 동일한지를 검사
print("6.999999999와 7의 비교=", math.isclose(6.999999999, 7))

#자연 로그값 계산
print("log(3.4)=", math.log(3.4))

#제곱근 계산
print("4의 제곱근=", math.sqrt(4.0))

#연습문제3.1
x = int(input("x"))
f = x ** 4 - 9 * (x ** 3) + x ** 2
print(f)

import math
y = int(input("y"))
fx = (4/3) * math.pi *(y**3)
print(fx)

a = int(input("a"))
b = int(input("b"))
c = int(input("c"))

fxx = (-b - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
print(fxx)

#3.2
x = int(input("주유한 연료의 양(단위 : 리터): "))
y = int(input("주행한 거리(km): "))
print("자동차의 연비는", y / x, "km/리터입니다.")

#3.3
x = int(input("감염 지수: "))
y = int(input("일수: "))
print(y, "일 후의 에상 감염자는", x ** y, "입니다.")

#3.4
x = int(input("이자율(단위 %): "))
y = int(input("원금(단위: 만원): "))
z = int(input("거치 기간(단위: 년): "))
print(str(x) + "년 후의 원리금은", int(((y * ((1 + (x/100)) ** z)))*10000))
#아니...왜 소수점으로 표시가되는거냐고...
#단항 연산자하고 이항 연산자가 뭐지?


#3.5
x = int(input("x"))
y = int(input("y"))
print(x, y, x + y, x - y, x * y, (x + y)/2, max(x,y), min(x,y))

#3.6
x = int(input("x"))
y = int(input("y"))

import math
print(x, y, 3.141592 * (x ** 2) * y)

#3.7
x = int(input("정수를 입력하시오: "))

a = x % 10
b = x // 10
b = b % 10
c = x // 100
c = c % 10
d = x // 1000
d = d % 10

print(a+b+c+d)

#3.8
x = int(input("x"))
y = int(input("y"))
x1 = int(input("x1"))
y1 = int(input("y1"))

s = (((x - x1) ** 2) + ((y - y1) ** 2)) ** 0.5
print(s)
"""
#3.9
import time
f = time.time() + 32400
a = f % 86400
a = a // 3600
b = f // 60
b = b % 60
print(a, b)

#3.10
x = int(input("물체의 무게를 입력하시오(킬로그램): "))
y = int(input("물체의 속도를 입력하시오(미터/초): "))

print("물체는", 0.5 * x * (y ** 2), "(줄)의 에너지를 가지고 있다.")
