#컴과코 10장
#화씨 섭씨 변환기
from tkinter import *

def process():
  temperature = float(e1.get())
  #e1,get()은 e1.Entry에 사용자가 입력한 값을 "문자열"로 가져옴
  mytemp = (temperature-32)*5/9
  e2.insert(0,str(mytemp))
  #e2.insert(0, "100")
  #인덱스 0(맨 앞)에 100을 삽입
  #이미 ABC가 입력되어 있는 상태면 100ABC가 됨

window = Tk()

L1 = Label(window, text="화씨", font='Helvetica 16 italic')
#헬베티카 폰트 크기 16, 이텔릭(기울임꼴) 스타일로 지정
#L1.pack() pack은 버튼이 보이게 하는 것
L2 = Label(window, text="섭씨", font='Helvetica 16 italic')
#L2.pack()
#Label이라는 라벨에 화씨라는 이름을 붙여서 내놓기
L1.grid(row=0, column=0)
L2.grid(row=1, column=0)

e1 = Entry(window, bg="yellow", fg="black")
#bg = background 배경을 노란색으로 지정, fg = foreground 글자 색상을 검은색으로 지정
e2 = Entry(window, bg="yellow", fg="black")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
#Entry는 입력칸을 만든 것
#e1.pack()
#e2.pack()

b1 = Button(window,text="화씨->섭씨", command=process)
b2 = Button(window, text="섭씨->화씨")
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
# b1.pack()
# b2.pack()

window.mainloop()
l1.pack()이건 적층이고
l1.grid(어쩌고)이건 격자
l1.place(x=0, y=0)이건 절대

# 배치 관리자
# 적층 : 수직이나 수평으로 쌓아서 배치
# 격자 : 격자 모양으로 배치
# 절대 : 절대 좌표를 사용하여 배치
# 행과 열 사용


버튼 이벤트 처리
def process():
  print("안녕하세요?")

window = Tk()
button = Button(window, text="클릭하세요!", command=process)
#process라는 함수를 만들어서 command 시키기, process함수 실행
button.pack()
window.mainloop()

#절대 위치 배열
window = Tk()
#window.title("화씨 섭씨 변환기")창 위에 뜨는 이름을 바꿔줌
w = Label(window, text="박스 #1", bg="red", fg="white")
w.place(x=0, y=0)
w = Label(window, text="박스 #2", bg="green", fg="black")
w.place(x=20, y=20)
w = Label(window, text="박스 #3", bg="blue", fg="white")
w.place(x=40, y=40)

window.mainloop()
#메인루프는 실행하고 여기서 멈추고 닫으면 그 다음 창이 생성됨
#window = Tk()
#이거는 Tk라는 창을 생성하는 것


#이미지 변환
def change_img(): 
  path = inputBox.get()#입력값을 저장함
  img = PhotoImage(file = path) #PhotoImage는 lable, button에 이미지를 넣고자 할 때 사용, gif, pgm, ppm만 사용
  imageLabel.configure(image = img)#표시 이미지 변경. 아래의 행 내용과 같이 써야됨 
  imageLabel.image = img#이미지 파일은 프로그램과 동일 폴더에 아니면 절대 경로를 써야

window = Tk()

photo = PhotoImage(file="wl.gif")
imageLabel = Label(window, image=photo)
imageLabel.pack()

inputBox = Entry(window)
inputBox.pack()

button = Button(window, text='submit', command=change_img)
button.pack()
  
window.mainloop()

#캔버스 위젯
# window = Tk()

# canvas = Canvas(window, width=300, height=200)
# canvas.create_oval(x0, y0, x1, y1)#타원을 그리는 함수

#Mypaint프로그램
mycolor = "blue"

def paint(event):
  x1, y1 = (event.x-1), (event.y-1)
  x2, y2 = (event.x+1), (event.y+1)#x1y1점과 x2y2를 끝점?대각선점?으로하는 아주 작은 타원 생성
  canvas.create_oval(x1, y1, x2, y2, fill = mycolor, outline=mycolor)
  #fill은 타원 안을 칠하는 것, outline은 타원의 선 색

def change_color():
  global mycolor
  if mycolor == "blue":
    mycolor = "red"
    button.config(text=mycolor)
  else :
    mycolor = "blue"
    button.config(text=mycolor)
