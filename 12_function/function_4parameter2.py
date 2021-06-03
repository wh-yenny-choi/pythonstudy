#함수의 매개변수 형식
#매개변수에 기본값 지정 : default parameter

def showMessage(message='Hi!'):
    print(message)

def showMessage2(name,message='Hello!'):
    print(name+message)

#defalut argument는 맨 뒤에
# def showMessage2(message='Hello!',name):
#     print(name,message)

showMessage('Hello')
showMessage('Hi')
showMessage('We are happy!')
showMessage2('Kim','Hi')
showMessage2('Kim')
showMessage()

def showInfo(name,age=10,sex='F'):
    print(name,age,sex)

showInfo('') #< 10 F>
showInfo('홍길동')  #<홍길동 10 F>
showInfo('강감찬',40)  #<강감찬 40 F>
showInfo('변학도',40,'M')  #<변학도 40 M>

#함수의 실인수로 리스트가 전달
def showNames(names):
    for name in names:
        print(name,end=' ') #end = > 한줄로 결과 출력
                            #<Hong Park Choi Lee>
showNames(['Hong','Park','Choi','Lee'])
#or
#names = ['Hong','Park','Choi','Lee']
#showNames(names)

#함수의 실연수로 딕셔너리가 전달
def showInfostu(student):
    print(student)
    print('이름 : ', student['name'])
    print('나이 : ', student['age'])
    print('연락처 : ', student['phone'])

info_std = {'name':'Kim','age':19,'phone':'010-1111-1023'}
showInfostu(info_std)

# *args : arguments 1개 이상 지정(가변길이 형식)
# kwargs : keyword argument사용, key=value

def mySum(*args):
    total = 0
    for x in args:
        total += x
    return total

print(mySum(1,3,5))   #<9>
print(mySum(3,4))     #<7>
print(mySum(1,2,4,5,6))  #<18>
#print(mySum([1,2,4,5,6]))

def myShowInfo(**kwargs):
    for key in kwargs.keys():     #id name add
        print(key,end=' ')        #id name
    print()                       #id name add phone
    for value in kwargs.values(): #123 Kim Seoul
        print(value,end=' ')      #333 Lee
    print()                       #121 Choi Incheon 1111-1111
    for item in kwargs.items():
        print(item)

myShowInfo(id=123, name='Kim', add='Seoul')
myShowInfo(id=333, name='Lee')
myShowInfo(id=121, name='Choi', add='Incheon', phone='1111-1111')

def calculator(operator,*args):
    pass

def studentInfo(name,age,sex):
    student={'name':name,'age':age,'sex':sex}
    return student

print(studentInfo('Lee',30,'F'))  #<{'name': 'Lee', 'age': 30, 'sex': 'F'}>
print(studentInfo(name='Kim',age=40,sex='F'))  #<{'name': 'Kim', 'age': 40, 'sex': 'F'}>
print(studentInfo(name='Kim',sex='F',age=40))  #<{'name': 'Kim', 'age': 40, 'sex': 'F'}>
#위치 기반 인수
#키워드 기반 인수
#키워드 순서 바뀌어도 매개변수 지정된 그대로 출력
print(studentInfo('Kim',sex='M',age=15))  #<{'name': 'Kim', 'age': 15, 'sex': 'M'}>
#print(studentInfo(name='Kim','M',15))
#오류 : 위치 인수와 키워드 인수를 같이 쓸때는 키워드인수는 위치 인수 뒤로 와야함

