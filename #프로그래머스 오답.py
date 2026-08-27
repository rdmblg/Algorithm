#프로그래머스 오답
#1
#꼬리문자열 문제

#내 코드 :
def solution(str_list, ex):
    x = []
    for i in range(len(str_list)):
        if int(ex in str_list[i]) == 1:
            x += str(str_list)
    return "".join(x)

#문제점
#1. 조건이 반대임
#ex가 str_list에 포함되어 있지 않은 것만 추가하려면 not in이 True여야함
#2. str(str_list)로 리스트 전체를 넣는게 아닌 str_list[i] 해서 특정 요소만 넣어야함

#바꾼 코드
def solution(str_list, ex):
    x = []
    for i in range(len(str_list)):
        if int(ex not in str_list[i]) == 1:
            x += str_list[i]
    return "".join(x)

#다른 사람의 코드
def solution(str_list, ex):
    return ''.join([i for i in str_list if ex not in i])
#리스트 컴프리헨션은 항상 새로운 리스트를 반환한다는 것을 잊지 말기


#tlqkf
#문자열 바꿔서 찾기
#내 풀이
def solution(a, pat):
    x = ''
    for i in range(len(a)):
        if a[i] == "A":
            x += "B" 
        else : 
            x += "A"
            
    ret = 0
    for i in range(len(pat)):
        
        if pat in x[i:len(pat)+i]:
            return 1
        else : 
            ret = 0
    return ret
#아니나도 리플레이스쓸생각했는데시바시바시밧비

#고수 풀이
def solution(myString, pat):
    return int(pat in myString.replace('A', 'C').replace('B', 'A').replace('C', 'B'))
#씨를 사용해도 된다는건 상상도못햇다 씨앙~~~
#그리고 int 하...아니 난왜 int생각이 안나지..
#pat in myString한다음에 true면 1나오고 아니면 0나오는거..
#뭔가 결과가 1, 0 이렇게 나오면 int도 생각해봐야겟다..이제부터,,,,


#tlqkf
#내코드
def solution(binomial):
    return eval(binomial)

#고수코드
solution=eval
#아니시발


#5명씩
#내코드
def solution(names):
    x = []
    x.append(names[::5])
    return [y for a in x for y in a]

#고수코드
def solution(names):
    return names[::5]
#아니 이게 왜 되는거지


#1로 변환하기
#내코드
def solution(num_list):
    x = 0
    for i in num_list:
        while i != 1:
            if i % 2 == 0:
                i = i / 2
                x += 1
            else :
                i = (i-1) / 2
                x += 1
    return x

#고수코드
def solution(num_list):
    return sum(len(bin(i)) - 3 for i in num_list)
#bin(i)는 정수 i를 이진수 문자열로 바꿔주는데 앞에 0b라는 접두사가 항상 붙음
#len(bin(i))는 이진수 자릿수 +2임 (ob)때문
#-3은 먼저 2를 빼서 0b를 제거, 추가로 1을 더 빼서 자릿수 -1함..?왜?
#이해가안된다


#배열만들기3
