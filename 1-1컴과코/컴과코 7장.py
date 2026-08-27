#컴과코 7장
#함수 : 서로 관련된 코드를 묶은 것
#모듈 : 여러 개의 함수들이 포함되어 있는 소스 파일
#객체 : 서로 관련된 변수와 함수를 하나로 묶은 것

#함수 정의
#def 함수이름() :
    #코드 묶음

#함수 호출
#함수 이름()

def print_address():
    print("어쩌라고용")
    print("용용죽겠징")

print_address()


#함수의 장점
#언제든지 필요할 때 불러서 일을 시킬 수 있다.

#함수에 입력 전달하기
#함수에 값을 저장할 수 있고 이를 인수라고함


def print_address(name):
    print("어쩌라고용")
    print("용용죽겠징")
    print(name)
    return name

y = print_address("바보")
print(y)


#값 반환하기
#함수는 값을 반환할 수 있다.
#return 사용

def calculate_area(radius):
    area = 3.14*radius**2
    return area

c_area = calculate_area(5.0)

print(c_area)

#함수에다가 어떤 복잡한 값을 저장함
#인수가 있으면 함수에 이미 계산된 값을 함수 밖으로 빼내야함
#그 계산된 값을 다시 받아줄 변수가 필요함
#그럼 그 변수를 호출해서 언제든지 특정 값을 거친 함수를 사용할 수 있음
#물론 함수 그 자체도 사용할 수 있음
#리턴없이 써도는 되는데 저장을 못함


#여러 개의 값을 반환하기
def get_input():
    return 2,3

x,y = get_input()

print(x,y)


def calculate (radius) :
    area = 3.14 * radius ** 2
    perimeter = 2.0 * 3.14 * radius
    return area, perimeter

x, y = calculate(10)
print(x, y)

#함수에 여러 개의 입력 전달하기
def get_sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += 1
    return sum

print(get_sum(1,10))


#자음과 모음의 개수 카운티하기
x = input("문자열을 입력하시오: ")

def countVowel(x) :
    count = 0
    for i in x :
        if i in ['a','e','i','o','u'] :
            count += 1
    return count

total = countVowel(x)
print(total)
  
    
#로또 번호 생성 함수
import random

def number():
    y = []
    while len(y) < 6 : #굳이 카운트 변수 안생성해도됨
        #그냥 len함수로 인수 몇개인지 측정
        x = random.randint(1,45)
        if x not in y :
            #중복 확인할 때 있으면 빼기보다 없으면 추가하기가 나음
            y.append(x)
    return y

print(f"생성된 로또번호: {number()}")


#변수의 종류
#지역 변수 : 함수 안에서 생성되는 변수
#전역 변수 : 함수 외부에서 생성되는 변수
#지역변수
def calculate_area (radius):
    result = 3.14 * radius ** 2
    return result

r = float(input("원의 반지름: "))
area = calculate_area(r)
print(area) #reuslt는 지역변수이기 때문에 반환한 값을 area에다가 저장한 것
#그래서 area를 출력해야

#radius, result는 지역변수, 함수가 종료되면 사라짐
#r, area는 전역변수, 함수 안팎에서 어디서든지 사용 가능


#전역변수
def calculate_area():
    result = 3.14 * r ** 2
    return result

r = float(input("원의 반지름:" )) #전역변수는 함수 뒤에 있어도 괜찮음
area = calculate_area() #괄호가 비어있어도 괜찮음 왜냐면 매개변수가 없으니까
print(area)


#함수 안에서 전역 변수 변경하기
def calculate_area(radius) :#전역변수 area에 계산값을 저장하려고함
    global area #함수 밖에 있는 전역변수와 같다고 선언
    area = 3.14 * radius ** 2 #반환되는 값 없이 return만 사용 가능
    return

area = 0
r = float(input("원의 반지름:"))
calculate_area(r) #이거는 그냥 함수 호출
#함수를 호출해서 area값을 바꾼 후 프린트 한 것
print(area)


