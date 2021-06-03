#재귀함수

def selfCall():
    print('ha',end='')
    selfCall()

selfCall()
#오류수정 코드
def selfCall(num):
    if num == 0:
        return
    else:
        print('ha',end='')
        selfCall(num-1)

selfCall(5)


#팩토리얼 계산
def fact(num):
    if num ==1 :
        return 1
    else:
        return num*fact(num-1)
print(fact(5))

#자연수를 입력받으면 해당하는 자연수까지 출력
#49 입력하면, 49~1 출력
def count(num):
    if num:
        print(num)
        count(num-1)
count(49)

aa = int(input('숫자입력 : '))
def sun(aa):
    if aa==1:
        return print(aa)
    else:
        return print(aa,end=" "),sun(aa-1)
sun(aa)

def count(num):
    if num:
        print(num,end='')
        return count(num-1)
count(49)

def count(num):
    if num==0:
        return
    else:
        print(num)
        count(num-1)
count(49)

#내부함수 : 함수 내에서 정의된 함수
def outFunc(x,y):
    def inFun(a,b):
        return a+b
    return inFun(x,y)

print(outFunc(10,20))  #30
#print(inFun(10,20))  #내부함수이기 때문에 오류

# 람다 식 : lambda 함수(표현식)
#방법 1.
#(lambda 매개변수들 : 식)(인수들)

#방법 2.
# 객체명 = lambda 매개변수들 : 식
# 객체명 (인수들)

# lambda 함수1정의,함수2정의 : 함수 식

def hap(x,y):
    return x+y

print(hap(10,50))  #60

print((lambda x,y:x+y)(10,50))  #60
hap2=lambda x,y:x+y
print(hap2(5,10))  #<15>

def hap(x=10,y=20):
    return x+y

print(hap()) #30
print(hap(30,100)) #130

hap3=lambda x=10,y=20 : x+y
print(hap3()) #30
print(hap3(9,10)) #19

#print((lambda x: y=10, x+y)(10)) 오류
#람다함수 안에서 변수 생성할 수 없다.

y=10
print((lambda x : x+y)(1)) #<11>

#람다 list 사용
#리스트의 값에 각각 10을 더하는 람다 함수

# 주어진 값에 10을 더하는 함수
def addTen(x):
    return x + 10

#myL=[1,3,4]
print(list(map(addTen,[1,3,4])))
print(list(map(lambda x:x+10, [1,3,4])))

#실습문제. 두개의 리스트의 같은 요소의 값들을 더해서 하나의 리스트로 반환
# 1) def함수 정의
# 2) lambda 표현식 정의
list1=[1,2,3,4]
list2=[10,20,30,40]
def addList(list1,list2):
    list3 = []
    for i in range(len(list1)):
        a = list1[i]+list2[i]
        list3.append(a)
    return list3

print(addList(list1,list2))
Hap = (lambda list1, list2 : list1 + list2)
print(Hap)


def hap(a, b):
    return [x + y for x, y in zip(a, b)]

print(hap(list1, list2))
