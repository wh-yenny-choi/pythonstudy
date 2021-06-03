#함수내에 사용되는 변수 : Local variable(지역변수)

def show():
    a = 'Hello'  #지역변수
    print(a)

def show1(a):
    a = a + 'Hello'
    print(a)

#전역 변수를 함수 내부에서 사용
def show2():
    #a=10
    print(a)

#전역 변수를 함수 내부에서 수정(변경)
def show3():  #전역변수 a를 변경하고 싶다
    global a
    a = a + 'H'
    print(a)

a='Hi' #전역변수 : 코드 전체 내에서 영향 주는 변수
#show1('haha')
#show()
#print(a)
#show2()
show3()


#실습문제
def sub(x,y):
    global a
    a=7
    x,y=y,x  #swap
    b=3
    print(a,b,x,y)
    print(id(a))
    print(id(x))

# a,b,x,y=1,2,3,4
# print('전역변수')
# print(id(a))
# print(id(x))
# sub(x,y)
# print(a,b,x,y)

def showList(mylist):
    #New_mylist = []
    mylist[0]=100  #전역변수처럼 전체 값수정 ,전달만 하고 싶을때는 list 새로 만들기 > #New_mylist = []
    print(mylist)
    print('in function ID : ',id(mylist))

mylist=[1,2,3,4]
showList(mylist)
print(mylist)
print('in function ID : ',id(mylist))

#딕셔너리 list를 dictionary로 변환
def getProduct(prdList):
    name=prdList['name']
    price=prdList['price']
    return {'name':name,'price':price}

productL=[{'name':'notebook','price':1200000,'Maker':'삼성'},
          {'name':'smartphone','price':1200000,'Maker':'삼성'},
          {'name':'냉장고','price':5100000,'Maker':'LG'},
          {'name':'에어콘','price':3500000,'Maker':'삼성'},]

for product in productL:
    prdInfo=getProduct(product)
    print(prdInfo)
