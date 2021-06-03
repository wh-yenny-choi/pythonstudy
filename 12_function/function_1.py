#함수의 개요
#함수 정의

def printHello():
    print('Hello')

def printName(name):
    print(name)

def area_square(width,height):
    area = width * height
    return area
w=10
h=20

#함수 호출
area = area_square(w,h)
print(area)
printHello()
printName('Lee')

#연습문제
# 함수이름 : show_info()
# 최원희
# 27
# 010-9953-9523

def show_info():
    print('최원희\n27\n010-9953-9523')

#함수 이름 sum()
#숫자 2개를 키보드로 입력받아서 두 수의 합을 출력
#숫자1 입력 : 10
#숫자2 입력 : 20
#합 : 7

def sum():
    a=int(input('숫자1 입력 : '))
    b=int(input('숫자2 입력 :'))
    print('합 : {}'.format(a+b))