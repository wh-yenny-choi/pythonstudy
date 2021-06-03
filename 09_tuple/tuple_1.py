#집합적 자료형 : tuple
#삭제, 추가, 변경 불가
#리스트 생성 : List() or []
#tuple 생성 : tulpe() or ()

t1 = tuple()
t2 = ()

t1=(1,2,3)
print(t1)  #<(1, 2, 3)>
print(type(t1))  #<<class 'tuple'>>

t2=1,3,4
print(t2)  #<(1, 3, 4)>
print(type(t2))   #<<class 'tuple'>>

t3=t1,(5,6,7)
print(t3)  #<((1, 2, 3), (5, 6, 7))>

t4=[1,4],[5,6]
print(t4)  #<([1, 4], [5, 6])>
print(type(t4))

t5=tuple([1,4]) #list -> tuple
print(t5)  #<(1, 4)>

#튜플의 요소 다루기, 요소 변경 불가
print(t1[2])  #<3>
# t1[2]=10 #튜플요소 변경 불가능

# #요소 추가 및 삭제 불가
# t1.append(-9)
# del(t1[2])

#튜플 자체 삭제는 가능
list=[1,2,3]
del(list[1])
print(list)  #<[1, 3]>

del(t1)
print(t1)

#tuple.index(), .count()
tt='a','b','c','e','a','b'
i=tt.index('e')
print(i)    #<3>
c=tt.count('a')
print(c)    #<2>

#slicing
t=tt[:]
t=tt[1:5]
print(t)   #<('b', 'c', 'e', 'a')>

# +, * 연산
print(t1+t2)  #<(1, 2, 3, 1, 3, 4)>
print(tt*2)   #<('a', 'b', 'c', 'e', 'a', 'b', 'a', 'b', 'c', 'e', 'a', 'b')>


#tuple 연습문제
tt=((1,2,3),(4,5,6),(7,8,9))
print(tt[1][2])  #<6>

#출력결과
#1 2 3
#4 5 6
#7 8 9

for i in tt:
    for j in i:
        print(j,end=' ')
    print()


for i in tt:
    for j in i:
        print(j,end=' ')
    print()
# a = [[1,2,3],[4,5,6],[7,8,9]]
# for i in a:
#     for j in i:
#         print(int(j+i*3),end=' ')
#     print()

#tuple 요소 추가
#출력결과 (10,20,30,40)

myTuple=(10,20,30)
print(type(myTuple)) #<<class 'tuple'>>
myList=list(myTuple)
print(type(myList))  #<<class 'list'>>
print(myList)  #<[10, 20, 30]>
myList.append(40)
print(myList)  #<[10, 20, 30, 40]>
myTuple=tuple(myList)
print(myTuple)  #<(10, 20, 30, 40)>

t4=[1,4],[5,6]
print(t4[0])  #<[1, 4]>
print(type(t4[0]))  #<<class 'list'>>
t4[0][0]=10
print(t4)  #<([10, 4], [5, 6])>


