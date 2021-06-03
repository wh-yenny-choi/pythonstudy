class Dog:
    def __init__(self,Breed,Size,Age,Color):
        self.Breed = Breed
        self.Size = Size
        self.Age = Age
        self.Color = Color
    def Eat(self):
        print('음식을 먹는다.')

    def Sleep(self):
        print('%s가 잠들었다.'%self.Breed)

    def Run(self):
        print('%s가 놀고있다.'%self.Breed)

    def __str__(self):
        return (self.Breed,self.Size,self.Age)
#객체가 가지고 있는 이름,나이 종류 정보를 출력
    def __lt__(self, other):
        return self.Age < other.Age
#자신의 객체나이와 other 객체 나이보다 작은지 비교한 결과값 출력

    def __eq__(self, other):
        return self.Age == other.Age
#자신의 객체나이와 other 객체 나이가 같은지 비교한 결과값 출력

dog1 = Dog('Neapolitan Mastiff','Large','5 years','Black')
dog2 = Dog('Maltese','Small','2 years','White')
dog3 = Dog('Chow Chow','Midium','3 years','Brown')
dog1.Eat()
dog1.Sleep()
dog1.Run()
dog2.Eat()
dog2.Sleep()
dog2.Run()
dog3.Eat()
dog3.Sleep()
dog3.Run()

if dog1.Age < dog2.Age:
    print('{}보다 {}가 더 나이가 많네요.'.format(dog1.Breed,dog2.Breed))
elif dog1.Age > dog2.Age:
    print('{}보다 {}가 더 나이가 많네요.'.format(dog2.Breed, dog1.Breed))
else:
    print('나이가 같네요.')



class Dog :
    def __init__(self, name, breed, size, age, color):
        self.name = name
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color

    def __str__(self):
       return "이름 : %s, 나이 : %d, 종류 : %s" % (self.name, self.age, self.breed)

    def eat(self):
        print("음식을 먹는다")

    def sleep(self):
        print("%s가 잠들었다" % self.breed)

    def sit(self):
        print("%s가 앉아있다" % self.breed)

    def run(self):
        print("%s가 놀고 있다" % self.breed)

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age

dog1 = Dog('aaa', 'Neapolitan Mastiff', 'Large', 5, 'Black')
dog2 = Dog('bbb', 'Maltese', 'Small', 3, 'White')
dog3 = Dog('ccc', 'Chow Chow', 'Midium', 3, 'Brown')

print(dog1)
print(dog2)
print(dog3)

if dog1 > dog2 :
    print("%s가 %s보다 나이가 적습니다" % (dog2.name, dog1.name))
else:
    print("%s가 %s보다 같거나 많습니다" % (dog2.name, dog1.name))

if dog2 == dog3 :
    print("나이가 같습니다")