#함수의 반환값(return)

def sum():
    a = int(input("숫자1 입력 : "))
    b = int(input("숫자2 입력 : "))
    # sum(a+b)#print(a+b)
    # return sum
    return a+b

# print(sum())
#res = sum()
#print("합은 %d" %res)
print("합은 %d" %sum())


#삼각형의 넓이 계산 함수 get_triangle_area()
#높이와 밑변을 키보드로 입력 받아 계산, 결과값 반환
def square():
    height=int(input("높이 : "))
    width=int(input("밑변 : "))
    print("삼각형의 면적 : %.1f"%(height*width/2))
    return height*width/2
square()

def square():
    height=int(input("높이 : "))
    width=int(input("밑변 : "))
    area = height * width / 2
    return area
area = square()
print("삼각형의 면적 : %.1f"%area)


#반환값이 여러개인 경우 컴마(,)구분
#반환값의 형식은 튜플

def square():
    height=int(input("높이 : "))
    width=int(input("밑변 : "))
    area = height * width / 2
    return height, width, area

area = square()
print('높이%d, 밑변 %d, 삼각형의 넓이 %.2f' %(area[0],area[1],area[2]))  #<(10, 5, 25.0)> 튜플형태로 값 변환

def multiRetrun() :
    return 1
    return 2
    return 3

print(multiRetrun())  #<1>


#리스트 반환값

def getNames():
    names=[]
    for i in range(3):
        name=input("이름 입력 : ")
        names.append(name)
    return names
nameL = getNames()
print(type(nameL))  #<<class 'list'>>
print(nameL)  #<['최원희', '최원희', '최원희']>


#이름과 나이를 입력받아 딕셔너리 형식 변환
#{'name':'홍길동','age':'20'}
def get():
    d = {}
    a = input("이름 입력 : ")
    b = int(input("나이 입력 : "))
    # d["name"] = a
    # d["age"] = b
    d={'name': a, 'age': b}
    return d
d=get()
#print(type(d))
print(d)   #{'name': '홍길동', 'age': 20}
print(d[list(d.keys())[0]])  #<홍길동>

for key, value in d.items():
    print(key,':',value)

for key in d.keys():
    print(key,":",d[key])

def myInfo():
    info=dict()
    name, age = input('이름, 나이 입력(","로 구분) : ').split(',')
    info['name'] = name
    info['age'] = int(age)
    return info
infoD = myInfo()
print(infoD)

'''

#반환값이 없는 경우 None 출력

def showHello():
    print('Hello')

result=showHello()
print(result)