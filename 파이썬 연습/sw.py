#2차시
'''
print("Do-Mi-Ran")
print("010-9431-8063")
print("rdmblg02@gmail.com")
print("chonbuk National Univ.")
print("~"*20)


for i in range(2,10):
    for j in range(1,10):
        print(i,"x",j,"=",i*j)
for i in range(1,10):
    for J in range(2,6):
        print(j,"x",i,"=",i*j,end='\t\t')
    print()


print("-"*50)

for i in range(1,10):
    for j in range(6,10):
        print(j,"x",i,"=",i*j,end='\t\t')
    print()


num = int(input("정수:"))
print(num,"=",end='')

insu = 2
result = {}

while insu <= num :
    if num%insu == 0:
        if(insu in result): result[insu]+=1
        else: result[insu]=1
        num = num/insu
    else :
        insu += 1

cnt = len(result)
i = 1

for k,v in result.items():
    if v==1 : print(k,end="")
    else:       print(k,"^",v,end="")
    if i < cnt :
        print("x",end="")
        i += 1


import turtle as t
t.shape("turtle")
#삼각형그리기
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
#사각형그리기
t.color("red")
t.left(120)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
#오각형그리기
t.color("blue")
t.left(90)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
'''

'''
#3차시
print(100+24)
#"는 문자열, 값을 구해야하는 수식이 아님
print("100+24")
print(1000-23424)
print("100-243")
print(342*2435)
print("243*34")
print(24332/2342)
print("243/234")



price = 100
babo = 22

print(price+babo)

price = 1000
count = 3.5
item = "apple"
total = price * count
바보 = 1

print(바보)
print(price)
print(count, item)
print(price+babo)
print(total)


radius = 5
pi = 3.14
area = radius**2*pi
#area = 5 * 5 * pi
print("반지름이 5인 원의 넓이 =", area)



x = 45
print("내가 처음 생각한 자연수 =", (x+10)/5-3)

num1 = 45
num2 = num1 + 10
num3 = num2 / 5
num4 = num3 - 3
print("내가 처음 생각한 자연수 =", num4)

num = 45
num = num + 10
num = num / 5
num = num - 3
print("내가 처음 생각한 자연수 =", num)


#4차시
x = 10
print(type(x))
y = 10.0
print(type(y))
z = "10.0"
print(type(z))
n = '10'
print(type(n))


total = 3 + 5
print(type(total))
y2 = y - 2
print(type(y2))
avg = total/2
print(type(avg))
#인트+인트=인트, 플롯-인트=플롯, 나누기는항상플롯


name = "python~ "
txt = "Hello "
print(name + txt)
print(txt + name)
print(txt + name + txt)


z ="10"
print(z*3)
z = 10
print(z*3)
#z는 문자, 더하기3은 숫자, 다른연사자라서 계산 ㄴㄴprint(z+3)
#print("문자열"), print(변수이름), print("문자열", 변수)


print(1, end=' ')
print(2, end=' ')
print(3, end=' ')
print(4)


#sep='\n' 구분자(separator)지정(전체구분), \n(각각구분)
#\한개 쓰는건 기능을 막아줌, r은 문자를 그대로 출력(함수기능없앰)
print(1,2,3,sep='\n')
print("1\n2",end=' ')
print(3)
print("1\n2\n3")
print("1\\n2\\n3")
print(r"1\n2\n3")


#큰따옴표만 출력(''작은따옴표쓰기), 둘다출력('작은따옴표 세 개쓰기)
print('나의 꿈은 "내"가 되는 것이다')
print("""너의 "꿈"을 응원하는 '나'를 기억해줘.""")
#시발진짜뭐지? '이거 3개쓰니까 주석처리가 안되고 강의에서는 '이거로 쓰라는데
#"이거로 써도 써지긴하네 뭐냐
print('it\'s python')


ddd = """
안녕하세요.
파이썬 공부 중입니다.
여러 줄도 문제없어요!
"""
print(ddd)


print("""ㅇ
2
2
""")
#이건또왜되는거냐..


name = "도미란"
rank = 1
money = 100

print("=" * 20)
print(name, "님")
print(rank, "등 입니다.")
print("상금은", money, "만원 입니다.")
print("=" * 20)


name = input("이름을 입력하세요:")

txt = "의 꿈을 응원합니다"

print(name,txt, sep='')
print(name + txt)
input("엔터를 누르세요")


#amount = input("총 비용:")
#n = input("사람 수:")

#amount = int(amount)
#n = int(n)

amount = int(input("총 비용:"))
n = int(input("사람 수:"))

pay = amount/n
#pay = int(amount)/int(n)

print("님이 내셔야할 돈은",pay,"입니당 쌰갈!!")


화 = int(input("화씨 :"))
섭 = (화-32)*9/5
print("변환된 화씨 온도는",섭,"섭씨 온도 입니다")
print("화씨온도:",화,"->","섭씨온도:",섭)


k = float(input("키를 입력해주세요(m):"))
kg = float(input("몸무게를 입력해주세요(kg):"))

bmi = round(kg/(k*k),2)
print("당신의 BMI는",bmi,"입니다")


x = str(input("원하는 특수문자를 입력하세요:"))
n = int(input("몇 번 반복할까요?"))

print((x+" ")*n)


score = int(input("점수를 입력하세요 :"))
print("80점보다 크거나 같은가?", score >= 80)


print("회원가입")
비번 = int(input("비밀번호를 만드세요:"))
print("로그인")
로그인 = int(input("비밀번호를 누르세요:"))
if 로그인 == 비번 :
 print("로그인 완료")
else :
 print("로그인 실패")


year = int(input("출생년도를 입력하세요:"))

is20 = (2026-year) >= 20
iseven = (year%2) == 0

ischeck = is20 and iseven

print("올해 건강검진 대상자인가?",ischeck)


password = "Cbnu9981"
number = input("비밀번호를 입력하세요")
print("비밀번호가 맞습니까?", password == number)


kor = int(input("국어 점수 입력 :"))
math = int(input("수학 점수 입력 :"))
eng = int(input("영어 점수 입력 :"))

avg = (kor+math+eng)/3

ischeck = (kor>=90) and (math>=90) and (eng>=90)

print("장학생인가요?",ischeck)

if(avg >= 90):
    print("축하합니다")
    print("A등급 입니다")
print("성적 평균 = ", avg, "점 입니다.")
'''
'''
avg = float(input("평균 점수를 입력하세요 :"))

if (avg>=90) :
    grade = 'A'
if (80 <= avg < 90) :
    grade = 'B'
if (70 <= avg < 80) :
    grade = 'C'
if (60 <= avg < 70) :
    grade = 'D'
if (avg <= 60) :
    grade = 'F'

print(grade, "등급 입니다")


num = int(input("정수를 입력하세요 :"))

if(num < 0):
    num = num*-1
print("절댓값 =" , num)


num = int(input("정수를 입력하세요 :"))

if(num%2 == 0):
    print("짝수입니다.")
else:
    print("홀수입니다.")


price = int(input("구매한 총액을 입력하세요 ;"))

if (price >= 100000):
    rate = 0.85
else:
    rate = 0.9

amount = price*rate
print("결제할 금액 =", int(amount),"원 입니다")


x = int(input("정수를 입력하세요 :"))

if (x>0):
    result = "양수이다"
elif (x<0):
    result = "음수이다"
else :
    result = "0이다"

print("입력한 값은", result)


avg = float(input("점수:"))
if (avg >= 90):
    grade = 'A'
elif(avg >= 80):
    grade = 'b'
elif(avg >= 70):
    grade = 'C'
elif(avg >= 60):
    grade = 'D'
else:
    grade = 'F'
print(grade, "등급 입니다")
    

이름 = "미란"
나이 = 19
전화 = "01094318063"
키 = 160


프로필 = ["미란", 19, "01094318063", 160]
print(프로필[0])

프로필[0] = "앙"
print(프로필) #()수정불가능 []수정가능

name = ['a', 'b', 'c', 'd', 'e', 'f', 'c']
print(name[1:3]) #1부터 2까지
print(name[1:]) #1부터 끝까지
print(name[:3]) #처음부터 끝까지
print(name[-1:-3]) #마지막
print(name[1:1]) #처음은 포함, 마지막은 포함안함, 시작하자마자 끝냄

name.append('앙앙')

name.insert(5,'앙앙앙')
print(name)


for i in range(5) :
    print("안녕", i+1)

for i in range(5) :
    print("hello",i)
    print("앙!!")


for i in range(9 ):
    print("2 x", i+1, "=", 2*(i+1))


for i in range(5):
    print('#'*(i+1))


hap = 0
for i in range(1,11):
    hap = hap + i
    print("hap=",hap)


x =int(input("1부터 몇까지의 합을 구할까요?"))

hap = 0
for i in range(1,x+1):
 hap = hap + i
 print(hap)


숫자 = [1,2,3,4]
for i in 숫자 :
 print(i)


import turtle as t
t.shape("turtle")
for i in range(4):
    t.forward(100)
    t.left(90)
for i in range(5):
    t.forward(100)
    t.left(72)
t.clear()


import turtle as t
t.shape("turtle")
n = int(t.textinput("정다각형 그리기","n"))

for i in range(n):
    t.forward(100)
    t.left(360/n)


import turtle as t
t.shape("turtle")
for i in range(100):
    t.forward(2)
    t.penup()
    t.forward(2)
    t.pendown()


import turtle as t
size = [10,20,30,40]
for i in size :
 for j in range(4):
    t.forward(i)
    t.left(90)


import turtle as t
size = [10,20,30,40]
for i in size :
    t.penup()
    t.forward(i)
    for j in range(4):
     t.pendown()
     t.forward(i)
     t.left(90)


for i in range(5):
    print("안녕하세요")

i = 0
while(i<5):
    print("안녕하세요")
    i = i+1


i = 0
hap = 0
while(hap<=500):
    i = i + 1
    hap = hap +i

print("i=",i)
print("hap=",hap)


n = 8
y = 1

x = int(input("내가 생각한 숫자를 맞춰보세요:"))
        
while(n!=x):
    if(x < 0):
        print("중단합니다")
        break
    print("실패")
    x = int(input("다시 입력:"))
    y = y + 1
if(x==n):
 print(y,"번 만에 성공하셨습니다")
print("게임 끝!")
'''


