
# x = max(1, 2, 3)
# print(x)
#  #max는 괄호 안에 넣어준 시퀀스에서 최댓값을 반환
#  #min은 괄호 안에 넣어준 시퀀스에서 최소값을 반환



# 파이썬 자료형
# bool(논리형)flag=True
# boolen변수, 참 거짓을 나타냄 True, False로 표현됨
# flag=대표 불변수

# list(리스트) arr=[1, 2, 3]
# tuple(튜플) t=(1,2)
# dict(딕셔너리) d={"a":1}
# set(집합) s={1,2,3}
# Nonetype x = None
# T
# flag=True
# #flag=not flag
# print(flag)
# print(type(flag))

# if flag:
#   print("True입니다.")

# else:
#   print("flase입니다.")

# flag=True
# #flag=True가 무조건 맞는 것은 아니고 이름을 나타내는 조건이 처음에 참인지 거짓인지 따지기
# flag=not flag
# #not은 값을 반전(토글)시키는 연산자
# #not을 쓰려면 우선 flag(bool)변수를 선언해줘야함
# print(flag)
# flag=not flag
# print(flag)
# flag=(1>0) #True로 평가됨
# flag=bool(0) #false로 평가됨

# def solution(a, b, flag):
#   if flag: 
#     return a+b
#   return a-b
# #flag값을 입력받고 값에 따라서 리턴 값을 정하는 것
# #return을 else로 활용

# list안의 값이 true일 때 실행하도록 하기
# if included[i]:
#     조건



# 등차수열 x = a+(d*i)




# eval() = 파이썬에서 문자열로 표현된 파이썬식을 실행하는 함수, 문자열을 파이썬 코드로 해석하여 실행, 결과 반환
# eval(expression, globals=None, locals=None)
# expression 실행할 파이썬 표현식이 담긴 문자열, 숫자 계산식 변수 연산식 등
# globals(선택) expression이 실행될 때 사용할 전역 변수 딕셔너리, 기본값은 None
# locals expression이 실행될 때 사용할 지역 변수 딕셔너리, 기본값은 None
# x =10
# result = eval('x + 5')
# print(result) #출력 : 15
# #근데 보안 위험이 큼
# ast.literal_eval() 리터럴값만 처리할 수 있고 임의의 코드 실행을 하지 않음
# import ast
# result = ast.literal_eval("[1,2,3]")
# print(result) #출력: [1,2,3]
# 사용 사례 1. 동적계산(문자열로 전달된 수식을 계산하는 경우)
#           2. 동적 변수 설정(변수명을 동적으로 생성하여 값 할당이 필요한 경우)
#           3. 리팩토링(복잡한 코드나 표현식을 동적으로 생성하거나 수정해야하는 경우)
#           4. 인터프리터나 스크립트 시스템(사용자가 입력한 수식을 실행해야 하는 경우)

# code = "print(1+2)"
# exec(code) 문자열이 실제 코드처럼 출력됨, 3




# 문자열 처리
# 문자열 처리가 중요한 이유
# :실무 데이터는 대부분 가공이 필요, 문자열을 분해하고 정리해야 데이터로 사용 가능

# 1. 슬라이싱:위치 기반으로 데이터 분리
# a = "strogman"
# year = "20260424"
# print(a[:4])
# print(a[-2:])
# print(year[:4])
# 뒤에서부터 셀 때는 -붙여서 세기, a[-1] = 'n'


# 2.replace:특정 문자를 다른 문자로 바꿈
# a = "엥이 게 뭐지 히히 히히 히"
# a.replace(" ", "")
# '엥이게뭐지히히히히히'
# a = "실험 용 입니다."
# a = a.replace("실험", "연습")
# print(a)
# 예)특수문자 제거, 공백 제거, 구분자 변경, 데이터 정리, 오류 데이터 수정, 불필요한 요소 제거


