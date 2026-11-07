#재귀
#종료 조건 : 더 이상 자기 자신을 호출하지 않고 곧바로 답을 줌
#재귀 단계 : 문제를 더 작은 같은 문제로 줄여 자기 자신을 호출하는 부분


# #팩토리얼 재귀로 옮기기
# def factorial(n):
#     if n == 0: #종료 조건 0! = 1
#         return 1
#     return n * factorial(n-1) # 재귀 단계 n! = n * (n-1)!

# # factorial(3)
# # = 3 * factorial(2)
# # = 3 * (2 * factorial(1))
# # = 3 * (2 * (1 * factorial(0)))
# # = 3 * (2 * (1 * 1))
# # = 6



# #함수에서 return다음에 아무것도 없으면 함수 중간에 빠져나옴

# #클래스는 데이터의 구조와 동작을 정의한 설계도
# #클래스로 실제로 만들어낸 실체를 객체 또는 인스턴스라고 함
# #하나의 클래스로 여러 개의 객체를 만들 수 있음.

# #객체는 자신만의 데이터인 속성과 메서드를 함께 가짐

# #클래스는 class 키워드로 정의
# #객체가 만들어질 때 호출되는 특별한 메서드인 _init_에서 속성을 초기화함

# class Student:
#     def __init__(self, name, score):
#         self.name = name #name 속성에 전달받은 값을 저장하라
#         self.score = score

# s = Student("홍길동", 90)
# print(s.name) #홍길동
# print(s.score) #90

# #파라미터(매개변수)
# # 1) 빈 객체 생성
# # 2) __init__(빈객체, "홍길동", 90) 자동 호출
# # 3) 그 빈객체.name = "홍길동", 빈객체.score = 90 저장됨
# # 4) 완성된 그 객체를 s에 넣어줌

# #Student라는 틀로 빈 객체를 하나 만들고 그 빈 객체를 채우기 위해 __init__함수를 실행함
# #객체 생성 + 초기화가 한 번에 일어남


# #메서드 : 클래스 안에 정의된 함수
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
    
#     def is_pass(self):
#         return self.score >= 60

# s = Student("홍길동", 90)
# print(s.is_pass())

# #ADT : 내부가 어떻게 구현됐는지는 감추고 무슨 기능을 하는지만 보여주는 데이터 형태
# #메서드 이름을 고정해두고 내부 구현을 나중에 다른 방식으로 갈아엎어도 된다는 뜻


# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def __str__(self):
#         return f"{self.name}({self.score}점)"

# print(Student("홍길동", 90))

# #__str__ 메서드를 정의하면 객체를 출력할 때 원하는 문자열을 보여줄 수 있음
# #자료구조의 내부 상태를 확인하며 디버깅할 때 유용


# #2차원 리스트, 격자
# grid = [
#     [1, 2, 3],
#     [4, 5, 6],
# ]

# print(gird[0][2]) # 0행 2열 3
# print(grid[1][0]) # 1행 0열 4

# #행의 개수는 len(grid)로 한 행의 열 개수는 len(grid[0])
# #행과 열의 개수가 달라도됨


# #값이 채워진 격자를 만들 때 흔히 저지르는 실수
# #[[0] * 3] * 2처럼 만들면 겉보기에는 두 행짜리 격자 같지만 두 행이 사실 같은 리스트 하나를 가리킴

# #잘못된 방법 : 모든 행이 같은 리스트를 가리킴
# wrong = [[0] * 3] * 2
# wrong = [0][0] = 1
# print(wrong) #[[1, 0, 0], [1, 0, 0]] #두 행이 함께 바뀜

# grid = [[0] * 3 for _ in range(2)]
# grid[0][0] = 1
# print(grid) #[[1, 0, 0], [0, 0, 0]] #한 행만 바뀜

# #_는 값을 따로 쓰지 않는 반복 변수에 관습적으로 붙이는 이름


# #격자 순회
# grid = [
#     [1, 2, 3],
#     [4, 5, 6],
# ]

# #행 단위로 꺼내기
# for row in grid :
#     print(row)

# #[1, 2, 3]
# #[4, 5, 6]

# #행 열 인덱스로 각 칸에 접근하기
# for r in range(len(grid)):
#     for c in range(len(grid[r])):
#         value = grid[r][c]


# #한 줄에 여러 값 입력받기
# # 입력: 3 5
# a, b = input().split()    # 공백 기준으로 나눠 두 문자열로
# a, b = int(a), int(b)     # 각각 정수로 변환
# print(a + b)              # 8

# # 입력: 3 5
# a, b = map(int, input().split())
# print(a + b)              # 8

# # 정수 여러 개를 리스트로 받기
# # 입력: 10 20 30 40
# numbers = list(map(int, input().split()))
# print(numbers)            # [10, 20, 30, 40]
# #map의 결과는 리스트가 아님

# #f-문자열
# print(f"평균:{(80 + 90 + 100) / 3:.2f}") #소수점 둘째 자리까지만 보이게
# #평균 90.00


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return (self.width + self.height) * 2

# s = Rectangle(4, 3)
# print(s.area())
# print(s.perimeter())


# def diagonal_sum(grid):
#     total = 0
#     for i in range(len(grid)):
#         total += grid[i][i]
#     return total

# print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


# def even_squares_reversed(nums):
#     x = [i*i for i in nums if i % 2 == 0]
#     return x[::-1] #역순 정렬

# print(even_squares_reversed([1, 2, 3, 4, 5]))


