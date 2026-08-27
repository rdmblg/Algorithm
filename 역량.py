#아이러브커피
# S = input("")
# if S[-6:] == "coffee" or S == "blacktea" :
#   print("Yes")
# else :
#   print("No")


#소수 개수 구하기
x, y = map(int, input().split()) #공백 기준으로 쪼개기
#'10', '20'으로 자름
#map은 여러개를 한꺼번에 변환, 10과 20을 int로 같이 변환
#map(적용할 함수, 데이터 묶음)
#split은 변수.split() 이렇게 쓰기
#쪼갠 후 리스트에 반환
count = 0
product = 0

for i in range(x, y+1):
  for z in range(1, i):
    if i % z == 0:
      product += 1
  if product == 2 and i % i == 0 and i % 1 == 0 :
    count += 1
  product = 0

#i라는 범위 안에서 z라는 수로 나누기, z에 1을 더해가면서 범위 내에서 반복
#나누었을 때 나머지가 0이면 product(나머지)에 1 더하기
#최종 나머지의 갯수가 2이고 자기자신, 1로 나누었을 때 0이 나오면 소수 변수(count)에 1 더하기
#나누기 반복을 끝내면 product를 0으로 초기화한 후 다시 반복
  
print(count)


#빈숫자찾기
x = input("")
X = x.replace(" ", "") #replace는 특정 공간?을 다시 재배치하는 것
for i in range(11):
    if str(i) not in X:
        print(i)
        break

#마카롱 개수 세기
N = int(input(""))
X = input("")
count = 0
for i in range(N):
    if X[i:i+3] == "(I)":
        count += 1
print(count)


#카드 뒤집기
N, T = map(int, input().split())
listt = [1] * (N+1)
#1이 앞면 0이 뒷면

for i in range(1, T+1):
  for v in range(1, i+1):
    if i % v == 0:
      if listt[v] == 1 :
        listt[v] = 0
      else :
        listt[v] = 1
#0부터 시작하면 계산하기 어려우니까 N+1을 하고 인덱스 0값을 제외함
print(listt[1:].count(1))


#완벽한 삼각김밥
count = 0
listtt = [90, 30, 2]
x = int(input(""))

for i in listtt:
  count += x // i
  x %= i #x는 i로 나누었을 때의 나머지

if x != 0 :
  print(-1)
else :
  print(count)

