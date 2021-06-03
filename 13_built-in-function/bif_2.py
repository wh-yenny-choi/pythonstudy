# 계산과 관련된 내장 함수

# abs() : 절대값 계산
print(abs(-10))   #10
print(abs(100))    #100

#min() : 최소값 계산
print(min(1,-10,3))  #-10
print(min([-9,-10,-30,3]))    #-30

#max() : 최대값 계산
print(max(1,-10,3))  #3
print(max([-9,-10,-30,3]))  #3

#pow(base,exp) : x^y
print(pow(2,10))   #1024

#divmod(a,b) : 나머지와 몫 => 결과 (\\,&)
print(divmod(9,2))  #(4,1)

#sum(iterable) : 합계
print(sum([1,-10,3]))  #-6

#round(숫자, 소수자리) : 반올림
print(round(9.87))  #10
print(round(9.87,1)) #9.9
print(round(-9.87,1))  #-9.9
print(round(9.87433,3))  #<9.874>

#enumerate(iterable,start=0)
#시퀀스(리스트,튜플,문자열,range)를 인덱스값을 포함하는 enumerate 객체로 변환
enum = enumerate(['apple','banana','melon','strawbeery','kiwi','watermelon'])
print(enum)
for i,item in enum:
    print(i,item)
# 0 apple
# 1 banana
# 2 melon
# 3 strawbeery
# 4 kiwi
# 5 watermelon

seasons=['spring','summer','fall','winter']
enumseason = list(enumerate(seasons))
print(enumseason)  #[(0, 'spring'), (1, 'summer'), (2, 'fall'), (3, 'winter')]
#요소들이 튜플형태이므로 for문 or list로 변환하여 사용
enumseason = list(enumerate(seasons,start=1))
print(enumseason)  #[(1, 'spring'), (2, 'summer'), (3, 'fall'), (4, 'winter')]

#eval()
print(eval('3.1'))  #3.1
print(eval('10+100'))  #110

#filter(funcion,iteralbe) : 반복가능한 자료형 요소에 함수를 적용하여
# 반환값이 참(True)인 결과만 걸러내어 반환

def positive(x):
    return x>0

print(positive(9))  #True
print(positive(-9))  #False

result = filter(positive,[-10,0,3,-8,7])
print(type(result))  #<class 'filter'>
print(list(result))  #[3, 7]  필터형은 리스트 상태로 반환하여 출력

#실습문제 : 짝수인지를 판별하는 함수even(x)를 정의하고,
# 이 함수를 filter이용하여 주어진 리스트의 짝수만 걸러내는 코드를 작성

def even(x):
    return x%2==0
even_list=[1,2,3,4,5,6,7,8,9,10]
even_result = filter(even,even_list)  #filter이용하여 True만 걸러냄
print(list(even_result))

print('----------')

enum = enumerate(['apple','banana','melon'])
#enum = list(enum)
#next()
for e in enumerate(['apple','banana','melon']):
    print(e)

print(enum)
print(list(enum))   #[(0, 'apple'), (1, 'banana'), (2, 'melon')]

print('----------')

fruits = iter(['apple','banana','melon'])
print(next(fruits))  #apple
print(next(fruits))  #banana
print(next(fruits))  #melon
print(list(fruits))  #[] !오류 : 빈리스트
# enumerate를 객체 주소로 받는 경우 __next()__나 __iter__()를 통해서
# 구성요소를 참조할때마다 삭제 된다고 합니다 그래서 각각 1회 참조할수있다고 합니다.

# list()
list("Hi Hello")
['H', 'i', ' ', 'H', 'e', 'l', 'l', 'o']

# sorted(ilterable,key=None,reverse=False) 디폴트값들
# reverse=True > 정렬 후 역순
# 결과를 리스트로 변환
print(sorted([10,-4,5]))  #<[-4, 5, 10]>
print(sorted([10,-4,5],reverse=True))  #<[10, 5, -4]>
print(sorted("flower"))  #<['e', 'f', 'l', 'o', 'r', 'w']>
print(sorted("SunFlower",key=str.lower))  #<['e', 'F', 'l', 'n', 'o', 'r', 'S', 'u', 'w']>

# range() < 클래스
print(type(range(5)))  #<class 'range'>
print(list(range(5)))  #<[0, 1, 2, 3, 4]>
print(list(range(2,10,2)))  #<[2, 4, 6, 8]>
print(tuple(range(5)))   #<(0, 1, 2, 3, 4)>

# open(filename,[mode]) : mode로 파일 열기,디폴트는 r

# zip(*iteralble) : 각 iterable에서 동일한 인덱스의 요소를 추출하여 묶어서 return
print(zip([1,3,5],['cat','dog','horse']))
print(list(zip([1,3,5],['cat','dog','horse']))) #[(1, 'cat'), (3, 'dog'), (5, 'horse')]
print(list(zip([1,3,5],['cat','dog','horse','lion'])))  #[(1, 'cat'), (3, 'dog'), (5, 'horse')]
print(tuple(zip([1,3,5],['cat','dog','horse']))) #((1, 'cat'), (3, 'dog'), (5, 'horse'))
#딕셔너리로 만들기
keys = ['cat','dog','horse']
values = [1,3,5]
result = dict(zip(keys,values))
print(result)  #{'cat': 1, 'dog': 3, 'horse': 5}

#map() : 반복가능한 iteralbe 요소(리스트,튜플,문자열)를 지정된 함수로 처리 함수
# list(map(함수,리스트))
# tuple(map(함수,튜플))

a=[1.5,2.7,3.2,4.1]
a=list(map(int,a))  #숫자
b=list(map(str,range(10))) #문자열
print(a)  #[1, 2, 3, 4]
print(b)  #['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(list(map(int,b)))  #문자열 숫자로 변환 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 람다 식 : lambda


