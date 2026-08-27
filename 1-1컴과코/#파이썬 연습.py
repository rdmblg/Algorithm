# 파이썬 연습
# for i in range(1, 9, 2):
#   print(i)
#1포함, 1부터 8까지

# for i in range(5):
#   print(i)
# #5번 반복하는거
# #i가 0부터 4까지 변경

# for i in [1, 2, 3]:
#   print(i)

# for i in range(1, 5):
#   print(i, end="")
#   #범위를 지정하면 포함, 지정이 아니라 숫자만 있으면 포함이 아님

# import time
# for i in range(5, 0 ,-1):
#   print(f"{i}초 남았습니다.")
#   time.sleep(1)

# x = int(input("구구단:"))

# for i in range(1, 10):
#   print(f"{x}*{i}=", x*i)

x = ""

# while x != "python":
#   x = input("암호를 입력하시오: ")
# print("로그인 성공")

# count = 0
# summ = 0

# while count != 10:
#   count+=1
#   summ += count
# print(summ)

# x = ""
# y = 0
# summ = 0

# while x != "no":
#   y = int(input("숫자를 입력하시오 :"))
#   summ = summ + y
#   x = input("계속?(yes/no): ")
# print(f"합계는? : {summ}")

# def avc(a):
#   print(a, "안녕하세요")

# avc("사장님,")

# def print_address(name):
#     print("어쩌라고용")
#     print("용용죽겠징")
#     print(name)
#     return "성공!"
  #얘는 위에서부터 프린트하고 따로 리턴 값을 다시 밖으로 내놔서 여러 개가 나오는 것
# y = print_address("바보")
# print(y)

# def calculate_area(radius):
#     area = 3.14*radius**2
#     return area
# #얘는 위에서 계산 한 값을 그대로 리턴에 넣어서 리턴 값을 밖으로 반환한 후 프린트
# c_area = calculate_area(5.0)

# print(c_area)

# s = "Hello World!"
# print(len(s))

letter = ['A','B','C']
# print('A' in letter)

# print('e' in 'Hello')

# for i in letter:
#     print(i)

# letter[1] = 'BB'

# print(letter)

# letter.append("D")
# print(letter)

# letter.insert(1,"B")
# print(letter)

phone = {"홍채운" : "바보", "도해연" : "1345", "정진희" : "1456"}
print(phone["홍채운"])

# x = letter.pop(0)
# #값을 빼내서 x라는 변수에 따로 저장한것
# print(letter)
# print(x)

text = "속담을 저장한 파일"
result = text.split()
print(result)

if "A" in letter:
    x = letter.index("A")

print(x)

# from tkinter import *
# import random
# x = random.randint(1, 100)

# def process():
#   y = e1.get()
#   if x != y :
#     l2 = Label(window, text="땡!")
#     l2.grid(row=3, column=0)
#   else :
#     l3 = Label(window, text="정답!")
#     l3.grid(row=3, column=0)


# window = Tk()

# l1 = Label(window, text="GUESSING GAME", font=10, bg="yellow", fg="blue")
# e1 = Entry(window)
# l1.grid(row = 0, column=0)
# e1.grid(row=1, column=0)

# b1 = Button(window, text="GUESEE", command=process)
# b1.grid(row=2, column=0)
# b2 = Button(window, text="RESET")
# b2.grid(row=2, column=1)

# mainloop()
