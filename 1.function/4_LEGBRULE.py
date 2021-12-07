#LEGB RULES
'''
파이썬에서 변수에 값을 바인딩하거나 값을 참조하는 경우 legb규칙을 따른다.

L : local : 함수 안 
E : Enclosed function locals : 내부함수에서 자신의 외부 함수의 범위
G : global : 함수 바깥, 모듈 범위 
B : Built-in : open, range와 같은 파이썬 내장 함수
'''

a = 10 
def test():
    a = 20
    print(a)

test()
# test 함수가 호출되면 a변수가 바인딩되는 값을 출력
# a라는 변수가 reference 되었음으로 L, E, G, B 순으로 변수를 탐색
# 1. test 함수 안 local 영역
# 2. local 영역 안에 존재 함으로 local 영역의 a 변수가 바인딩하는 값인 20이 화면에 출력

a = 10

def test():
    print(a)
test()
# local 영역에 변수가 없고 
# Enclosed function 안에도 존재 하지 않는다
# global 영역의 변수 참조

# 변수 바인딩

a = 10 
def test():
    a = 20
    print(a)

test()
print(a)
# 함수 내에서 생성되는 a는 global영역에 있는 a와 전혀 다른 변수 
# local 영역에서 global 영역에 변수 값 수정 불가능

a = 10
def test():
    global a 
    a = 20
test()
print(a)
# 함수 내에서 global 영역의 변수 값을 수정할려면 global
# local 영역에 사용되는 변수가 global 영역의 변수임을 선언 