# 3. 문자열 분리
# a = "엥이 게 뭐지 히히 히히 히"
# a.split(' ')
# ['엥이', '게', '뭐지', '히히', '히히', '히']
# split은 구분자를 기본으로 문자열을 나눔, 리스트 형태로 분리됨
# 예 )코드와 명칭 분리, 날짜 분리, 구조를 나눔
# a = "2026-04-26"
# aa = a.split('-')
# print(aa)
# ['2026', '04', '26']

# 변수에 저장하면서 동시에 리스트를 만듦
# 날짜 추출은 dt함수로도 할 수 있음(dt함수가 뭐지)
# *어떤 문자열 기준이 아니라 그냥 나누고 싶은거면 리스트 쓰기


# join 함수
# a = ['감자', '고구마', '양파', '당근] #감자고구마양파당근
# print("".join(a))
# 문자열로만 구성된 리스트에서 사용 가능, 다른 자료형이 리스트 내에 포함되면 에러 발생


# remove
# :값을 제거함
# list.remove(값)


# pop
# :위치로 제거함
# list

# 실무에서는 순서가 중요
# replace로 불필요한 문자 제거, split으로 구조를 분리, 슬라이싱으로 필요한 부분 추출
# split같은 걸로 나누기도 애매하고 그냥 위치(글자 수)로 뭉텅이로 잘라야할 때 슬라이싱을 씀
# a = "나는 -지금 -똥이 -마렵다"
# aa = a.replace(" ", "").split('-')
# print(aa)  #['나는', '지금', '똥이', '마렵다']
# print(aa[0], aa[1], aa[2], aa[3]) #나는 지금 똥이 마렵다


# def solution(ineq, eq, n, m):
#   return int(eval(str(n)+ineq+eq.replace('!', ''+str(m))))
# 예를 들어 3>!2 == 3>2 이렇게 계산이 됐다고 하면
# eval("3>2")가 나오는데 3>2는 비교 연산이고 비교 연산의 결과는 숫자가 아니라
# True or False임!!!!!!!!!!!
# 여기에서 int()로 묶으면 True는 1이 되고 False는 0이 됨

# 자주 발생하는 문제
# 1. 잘못된 구분자: 문자열 분리 실패
# 2. 공백 포함: 데이터 불일치
# 3. 문자열 길이 불일치: 슬라이싱 오류
# 데이터마다 길이가 다르면 문제가 생김
# 날짜 = "20260426"
# 날짜 = "2026426"
# year = 날짜[0:4]
# month = 날짜[4:6]
# year는 정상인데 month는 42가 나옴 -> 그럼 날짜가 달라짐
# 월은 항상 2자리일 것이다 라고 가정하고 [4:6]처럼 위치로 잘랐는데 실제 데이터가 그 가정이 깨지면 엉뚱한 글자가 잘려서 나온다는 뜻




# 삼항 연산자
# 1. 구조를 정확히 나누기
# 조건이 참일 때 선택되는 값(참값)
# 참 또는 거짓으로 판단되는 식(조건)
# 조건이 거짓일 때 선택되는 값(거짓값)
# *한개라도 빠지면 안됨, if와 else는 같이 사용됨, 조건 자리에는 True or False로 판단되는 식이 와야함

# 2. 실행 순서
# 조건을 먼저 평가하여 조건 결과에 따라 True는 앞의 값 False는 뒤에 값을 평가
# True면 앞의 값 선택 False면 뒤의 값 선택
# if앞에는 참일 때 사용하는 값이 옴

# 참값 if 조건 else 거짓값

# 예제
# result = '합격' if score >= 60 else '불합격'

# def solution(code):
#     mode = 0
#     ret = ''
#     for i in range(len(code)):
#         if code[i] == '1':
#                 mode = 1 if mode == 0 else 0
#                 continue
#         if mode == 0 and i % 2 == 0:
#             ret += code[i]
#             print(mode)
#         if mode == 1 and i % 2 != 0:
#             ret += code[i]
#             print(mode)
#     return "EMPTY" if ret == '' else ret

# 만약 continue가 없으면 if가 실행됨, 1이 모드만 바꾸는게 아니라 ret에 들어갈 수 있음
# continue를 넣어서 반복문을 한번 더 실행하는 것