# #스택
# #가장 나중에 넣은 것을 가장 먼저 꺼낸다(후입선출)

# #스택 ADT연산
# #push(x) : 데이터 x를 스택의 top에 넣는다
# #pop() : top의 데이터를 꺼내 제거하고 그 값을 반환한다. 빈 스택이면 오류로 처리
# #peek() : top의 데이터를 제거하지 않고 확인만 한다
# #is_empty() : 스택이 비어 있으면 참, 아니면 거짓을 반환함
# #size() : 스택에 저장된 데이터의 개수를 반환
# #빈 스택에 pop이나 peek을 호출하면 꺼낼 데이터가 없어 오류가 됨, 이를 언더플로라고 함
# #데이터를 꺼내기 전에 is_empty()로 스택이 비었는지 확인하는 습관이 필요

# #가장 최근의 것을 먼저 처리해야 하는 곳에서 두루 쓰임
# #편집기의 되돌리기, 프로그램이 함수를 호출하고 되돌아오는 과정


# #리스트를 스택으로 쓰는 아이디어
# #파이썬 리스트의 맨 끝을 스택의 top으로 삼기
# #push(x) == append(x)
# #pop() == pop()
# #peek() == [-1]
# #is_empty() == 길이가 0인지 확인
# #size() == 리스트의 길이

# #Stack 클래스 구현
# x = int(input(""))
# x = [input() for i in range(x)]

# class Stack:
#     def __init__(self):
#         self.item = []

#     def push(self, item):
#         self.item.append(item)

#     def pop(self):
#         if len(self.item) == 0:
#             return -1
#         return self.item.pop()

#     def top(self):
#         if len(self.item) == 0:
#             return -1  
#         return self.item[-1]

#     def empty(self):
#         if len(self.item) == 0:
#             return 1
#         return 0

#     def size(self):
#         return len(self.item)

# s = Stack()

# for i in x:
#     pre = i.split()
    
#     if pre[0] == "push":
#         push = int(pre[1])
#         s.push(push)
#     elif pre[0] == "pop":
#         print(s.pop())
#     elif pre[0] == "size":
#         print(s.size())
#     elif pre[0] == "top":
#         print(s.top())
#     elif pre[0] == "empty":
#         print(s.empty())


# class Stack:
#     def __init__(self):
#         self._items = []

#     def push(self, item):
#         self._items.append(item)

#     def pop(self):
#         if self.is_empty():
#             raise IndexError("빈 스택에서 pop을 호출했다")
#         return self._items.pop()

#     def peek(self):
#         if self.is_empty():
#             raise IndexError("빈 스택에서 peek을 호출했다")
#         return self._items[-1]

#     def is_empty(self):
#         return len(self._items) == 0

#     def size(self):
#         return len(self._items)

#_items이라고 쓰는 이유
#클래스 내부에서만 쓰는 값이라는 뜻을 약속처럼 나타냄
#문법으로 강제되지는 않지만 스택을 쓰는 쪽은 _items를 직접 건드리지 말고 push와 pop같은 메서드만 사용하라는 신호


# def divide(a, b):
#     if b == 0:
#         raise ValueError("0으로 나눌 수 없습니다")
#     return a / b

# divide(10, 0)

#파이썬은 내장된 리스트로 스택을 구현할 수 있지만
#리스트를 그대로 쓰는 방식은 짧은 코드나 간단한 문제에 편리하고
#클래스로 감싸는 방식은 스택이라는 의도를 분명히 하고 잘못된 사용을 막고 싶을 때 좋음


#괄호 검사


#큐 ADT
#먼저 들어온 것이 먼저 나오는 자료구조(선입선출), FIFO
#한쪽 끝에서 데이터를 넣고 반대쪽 끝에서 빼는 자료구조

#enqueue : 큐에 데이터를 넣는 동작
#dequeue : front에서 데이터를 꺼내며 제거하는 동작, 그 값을 반환함, 빈 큐면 오류로 처리
#peek() : front의 데이터를 제거하지 않고 확인만 함
#is_empty() : 큐가 비어 있으면 참, 아니면 거짓 반환
#size() : 큐에 저장된 데이터의 개수를 반환

#먼저 들어온 것을 먼저 처리해야하는 곳에서 쓰임
#서버가 들어온 요청을 순서대로 처리하는 작업
#그래프나 트리를 가까운 곳부터 차례로 살피는 너비우선탐색(BFS)가 큐로 구현됨

#리스트로 단순하게 큐를 만들 수 있지만 느림

#원형 큐
#고정 크기의 배열을 쓰되 끝에 도달하면 다시 처음으로 돌아가 빈 자리를 재사용하는 방식
#다음에 넣을 위치는 (front+size)%배열크기

class CircularQueue:
    def __init__(self, capacity):
        self._data = [None] * capacity
        self._capacity = capacity
        self._front = 0      # 맨 앞 원소의 위치
        self._size = 0       # 현재 원소 개수

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._capacity

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("큐가 가득 찼다")
        rear = (self._front + self._size) % self._capacity
        self._data[rear] = item
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("빈 큐에서 dequeue를 호출했다")
        item = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("빈 큐에서 peek을 호출했다")
        return self._data[self._front]

    def size(self):
        return self._size




class CircularQueue:
    def __init__(self, que):
        self.data = [None] * que
        self.front = 0
        self.size = 0

    def push():

    def is_full():
        return self.size == self.front

    def size():
        return self.size