#global은 함수 안에서 지역변수가 아닌 전역변수를 가져다 쓰겠다는 뜻

window = Tk()

canvas = Canvas(window)
canvas.pack()
canvas.bind("<B1-Motion>", paint)#B1을 활용하여 드래그 중인 좌표를 계속 추적, 해당 좌표에 작은 타원을 계속 그림
#왼쪽 버튼을 누른 상태에서 마우스 이동을 감지

button = Button(window, text=mycolor, command=change_color)
button.pack()

window.mainloop()


#계산기 프로그램
window = Tk()

window.title("My Calculator")

display = Entry(window, width=33, bg="yellow")
display.grid(row=0, column=0, columnspan=5)
#columnspan=5는 5개의 컬럼을 1개로 합침, 즉 가로로 길게 늘어뜨림

button_list = [
'7', '8', '9', '/', 'c', #row_index = 1
'4', '5', '6', '*', '',  #row_index = 2
'1', '2', '3', '-', '',  #row_index = 3
'0', '.', '=', '+', ''   #row_index = 4
]

#row_index는 행 인덱스고 #col_index는 열인덱스

row_index = 1
col_index = 0

def click(key):
  if key == "=":
    result = eval(display.get()) #괄호 안의 식의 계산결과 얻음
    s = str(result)
    display.insert(END, "=" + s)
  elif key == "c" :
   display.delete(0, END)
  else :
   display.insert(END, key) #끝에 key를 추가

# '7'을 처리할 버튼을 만드는 중...
# 1. t='7'을 기억하는 [process 함수]를 만듦
# 2. [Button 객체]를 만듦
# 3. [Button 객체]의 'command' 속성에 [process 함수]를 저장함
for button_text in button_list :
  def process(t=button_text):
    click(t)
  Button(window, text=button_text, width=5,
  command=process).grid(row=row_index, column=col_index)
  col_index += 1
  if col_index > 4:
    row_index += 1
    col_index = 0
#버튼 리스트 안에 있는 값을 버튼 텍스트에 넣으면서 포문을 반복
#포문 값에 따라 버튼이 격자 위치에 맞춰서 생성됨
#버튼을 클릭하면 command가 실행되면서 프로세스 함수가 실행됨
#process함수는 버튼텍스트 값을 t로 지정하고 t가 입력된 클릭 함수가 실행됨

#첫 번째 루프 button_text ='7'
#컴퓨터는 첫 번째 process함수를 만듬 이 때 t=7이라는 내용을 함수 내부에 넣기
#두 번째 루프 button_text ='8'
#이 때 t='7'이라는 내용을 함수 내부에 넣어
#컴퓨터는 두 번째 process 함수를 완전히 새로 만듦
#이 때 t='8'이라는 내용을 함수 내부에 넣어
#이 과정을 마지막 공백('')버튼까지 20번 반복
window.mainloop()

def process():
  x = int(e1.get())
  y = x * 1.609
  e2.insert(0, str(int(y))+" km")

window = Tk()
l1 = Label(window, text="마일")
l2 = Label(window, text="킬로미터")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(window, text="변환", command = process)
b1.grid(row=2, column=0)
  
window.mainloop()


import random
x = random.randint(1,100)

def process():
  y = int(e1.get())
  if x == y :
    l2 = Label['text'] = Message
  elif x < y :
    l2 = Label['text'] = Message
  else :
    l2 = Label['text'] = Message

def process2():
  e1.insert(0, "")

window = Tk()

l1 = Label(window, text="Guessing game")
l1.grid(row=0, column=0)

e1 = Entry(window)
e1.grid(row=1, column=0)

b1 = Button(window, text="guess", command=process)
b2 = Button(window, text="reset", command=process2)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)

window.mainloop()


window = Tk()
i = 1

def process():
  global i
  x = e1.get() + "\n"
  e2.insert(END, f"[ #{i}]" + x)
  i += 1

l1 = Label(window, text="할일을 입력하세요")
l1.grid(row=0, column=0)

e1 = Entry(window)
e1.grid(row=1, column=0)

b1 = Button(window, text="추가", command=process)
b1.grid(row=2, column=0)

e2 = Text(window, height=5, width=25, font=("Arial"))
#Text위젯은 여러 줄의 텍스트를 표시할 때 사용
e2.grid(row=3, column=0)

window.mainloop()