# def solution(code):
#     return "".join(code.split("1"))[::2] or "EMPTY"
    
# 1. split기준으로 나누니까 1이 사라질때마다 인덱스가 당겨짐 -> 토글됨
# == 모드를 토글하면서 짝/홀을 따라가는 복잡한 로직을 지우면 그냥 남은 글자들 중
# 첫번째, 세번째, 다섯번째를 고르는 것과 동치임........
# 2.[::2]이거는 시작과 끝을 생략, 간격만 2로 지정[시작:끝:간격]
# 3.AorB에서 A가 참취급이면 A를 리턴, A가 거짓취급이면 B를 리턴
# #시발뭐임




# #set 함수
# s1 = set("HELLO")
# print(s1)

# 1st = [1,2,2,3]
# st = set(1st)
# print(st) #{1,2,3}

# 활용 예시 : 중복제거, 두 데이터 비교, 포함 여부 확인

# a = {1,2,3}
# b = {2,3,4}

# print(a & b) #{2,3} 교집합
# a.intersection(b) #위랑 같은 결과
# print(a | b) #{1,2,3,4} 합집합
# a.union(b) #위랑 같은 결과
# print(a - b) #{1} 차집합, a의 원소 중에서 b에 들어있는 원소를 제외하고 남은 것, 순서가 바뀌면 결과도 달라짐
# a.difference(b) #위랑 같은 결과

# 예제
# check=len(set([a,b,c]))
# #a, b, c를 입력받고 중복되는 수 찾기




# 리스트 컴프리헨션 : 반복을 이용해 새로운 리스트를 간결하게 생성하는 문법
# #코드가 깔끔해져서 읽기 쉽고, 내부적으로 속도가 빨라서 씀
# #기존 방식
# r = []
# for i in range(5):
#     r.append(1)

# print(f"r:{r}")

# #컴프리헨션
# r = [i for i in range(5)]
# print(f"r:{r}")

# #핵심 개념
# #반복 +수집, 반복 결과를 자동으로 리스트에 모음, 항상 새로운 리스트를 반환
# #원본 데이터는 수정지 않음
# #리스트 컴프리헨션은 새로운 반복문이 아닌 기존 반복문의 축약 문법
# #결과는 항상 <class 'list>
# #단순 반복이 아니라 데이터 변환이 핵심

# r = [x*10 for x in [1,2,3] #[10,20,30]
# #결과를 자동으로 수집하여 리스트로 만듦
# #입력 -> 반복 -> 변환 -> 출력

# numbers = [1,2,3]
# r = [x*2 for x in numbers] #[2,4,6]

# [] : 결과를 리스트로 생성
# 표현식(예시 : i) : 리스트에 저장할 값
# for : 반복 수행
# 변수 : 반복시 값 저장
# in : 반복 대상에서 값 꺼냄
# 반복가능객체(range(5)) : 반복할 대상

# 반복가능객체 -> 값 꺼내기 -> 변수 저장 -> 표현식 계산 -> 리스트 저장

# #이게뭐지
# #표현식의 다양한 활용
# 1. 리터럴 [100 for x in range(3)] -> [100, 100, 100]
# 2. 변수 [x for x in range(5)] -> [0, 1, 2, 3, 4]
# 3. 산술 [x**2 for x in range(5)] -> [0,1,4,9,16]
# 4. 비교 [x>2 for x in range(5)] -> [f,f,f,t,t] #false, true
# 5. 논리 [(x>1) and (x<4) for x in range(6)]
# 6. 조건(삼항) ["짝수" if x%2 == 0 else "홀수" for x in range(5)]
# 7. 함수 호출 [abs(x) for x in [-3, -2, -1, 1, 2]]
# 8. 메서드 호출 [name.upper() for name in names]
# 9. 속성 접근 [p.name for p in people]
# 10. 인덱스/슬라이싱 [word[0] for word in words], [word[:3] for word in words]
# 11. 언패킹 [a+b for a, b in pairs]
# 12. f-string [f"번호:{x} for x in range(3)"]
# 13. walrus 연산자 [(y:x*2) for x in range(5)] #월루스? 이게뭐임
# 14. 컬렉션 생성 [(x, x*2) for x in range(5)], [{"num":x} for x in range(3)]
# 15. 중첩 컴프리헨션 [[y for y in range(3) for x in range(2)]]


