# positional variable argument (*args)
# 함수 정의시 인자값의 개수를 가변적으로 정의 해야 하는경우
# *args 같이 파리미터 앞에 * 붙여 준다
def foo(*args):
    print(args)

foo(1, 2, 3) # 서로 다른 개수의 인자를 전달하고자 할때 Variable argument(가변인자)를 사용   
             # 함수 호출시 args라는 변수는 여러개의 입력에 대해 튜플로 저장하고 튜플 객체를 바인딩 한다

# Keyword variable arguments(**kwargs)
# 파이썬 가변인자 : 위치 가변 인자, 키워드 가변인자 
# *args: 위치 가변 인자, **kwargs : 키워드 가변인자

def foo(**kwargs):
    print(kwargs)

foo(a=1, b=2, c=3) # a=1, b=2, c=3과 같이 키워드와 해당 키워드 값을 전달 / kwargs라는 변수가 딕셔너리 객체를 바인딩


# mixup
def foo(*args, **kwargs):
    print(args)
    print(kwargs)


foo(1, 2, 3, a=1, b=1, c=2)
 
 # onemore!
def foo(a, b, c):
    print(a, b, c)

data = [1, 2, 3]
foo(*data) # foo(data[0], data[1], data[2]) it can be 인덱싱 귀찮고 list/tuple * 붙여주면 풀어서 나감

# twomore!s
def foo(**kwargs):
    print(kwargs)

foo(a=1, b=2) # kwargs 딕셔너리 바인딩 

params = {'a': 1, 'b': 2} # if 데이터 already dictionary **
foo(**params)
