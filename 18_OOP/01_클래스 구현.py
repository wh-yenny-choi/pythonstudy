# 클래스 선언
# class 클래스 이름[(슈퍼클래스명)] :
#     필드(속성1)
#     필드(속성2)
#     def method(self):
#         ...
#     def method(self):
#         ...


# 빈 클래스 정의
class Car:
    pass

car1=Car()
print(car1)
#<__main__.Car object at 0x000000801F6FF280>


class Car:  #메소드 정의
    def show(self):
        print('시험중입니다.')
#인스턴스 생성
car1=Car()
car2=Car()
car3=Car()
print('-------')
car1.show()   #메소드 호출
car2.show()
car3.show()

# 특정 클래스의 인스턴스인지 확인 : isinstance(인스턴스명, 클래스명)
print(isinstance(car1,Car))
print(isinstance(car1,int))

# 파이썬에서 기본 제공하고 있는 int,float,bool,str,list,dict,set,tuple
# ==> 클래스
x=3
print(isinstance(x,int))
print(type(x))  #<class 'int'>

y=list([1,2,3,4])
print(isinstance(y,list))

z='Hi, 반가워요'
print(type(z))  #<class 'str'>

a = True
print(type(a))  #<class 'bool'>

print(isinstance(a,int))  #True

b=(1,2,3)
print(type(b))  #<class 'tuple'>
print(isinstance(b,list))  #False

# instance & object
# 같은 것 가리키고 있음
# instance : 클래스와 연관지어 말할때
# 예 ) car1은 Car 클래스의 인스턴스이다
# object : 단독으로 부를 때
# 예 ) car1 객체


#####################################
#필드 추가

#클래스 정의 부분
class Car:
    def show(self):
        print('시험중입니다')
    # def drive(self):
    #     self.speed=60 #speed필드
    #     print('%d 로 주행중입니다.' %self.speed)
    def drive(self,speed):
        self.speed=speed #speed필드
        print('%d 로 주행중입니다.' %self.speed)

#메인 : 인스턴스를 생성하고 이용하는 부분
car1=Car()
car1.drive(70)  #60 로 주행중입니다.
print(car1.speed)  #60
car1.speed=100
car1.drive(50)


# 인스턴스.필드
car1.color = 'red'
print(car1.color)

#클래스에서 필드 선언
class Car:
    speed = 0
    color=''
    def show(self):
        print('시험중입니다.')
    def drive(self):
        print('%d 로 주행중입니다.' %self.speed)

mycar = Car()
print(mycar.speed)
mycar.drive()
mycar.speed=60
mycar.drive()

#생성자(construct) : 인스턴스를 생성해주는 함수
class Car:
    def __init__(self):
        self.color = 'white'
        self.speed = 0

    def showInfo(self):
        print('이 자동차의 색상은 %s입니다.'%self.color)

    def drive(self):
        if self.speed != 0:
            print('%d 로 주행중입니다.' %self.speed)
        else:
            print('정차중입니다.')

mycar=Car()
print(mycar.color)
print(mycar.speed)
mycar.showInfo()
mycar.drive()
mycar.speed = 50
mycar.drive()

#매개변수가 있는 생성자 __init__(self, 매개변수1, 매개변수2)

class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def showInfo(self):
        print('이 자동차의 색상은 %s입니다.' % self.color)

    def drive(self):
        if self.speed != 0:
            print('%d 로 주행중입니다.' % self.speed)
        else:
            print('정차중입니다.')


mycar = Car('red',10)
print(mycar.color)
print(mycar.speed)
mycar.showInfo()
mycar.drive()
mycar.speed = 50
mycar.drive()

yourcar = Car('blue',0)
yourcar.showInfo()

class Car:
    def __init__(self, color='white', speed=0):  #기본값 지정
        self.color = color
        self.speed = speed

    def showInfo(self):
        print('이 자동차의 색상은 %s입니다.' % self.color)

    def drive(self):
        if self.speed != 0:
            print('%d 로 주행중입니다.' % self.speed)
        else:
            print('정차중입니다.')

car1 = Car()
car2 = Car('Yellow')
car3 = Car('blue')  #출력에 한개쓰면 기본값은 매개변수1
car4 = Car(speed = 20)  #출력에 한개쓰면 기본값은 매개변수1 >> 매개변수2 출력위해서는 'speed=' 적어줘야 함
car5 = Car('black',speed=50)
car1.showInfo()
car2.showInfo()
car3.showInfo()
car4.drive()
print(car5.speed)
print(car5.color)


class Car:
    def __init__(self, color='white', speed=0):  #기본값 지정
        self.color = color
        self.speed = speed

    # def __str__(self):

    #color필드 값을 반환
    def getColor(self):
        return self.color

    #color 필드값을 변경메소드
    def setColor(self,color):
        self.color=color #매개변수와 필드값이 동일

    def showInfo(self):
        print('이 자동차의 색상은 %s입니다.' % self.color)

    def drive(self):
        if self.speed != 0:
            print('%d 로 주행중입니다.' % self.speed)
        else:
            print('정차중입니다.')

car1 = Car()
print(car1.getColor())
car1.setColor('red')
print(car1.getColor())
car1.setColor('blue')  #필드를 외부에서 직접 입력
car1.showInfo()

# 비공개 필드 정의 : __필드명
# 클래스 내부의 메소드를 통해서 사용
class Car:
    def __init__(self, color='white', speed=0):  #기본값 지정
        self.__color = color  #클래스 내에서만 사용하는 비공개 필드
        self.speed = speed

    # def __str__(self):

    #color필드 값을 반환
    def getColor(self):
        return self.__color

    #color 필드값을 변경메소드
    def setColor(self,color):
        self.__color=color #매개변수와 필드값이 동일

    def __showColor(self):
        print('이 자동차의 색상은 %s입니다.' % self.__color)

    def showInfo(self):
        self.__showColor()
        print('속도는 %d입니다.' %self.speed)

    def drive(self):
        if self.speed != 0:
            print('%d 로 주행중입니다.' % self.speed)
        else:
            print('정차중입니다.')

    def upSpeed(self,up):
        self.speed += up

    def downSpeed(self,down):
        self.speed -= down
        if self.speed < 0:
            self.speed = 0

car1 = Car()
print(car1.getColor())
car1.setColor('red')
print(car1.getColor())
# car1.setColor('blue')  #필드를 외부에서 직접 입력
# car1.__showColor()  #AttributeError: 'Car' object has no attribute '__showColor'
car1.showInfo()
car1.upSpeed(20)
car1.drive()
car1.upSpeed(20)
car1.drive()
car1.downSpeed(20)
car1.drive()
car1.downSpeed(20)
car1.drive()