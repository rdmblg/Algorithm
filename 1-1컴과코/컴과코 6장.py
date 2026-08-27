#컴과코 6장
#for문


#for i in range(범위) :
for i in range(5):
    print("방문을 환영어쩌구")
#i가 0부터 4까지 변경
#for i in range(시작값, 종료값, 증가값)
#종료값은 -1해서 끝남, 증가값은 시작에서 종료까지 증가하는 양
for i in range(1, 10, 3):
    print(f"변수 i의 값={i}")
print()
#에서 1부터 시작해서 3씩 올라가는 것, 1 4 7, 10은 포함 안됨
#증가값이 1이면 증가값은 생략 가


#for 변수 in 리스트 :
#   문장(들여쓰기)
for i in [1,2,3] :
    print(i)
#리스트 안에 있는 인수가 i에 들어가며 인수 수 만큼 반복
#i가 1부터 5까지 변경


#end="" 출력결과 한줄에 나오게 하기
#따옴표 안을 띄어쓴 만큼 간격이 넓어짐
#따옴표 안에 뭔가를 넣어 쓸수도 있음
print("123",end=" ")
print("456")

print("123",end="")
print("456")

print("123",end="안녕")
print("456",end=" @ @ ")
print("789",end=" ")
print("10")


#카운트 다운 프로그램
import time
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("발사!")

#요리 타이머 작성하기
import winsound
import time

x = int(input("초 단위의 시간을 입력하시오: "))

for i in ragne(x, 0 ,-1):
    print(f"{i}초 남았습니다.")
    time.sleep(1)

#winsound.Beep(2000, 3000)
#beep(주파수, 시간)
#주어진 주파수의 시간동안 알람이 울림, 주파수 32, 3276
#시간 단위는 ms(1000=1초)
#winsound 안에 존재

#구구단
x = int(input("원하는 단은: "))

for i in range(1, 10):
    print(f"{x}*{i}={x*i}")


x = int(input("정수를 입력하시오: "))

y = 1
for i in range(1, x+1):
    y = y * i
print(y)

#팩토리얼은 1에서부터 x까지의 수를 곱하는거니까
#저 계산식은 1부터 계산값을 하나씩 계산해가는거


#while문
#while 조건 :
    #반복 문장

response = "아니"

while response =="아니":
    response = input("엄마, 다 됐어?")
print("먹자")
#리스폰이 아니면 반복하는 문장이어서 처음에 변수가 있어야함
#while문을 쓸 때는 while 조건이 참이 될 내용 문장이 있어야함


#로그인 프로그램
login = ""

while login != "pythonisfun":
    login = input("암호를 입력하시오: ")
print("로그인 성공")
#처음 변수에 그냥 아무것도 저장을 안해둔 것


#1부터 10까지의 합 계산
x = 0
count = 1
while count < 11:
    x = x + count
    count = count + 1
print(f"합계는 {x}")


#사용자가 입력하는 숫자의 합 계산
sum = 0
#혹은 x = input("계속?(yes/no): ")
x = "yes"

while x == "yes":
    y = int(input("숫자를 입력하시오: "))
    sum = sum + y
    x = input("계속?(yes/no): ")
print("합계는", sum)


#숫자 맞추기 게임
#1번
import random
print("1부터 100 사이의 숫자를 맞추시오")

x = random.randint(1, 100)
y = int(input("숫자를 입력하시오: "))
tryy = 1

while y != x:
    if y < x:
        print("낮음!")
        y = int(input("숫자를 입력하시오: "))
        tryy += 1
    else :
        print("높음!")
        y = int(input("숫자를 입력하시오: "))
        tryy += 1
print("축하합니다. 시도횟수 =", tryy)

#아 일단 문제가 존나많은데..일단은 인풋을 바깥에서 받았기 때문에 트라이 횟수 추가가안되고


#아니씨발다른버전ㅉ
#2
import random

tryy = 0
guess = 0
answer = random.randint(1,100)

print("1부터 100 사이의 숫자를 맞추시오")

while guess != answer:
    guess = int(input("숫자를 입력하시오: "))
    tryy += 1
    if guess < answer:
        print("낮음!")
    elif guess > answer:
        print("높음!")
    else :
        print("축하합니다", end="")

print("시도횟수=",tryy)


#3번
import random

x = random.randint(1,100)
y = 0
tryy = 0

while x != y:
    y = int(input("숫자를 입력하시오: "))
    tryy += 1
    if y < x:
        print("낮음!")
    elif y > x:
        print("높음!")
print(f"축하합니다. 시도횟수={tryy}")
#이게 제일 깔끔한듯
#이프문에 들어갈 중복된 함수는 그냥 이프문 밖에다가 그니까 와일문에다가 같이 써도됨


#초등생을 위한 산수 문제 발생기
import random

while True :
    x = random.randint(1,100)
    y = random.randint(1,100)
    z = int(input(f"{x}+{y}="))
    if x + y == z:
        print("잘했어요!!")
    else :
        print("다음번에는 잘할 수 있죠?")


print("안녕",end="")
print("바보",end=" ")
print("히히")
#end함수 쓸 때 ""사이에 공백에 따라서 공백이 생김 end는 줄붙이는 함수


#모든 샌드위치 종류 출력하기
bread = ["호밀방"]
meat = ["미트볼", "쏘지지", "닭가슴살"]
vege = ["양상추", "토마토", "오이"]
source = ["마요네즈", "허니 머스타드", "칠리"]

for b in bread :
    for m in meat :
        for v in vege :
            for s in source :
                print(f"{b}+{m}+{v}+{s}")
