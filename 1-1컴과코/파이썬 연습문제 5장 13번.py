#5.13
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