# 리스트 컴프리헨션 조건 필터링
# #반복문으로 데이터를 순회하면서 조건에 맞는 값만 골라 새로운 리스트를 만드는 기능
# [표현식 for 변수 in 반복가능객체 if 조건]

# 예제
# n = [1,2,3,4,5]
# result = [n for n in numbers if n %2 == 0] #[2, 4]

# 실행 순서
# 반복문 실행 -> 값 꺼내기 -> 조건 검사 -> 조건이 true면 표현식 실행, 리스트에 추가
# -> 조건이 false 면 제외

# 함수 결과 사용
# def is_even(n): return n % 2 == 0
# [n for n in range(10) if is_even(n)]

# 메서드 활용
# word =["apple", "banana", "airplane", "melon", "avocado"]
# [w for w in word if w.startswith("a")]
# word라는 리스트를 돌면서 단어를 담고 a로 시작하는지(startswith) 검사해서 참인것만 골라냄


# 고급활용
# 1. 객체 속성 조건
# [user.name for user in users if user.active]
# #이게뭐지
# 1. for user in users
# 2. if user.active #active상태가 True인지 검사, 탈퇴했거나 휴면 계정인 사용자는 필터링됨
# 3. user.name #사용자의 정보를 다 가져오는게 아니라 이름 속성만 결과 리스트에 담겠다는 뜻

# # 이해를 돕기 위한 가상의 사용자 객체 리스트
# users = [
#     {"name": "민수", "active": True},
#      {"name": "철수", "active": False},  # 휴면 유저
#     {"name": "영희", "active": True},
# ]

# # 위 구조를 다루는 실제 코드 예시
# result = [user['name'] for user in users if user['active']]

# print(result)
# # 출력: ['민수', '영희']

# #users의 딕셔너리 하나가 순회를 돌면서 user에 담김, user['name']은 순회를 돌면서
# #만들어진 user딕셔너리에서 name(키)에 맞는 값을 찾아서 반환하는 것
# #(만약 user['active']값이 True라면)


# 2. enumerate 조건
# [v for i, v in enumerate(data) if i%2==0]
# enumerate() : 인덱스 번호도 같이 필요할 때 사용
# for i, v in enumerate(data) : data리스트를 돌면서 인덱스 번호는 i에 담고 실제 값은 v에 담기


# 3. zip 조건
# [name for name, score in zip(names,scores) if score>=80]
# zip() : 같은 인덱스의 요소끼리 하나로 묶어주는 역할
# for name. score in zip(names, scores) : 짝지어진 데이터를 순서대로 꺼내서 이름은 name에 점수는 score변수에 각각 나눠담기

# names = ["민수", "철수", "영희", "길동"]
# scores = [85, 60, 95, 75]

# # 80점 이상인 사람의 이름만 추출
# pass_students = [name for name, score in zip(names, scores) if score >= 80]

# print(pass_students)
# # 출력: ['민수', '영희']


# 4. 딕셔너리 조건
# [k for k, v in data.items() if v>= 20]
# #data.items() 딕셔너리 안에 있는 키와 벨류를 쌍으로 묶어서 하나씩 꺼내옴
# #키는 k변수에, 벨류는 v변수에 각각 담기


# 5. 집합 조건
# [n for n in numbers if n%2==0]
# #for n in numbers : numbers라는 숫자 모음에서 숫자를 하나씩 꺼내 n 변수에 담기


# 6. 다중if
# [x for x in range(20) if x > 5 if x < 15]
# #if를 나란히 쓰면 and연산자로 묶은것과 똑같이 작동함

# [x for x in range(100) if x > 10 if x <90 if x % 2 == 0]
 

# 7. 중첩 반복문과 조건
# [(x,y) for x in range(3) for y in range(3) if x == y] 

