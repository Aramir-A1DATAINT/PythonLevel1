#nested function(중첩 함수)
'''
함수 암에 함수를 정의한거
중첩함수를 통해 defualt로 enclosing function local scope 변수를 참조할 수 있습니다
'''

def outer_func(msg):

    def inner_func():
        print(msg)
    return inner_func
# inner func : 내부함수
# outer func : 외부함수
# inner func 입장에서 outer_func 함수의 지역변수 영역을 enclosing function local scope


myfunc = outer_func('hello there python is easy')
myfunc()
# closure
# 내부함수가 회부함수의 맥락에 접근할 수 있는 것을 가리킴
# 함수를 변수에 저장할수 있는 이유는 파이썬에서 함수가 first class object 이기 때문에


first_func = outer_func("python is very cute!!")
second_func = outer_func("It's true") 

print('outer_func:', id(outer_func))
del outer_func
first_func() 
second_func() 
print('first_func:', id(first_func))
print('second_func:', id(second_func))
#outer func 을 삭제해도 first func가 정상적으로 호출됨
# 함수를 변수에 저장할 떄 마다 객체를 새롭게 생성하기 때문 (id 값을 새로 생성함)
# first_func, second_func가 서로 완전히 독립적 객체

# 클로저 내에서 enclosing function local scope 변수 Read/Write

def outer_func(msg):

    def inner_func():
        print(msg)
        msg = 'no it is not fun at all '
        print(msg)
    return inner_func
first_func = outer_func("python is very cute!!")
first_func() # 작동하지 않음, local variable 'msg' referenced before assignment
# print문에서 inner_func 함수 내에서 msg라는 변수가 선언된적이 없기에 enclosing functino local scope에서 찾는다
# BUT 전역변수와 같이 함수 내에서 수정할수 없음

def outer_func(msg):

    def inner_func():
        inner_func.msg = msg
        print(inner_func.msg)
        inner_func.msg = 'no it is not fun at all '
        print(inner_func.msg)
    return inner_func
first_func = outer_func("python is very cute!!")
first_func()