class Car:
    number = 1
    def __init__(self, color='white', speed=0):  #기본값 지정
        self.color = color  #클래스 내에서만 사용하는 비공개 필드
        self.speed = speed

    def __str__(self):
        return ('이 자동차의 색상은 %s이고,\n속도는 %d입니다.' %(self.color,self.speed))

    #color필드 값을 반환
    def getColor(self):
        return self.color

    #color 필드값을 변경메소드
    def setColor(self,color):
        self.color=color #매개변수와 필드값이 동일

    def showInfo(self):
        self.showColor()
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

# car1 = Car()
# print(car1.getColor())
# car1.setColor('red')
# print(car1.getColor())
# # car1.setColor('blue')  #필드를 외부에서 직접 입력
# # car1.__showColor()  #AttributeError: 'Car' object has no attribute '__showColor'
# car1.showInfo()
# car1.upSpeed(20)
# car1.drive()
# car1.upSpeed(20)
# car1.drive()
# car1.downSpeed(20)
# car1.drive()
# car1.downSpeed(20)
# car1.drive()

car1=Car()
#인스턴스 변수(필드)
print(car1.speed)
print(car1.color)

#클래스 변수
print(car1.number)

car2=Car('Blue',10)
print(Car.number)