# result = []
# for x in range(3):
#     for y in range(3):
#         if x == y:
#             result.append((x, y))

# #조건 위치와 그룹화
# if 위치에 따라 필터링 범위가 달라짐
# [(x, y) for x in range(3) for y in range(3) if x > 1]

# [(x, y) for x in range(3) if x > 1 for y in range(3)]

# #복잡한 조건은 괄호로 그룹화하여 가독성 확보
# [
#     x for x in range(100) 
#     if (x % 2 == 0 and x > 50) or (x % 3 == 0)
# ]


# 8. short-circuit 평가(단락 평가)
# if x is not none and x > 0
# 참 취급 : 알맹이가 있는 것들
# 거짓 취급 : 텅 비어있는 것들(none, 0, "")


# 9. walrus 연산자
# length for word in words if (length :=len(word))>5
# :=는 x에 값을 저장후 if조건문에 값을 반환해줌


# 10. 예외 방지 필터링
# [int(x) for x in data if x]
# #리스트에 none이라고 적혀있거나 빈 문자열은 걸러짐
# #파이썬은 if 조건문 뒤에 어떤 값이 오면 그게 True/False가 아니더라도
# #알맹이가 있으면 참, 텅 비어있으면 거짓으로 판정함


# #삼항 연산자와 리스트 컴프리헨션의 차이
# #삼항 연산자 : A, B중 하나를 고름
# #리스트 컴프리헨션 : 조건에 맞는걸 모아 리스트로 만듦


# #잘못된 코드
# [x for x in data if x : 0 else 0 ]
# #1. 컴프리헨션에서 맨 뒤에 오는 if는 데이터 중에서 조건에 맞는 것만 남기고 나머지는 버리는 필터 역할
# #2. 근데 esle 0 을 넣으니까 오류가 남. 필터링하라는거야 0으로 바꿔서 넣으라는거야?

# #옳은 코드
# [x if x > 0 else 0 for x in data]
# #1. x가 0보다 크면 그대로 담기, 0보다 작거나 같으면 0으로 바꿔서 리스트에 담기

# #정리
# #데이터를 조건에 맞춰 버리고(필터링) 싶으르 때 : if를 맨 뒤에 쓰기
# #데이터를 버리지 않고 조건에 맞춰 값만 바꿔치기 하고 싶을 떄 : if-else를 맨 앞에 쓰기
# #조건 필터링(if):조건 불만족 -> 데이터 제거
# #조건식(if-else) : 조건에 따라 다른 값 생성, 데이터 유지

# # 정적은 코드를 작성할 때 이미 정해지는 것, 동적은 프로그램이 실행되는 도중에 정해지는 것
# # 정적 flag = True
# # 동적 flag(사용자 입력>0)


# 2차원 리스트
# #리스트 안에 리스트가 들어 있는 것

# def solution(num_list):
#     if num_list[-1] > num_list[-2]:
#         num_list.append(num_list[-1] - num_list[-2])
#     else :
#         num_list.append(num_list[-1]*2)
#     return num_list

# 1. 이 식에서 else를 if로 대체하면 먼저 실행된 리스트에 새로운 값이 추가됨..
# 2. 방금 바뀐 리스트를 기준으로 조건을 새로 검사함 -> 오류

# 이차원 리스트 1차원으로 만들기
# litt = sum(listt, [])


# #count
# ooyyy.count('y')
# 3


# 리스트 정렬하기
# a.sort()

# 새로운 정렬된 리스트를 만들기
# sorted([5, 2, 3, 1, 4])


# 딕셔너리
# :키와 값을 짝지어 저장하는 자료형
# {키:값} 형태로 씀

scores = {"국어" : 90, "영어":85}
print(scores["영어"]) #키로 값 찾기, 85)

# 값을 추가하거나 수정하는 방법
scores["과학"] = 80  # 추가
scores["영어"] = 88  # 수정
del scores["국어"]  #삭제
print("수학" in scores) #키가 있는지 확인

#없는 키를 대괄호로 접근하면 오류가 남, 안전하게 꺼낼 때는 get()을 씀
print(scores.get("미술", 0)) #없으면 기본값 0 반환

