# #함수의 매개변수(parameter)
# #함수에 전달(입력)되는 값(함수 정의할 때)
#
# #인수(argument) : 함수에 실제로 전달되는 값
#
# def showInfo(name,age):
#     print("이름은 %s이고 나이는 %d에요." %(name,age))
#
# showInfo('홍길동',18)  #<이름은 홍길동이고 나이는 18에요.>
#
#
# def getArea(width,height):
#     return width*height*0.5
#
# w = int(input('밑변 : '))
# h = int(input('높이 : '))
# print(getArea(w,h))


#사칙연산을 수행하는 함수들을 정의하여 호출
#add(x,y)
#sub(x,y)
#mul(x,y)
#div(x,y)

#2개의 숫자를 기보드로 입력받고, 각 함수에 전달하여 계산결과 출력 코드 완성
# 10 + 5 = 15
# 10 - 5 = 5
# 10 * = 50
# 10 / 5 = 2.0

def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    return x / y
x = int(input("숫자1 입력 : "))
y = int(input("숫자2 입력 : "))
#x, y = map(int, input('숫자 두 개를 입력하세요. : ').split(' '))
print('{} + {} = {}' .format(x,y,add(x,y)))
print('{} - {} = {}' .format(x,y,sub(x,y)))
print('{} * {} = {}' .format(x,y,mul(x,y)))
print('{} / {} = {}' .format(x,y,div(x,y)))
