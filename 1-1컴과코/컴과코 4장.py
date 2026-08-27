#컴과코 4장
#파이썬에서 사용할 수 있는 자료의 종류
#정수, 실수, 문자열
#문자열을 변수에 저장할 때는 꼭!!!!!!!!!!!!!!!!!따옴표를 붙여야한다!!!!!!!!!!!!

#큰따옴표와 작은 따옴표를 동시에 사용하는 경우
# x = "철수가 "안녕"이라고 말했습니다."  실행안됨! 왜" 안에 "가 있냐!
# x = "철수가 '안녕'이라고 말했습니다."  철수가 '안녕'이라고 말했습니다. 라고 실행됨

#자료형에 따라 연산 결과가 달라진다
#100과 "100"의 차이
"""
print(100+200)
print("100"+"200")

#자료형을 알고 싶으면?
#type함수 사용
print(type("Hello World!"))
print(type(3.2))
print(type(17))

x = 10
print(type(x))

#int == 문자열을 정수로 변환
#float == 문자열을 실수로 변환
#input은 기본적으로 문자열 형태로 저장! 숫자여도 문자열로 저장함

t = input("정수를 입력하시오:")
x = int(t)
# x = int(input("정수어쩌구:")
t = input("정수를 입력하시오:")
y = int(t)
# y = int(input("정수어쩌구:")
print(x+y)
#사용자가 소수를 입력하면 오류가 남
#float을 사용하여 소수로 받기

#str함수
print("나는 현재 " + str(21) + "살이다.")
print("원주율은 " + str(3.14) + "입니다.")

#챗봇 프로그램
print("안녕하세요?")
x = input("이름이 어떻게 되시나요?: ")
#y = int(input("나이가 어떻게 되나요?: "))
print("\n만나서 반갑습니다." + x + "씨")
print("이름의 길이는 다음과 같군요:" + str(len(x)))
y = int(input("나이가 어떻게 되나요?: "))
#len은 문자열을 구성하는 문자 개수
#print("나이가 어떻게 되나요? " + str(y))
print("내년이면 " + str(y + 1) + "이 되시는군요")

print('hello ' + 'World!')

#문자열을 반복하려면 * 연산자
print("=" * 50)

#문자열의 길이 len
print(len("Hello Wolrd"))

#문자열 포함 여부 in
print('hello' in 'hello world')

#문자열 연산
#count 서브 문자열 나오는 횟수
text = " Hello Wolrd "
print(text.count("o"))

#lower 소문자로
print(text.lower())

#strip 좌우 공백 제거
print(text.strip())

#f문자열!!!!!!!!!!!!!!!!!
#문자열에 변수의 값을 삽입하여 출력하고 싶으면 f-문자열
price = 10000
print(f"상품의 가격은 {price}원입니다.")
#문자열 맨 앞에 f를 붙이고 중괄호{} 안에 출력하고 싶은 변수

product = "coffee"
count = 3
price = 10000
print(f"상품 {product} {count}개의 가격은 {count*price}원입니다.")
#와..아니 중괄호랑 중괄호 사이에 띄어쓰기가 반영이 된다고?

#개별 문자 추출
#문자열에서 개별 문자를 추출하려면 인덱스라는 번호를 사용한다.
#기준 : 왼쪽 0부터 시작
#기준 : 오른쪽 -1부터 시작

s = "Monty PYthon"
print(s[6:10])

#특수 문자열
# \n 줄바꿈 문자
# \t 탭 문자
# \\ 역슬래시 자체
# \" 큰따옴표 자체
# \' 작은따옴표 자체

x = 'doesn\'t'
print(x)

#이니셜 출력하기
a = input("첫글자: ")
b = input("두번째: ")
c = input("세번째: ")

print(a[0] + b[0] + c[0])

#단답형 퀴즈 프로그램
a = input("세상에서 가장 쉬운 프로그래밍 언어는?: ")
print(a == "파이썬")
#이게 되네? a == 문자열 값을 입력해도 되는구만.. 변수로만 저장해야하는줄 알았는데!!

#리스트!!!!!!!!!!!!!!
#여러 개의 자료들을 모아서 하나의 묶음으로 저장하는것
#항목들은 쉼표로 분리
#대괄호로 묶음[]
#리스트 항목 종류 : 문자열, 숫자도 가능
#리스트 항목 지정 : []안에 인덱스 이용, 0부터 ~~
#공백 리스트 생성 가능 ex) list = []
#리스트 항목 추가 : 공백리스트 생성 후 append()이용, list.append()

#친구들의 리스트 생성하기
list = []

f = input("친구:")
list.append(f)

f = input("친구:")
list.append(f)

f = input("친구:")
list.append(f)

f = input("친구:")
list.append(f)

f = input("친구:")
list.append(f)

print(list)

#연습문제4.1
print("나는 " + str(12) + "개의 사과를 먹었다.")

#4.2
x = input("문자열을 입력하시오: ")
print(x + "하는중")

#4.3
x = input("기호를 입력하시오: ")
y = input("중간에 삽입할 문자열을 입력하시오: ")
print(x[0] + y + x[1])

#4.4
list = [1, 2, 3, 4]
x = list[0] + list[1] + list[2] + list[3]
print(x)

#4.5
list = []
x = int(input("정수:"))
list.append(x)
y = int(input("정수:"))
list.append(y)
z = int(input("정수:"))
list.append(z)

print("리스트 = ", list)
print("리스트 숫자들의 합 =", list[0] + list[1] + list[2])
"""
#4.6
import random
list = [str(1), str(2), str(3), 'a', 'b', 'c']
print("생성된 패스워드: ", random.choice(list) + random.choice(list) + random.choice(list))