#디폴트 인수
def greet(name, msg) :
    print("안녕", name+','+msg)

greet("철수","좋은 아침!")


def greet(name, msg="별일없죠?") :
    #디폴트 인수 두개하고 싶으면
    #(name="영희", msg="별일없죠?"):
    #디폴트 인수를 만들 땐 오른쪽부터 채워야
    print("안녕", name+','+msg)

greet("철수") #디폴트 인수이기 때문에 호출할때 값을 바꾸면 값이 바뀐상태로 출력됨


#3개 중에서 갸장 큰 값 찾기
def max(a,b,c=-10000): #두개만 써도 구할 수 있도록 c에다가 -10000부여
    if a >= b and a >= c :
        large = a
    elif a <= b and c <= b :
        large = b
    else :
        large = c
    return large

print(max(3,1,2))
print(max(1, 2))


#키워드 인수
#인수의 이름을 명시적으로 지정해서 전달하는 방법
def b(x,y,z):
    print(x,y,z)

#함수 호출
#b(10,20,30)

#키워드 인수는 직접 대입해서 전달할 수도 있음
#b(x=10, y=20, z=30)

#키워드 인수의 장점은 인수의 위치가 매개변수와 달라도 된다는 것
#b(y=20,x=10,z=30)
#b(z=30,y=20,x=10) 등등

#키워드 인수와 위치인수가 섞일 수는 있는데 위치인수가 더 앞에 와야함
#b(10, y=20, z=30) o
#b(x=10, 20, 30) x


#연습문제 1장
def birtday(name):
    print("Happy Birthday to you!") 
    print("Happy Birthday to you!") 
    print("Happy Birthday, dear" , name)
    print("Happy Birthday to you!")

    
birtday("도해연")


#연습문제 2장
x = int(input("첫 번째 정수 "))
y = int(input("두 번째 정수 "))

def a(x, y):
    summ = int(input(f"정수 {x}+{y}의 합은? :"))
    b = x + y
    if summ == b :
        print("정답입니다.")
    else :
        print("틀렸습니다.")

a(x, y)


#연습문제 3장
PI = 3.14

def x(r):
    return PI * r ** 2

def y(r):
    return 2 * PI * r
    
r = int(input("반지름: "))

a = x(r)
b = y(r)
print(a)
print(b)


#연습문제 4장
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def dlv(x,y):
    return x/y

x = int(input("x의 값: "))
y = int(input("y의 값: "))

a = add(x,y)
b = sub(x,y)
c = mul(x,y)
d = dlv(x,y)

print(a)
print(b)
print(c)
print(d)


#연습문제 5장
def factorial(n):
    x = 1
    summ = 1
    while x < n+1 :
        summ = x * summ
        x += 1
    return summ

n = int(input("정수를 입력하시오: "))
total = factorial(n)
print(total)


#연습문제 6장
def grade(score):
    if score >= 90 :
        print("A입니다.")
    elif score >= 80 :
        print("B입니다.")
    elif score >= 70 :
        print("C입니다.")
    elif score >= 60 :
        print("D입니다.")
    else :
        print("F입니다.")

score = int(input("성적을 입력하시오: "))
a = grade(score)
input("\n엔터 키를 누르면 프로그램이 종료됩니다...")


#과제
def square_Area(width, heigth):
    area = width * height
    return area

width = int(input("가로: "))
height = int(input("세로: "))
area = square_Area(width, height)
print(area)


a = 222

def func1() :
    print(a)
def func2() :
    a = 111
    print(a)

func1()
func2()


def f(x,y):
    if x%y==0:
        return 1
    else :
        return 0

print(f(12,3))
"""

def fun(t) :
    n = (t+1)*(t+1)

n = 7
print(n)
fun(n+1) #return을 안해서 함수 안에서 81이 나오긴 하지만 저장이 안됨
print(n) #따라서 전역변수에 저장된 값인 7이 나오게됨


    


    