#포문은 범위만큼 반복하는거니까 범위가 끝날때까지 반복
#맨위에 리스트가 다 되면 아래거는 실행되지않고 그대로 끝남, 중간도 마찬가지

#존나재밋당ㅎ
from itertools import product

bread = ["호밀빵", "위트"]
meat = ["미트볼", "소시지"]
vege = ["양상추", "토마토"]
source = ["마요네즈", "칠리"]

# 모든 리스트를 product 안에 넣으면 알아서 모든 조합을 만들어줍니다.
for b, m, v, s in product(bread, meat, vege, source):
    print(f"{b} + {m} + {v} + {s}")


#무한루프와 break
#while True :
    #반복문장
    #반복문장
    #if 조건 :
        #break;

while True :
    light = input("신호등 색상을 입력하시오")
    if light == "blue":
        break
print("전진!")


#암호해독 프로그램
import random
import sys

user_pass = input("패스워드를 입력하시오: ")
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

for letter1 in password:
    for letter2 in password:
        for letter3 in password:
            guess = letter1 + letter2 + letter3
            print(guess) 
            if guess == user_pass:
                print("당신의 패스워드는 " + guess)
                sys.exit()  # 프로그램 강제 종료!!
#random은 하는 일이 없고
#sys는 멈추는 함수인데 break는 한개만 멈추고 sys는 전체 다 멈춤


#점치는게임 ㅇㅈㄹ
import random
import sys
listt = ["네, 확실합니다.", "전망이 좋은 거 같은 데요.", "믿으셔도 됩니다.", "글쎄요 아닌 것 같군요.", "한 점의 의심도 없이 맞습니다.", "그럼요, 명백히 올바른 선택을 했습니다.", "제 답변은 No입니다.", "나중에 다시 물어 보세요."]

while True :
    x = input("이름: (종료하려면 엔터키)")
    if x == "":
        sys.exit()
    y = input("무엇에 대하여 알고 싶은가요?")
    print(f"{x}님 \"{y}\"에 대하여 질문 주셨군요.\n운명의 주사위를 굴려볼게요....")
    print(random.choice(listt))


#연습문제
#1장
for i in range(1,101):
    if i % 2 == 0 :
        print(i,end=" ")


x = 1
while x <= 100 :
    if x % 2 == 0 :
        print(x, end=" ")
    x += 1


#연습문제2
import time

x = 1
y = 1

while x != 6 :
    print(f"{x}세트 {y}회입니다.")
    y +=1
    time.sleep(1)
    if y == 11 :
        x += 1
        y = 1


#연습문제 3장
#다시풀어보기
x = 1

while x < 100 :
    if x % 10 in [3, 6, 9] and x // 10 in [3, 6, 9] :
        print(x, "짝짝")
    elif x % 10 in [3, 6, 9] or x // 10 in [3, 6, 9] :
        print(x, "짝")
    else :
        print(x)
    x += 1


#연습문제 4장
x = 10000000
y = 0
while x <= 20000000 :
    y += 1
    x = x * 1.07
    print(f"{y}년 후 {x}가 되었습니다.")
print(y, "년이 걸립니다.")


#연습문제 5장
import random

x = random.randint(1,10)
y = random.randint(1,10)
z = input(f"{x}*{y}는")

while z != x * y :
    z = int(input(f"{x}*{y}는 "))
    if z == x * y
        print("맞았습니다.")
        break


#연습문제 6장
from rich.console import Console
from rich.panel import Panel

console = Console()
console.print(Panel("더하기 계산기!", style="bold magenta", expand=False))

summ = 0
while True :
    x = int(input("정수를 입력하시오: "))
    if x == 0 :
        print("합은", summ, "입니다.")
        break
    summ = summ + x


import tkinter as tk
from tkinter import messagebox

def add_number():
    global summ
    try:
        x = int(entry.get())
        if x == 0:
            messagebox.showinfo("결과", f"최종 합은 {summ}입니다.")
            root.quit()
        else:
            summ += x
            label_sum.config(text=f"현재 합: {summ}")
            entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("에러", "정수만 입력하세요!")

summ = 0
root = tk.Tk()
root.title("더하기 계산기")
root.geometry("300x200") # 창 크기

label_title = tk.Label(root, text="숫자를 입력하고 버튼을 누르세요")
label_title.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

btn = tk.Button(root, text="더하기", command=add_number)
btn.pack(pady=10)

label_sum = tk.Label(root, text="현재 합: 0")
label_sum.pack()

root.mainloop()


import tkinter as tk
from tkinter import messagebox
messagebox.showinfo("경고","보안이 위험합니다.")


#연습문제 7장
import random

z = 0

while z !=3 :
    x = random.randint(1,6)
    y = random.randint(1,6)
    print(f"첫번째 주사위= {x} 두번째 주사위= {y}")
    z += 1


#연습문제 8장
import time
import random

timee = random.randint(1,10)
a = time.time()

z = input(f"{timee}초가 지나면 엔터키를 누르세요")

b  = time.time()

c = timee - (b - a)
d = int(abs(c))
if d == 0 :
    print("완벽합니다.")
elif d > 0 :
    print(f"{d}초가 빨랐습니다.")
else :
    print(f"{d}초가 느립니다..")


#연습문제 9장
import sys

x = input("패스워드를 입력하시오: ")

a = ['a', 'b', 'c']
b = ['1', '2', '3']
guess = 0

for q in a :
    for w in b :
        guess = q+w
        print(guess)
        if guess == x :
            print("당신의 암호는", guess, "입니다.")
            sys.exit()
print("암호를 찾지 못했습니다.")
"""