for subject, score in scores.items():
  print(subject, score)

#.items()는 키 값을 변수 안에 넣어주는건가봄
#딕셔너리의 키로는 문자열, 정수, 튜플처럼 바뀌지 않는 자료형만 쓸 수 있음


#집합
#집합(set)은 중복을 허용하지 않고, 순서가 없는 원소들의 모음, 중괄호{}로 만들되 값만 나열

fruits = {"사과", "배", "사과"}
print(fruits) #중복이 사라짐 {'사과', '배'}

a = {1, 2, 3}
b = {3, 4, 5}
a.add(6)  #추가
a.discard(2)  #삭제(없어도 오류 없음)
print(a | b) #합집합{1, 3, 4, 5, 6}
print(a & b) #교집합{3}
print(a - b) #차집합{1, 6}

#집합은 중복을 제거하거나 어떤 값이 들어 있는지 빠르게 확인할 때 유용

#딕셔너리와 집합은 내부적으로 해시라는 방식을 이용
#포함 여부를 자주 확인해야 한다면 리스트보다 집합이나 딕셔너리가 유리



#break
#반복문을 즉시 종료할 때 사용
for i in range(1, 6):
  if i == 3:
    break
  print(i)

# 1, 2


#continue

for i in range(1, 6):
  if i == 3:
    continue
  print(i)

# 1, 2, 4, 5
# 3일 때만 print를 건너뛰고 4부터 다시 실행함


#함수와 매개변수
#함수는 특정 작업을 수행하는 코드 묶음에 이름을 붙인 것
#def 키워드로 정의, 이름을 불러 호출함

def greet():
  print("안녕하세요")

greet()

#한 번 정의해 두면 같은 코드를 다시 쓰지 않고 이름만 불러 여러 번 사용할 수 있음


#매개변수와 인자
#함수는 외부에서 값을 받아 동작할 수 있음.
#함수를 정의할 때 받기로 한 변수를 매개변수, 호출할 때 실제로 넘기는 값을 인자라 함

def greet(name): #name은 매개변수
  print(name + "님, 안녕하세요")

greet("홍길동") #"홍길동"은 인자

#매개변수는 여러 개를 둘 수 있으며 넘긴 순서대로 짝지어짐
def add(a, b):
  print(a + b)

add(3, 5) #a=3, b=5, 8


#반환값
#함수가 계산한 결과를 호출한 쪽으로 돌려줄 때 return을 씀.
#반환된 값은 변수에 담거나 다른 식에 바로 쓸 수 있음.

def add(a, b):
  return a + b

result = add(3, 5)
print(result) #8

#return이 없는 함수는 특별한 값인 None을 돌려줌
#또한 여러 값을 한꺼번에 반환하면 3.2에서 본 튜플로 묶여 전달됨

def min_max(numbers):
  return min(numbers), max(numbers)

low, high = min_max([4, 1, 8, 3])
print(low, high)
print(low)
print(high)

#기본값과 키워드 인자
#매개변수에 기본값을 정해 두면, 호출할 때 그 인자를 생략할 수 있다.
def greet(name, greeting="안녕하세요"):
  print(name + "님, " + greeting)

greet("홍길동")
greet("홍길동", "반갑습니다")

#또한 어떤 매개변수에 넣을지 이름을 직접 지정해 넘기는 키워드 인자를 쓰면
#순서와 무관하게 값을 전달할 수 있어 코드가 명확해진다.

def greet(name, hi, bye):
  print(name, hi, bye)

greet(hi="안녕하세요", bye="안녕히가세요", name="저는 미미입니다.")
#키워드인자: 위처럼 입력 순서 상관없이 매개변수의 이름을 지정해서 인자를 정하는 것

#함수 안에서 만든 변수는 그 함수 안에서만 유효한 지역 변수
#함수가 끝나면 사라지며, 함수 밖에서는 사용할 수 없다.
#함수끼리 값을 주고 받을 때는 매개변수로 받고 return으로 돌려주는 방식을 쓰는 것이 안전