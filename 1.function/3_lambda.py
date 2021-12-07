# lambda 간단한 정의할 때 사용

def mul5(x):
    return 5*x
# mul5라는 함수는 함수 객체를 바인딩

a = lambda x: 5*x
# 함수 객체가 생성되고 a가 바인딩
# a가 함수 객체를 바인딩 함으로 a()로 함수 호출 가능 / 함수 호출시 인자가 하나 필요함으로 인자값 넘긴다
print(a(2))