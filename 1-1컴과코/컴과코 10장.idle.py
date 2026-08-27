#컴과코 10장

#버튼이 있는 윈도우 생성
from tkinter import *
#tkinter 모듕 ㄹ안의 모든 * 함수를 포함하라는 의미
#모듈 안에 함수 사용시 모듈의 이름을 앞에 붙이지 않아도 됨
window = Tk()
#Tk()는 다양한 위젯들을 담을 윈도우 창 생성, window라는 이름을 붙인 것
button = Button(window, text="클립하세요!")
#window라는 윈도우에 "클릭하세요!"라는 버튼 생성
button.pack()
#pack()을 사용하지 않으면 버튼이 나타나지 않음
window.mainloop()
#윈도우에서 발생하는 여러가지 이벤트를 처리하는 함수


#엔트리와 레이블 위젯
from tkinter import *

window = Tk()

l1 = Label(window, text="화씨")
l1.pack()
e1 = Entry(window)
e1.pack()
