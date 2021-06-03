#값 추가,삭제 가능 / 변경 불가능

#set()함수로 집합 만들기  {}안에는 숫자,문자 모두 가능
s1={1,2,3,4,5}
print(s1)  #<{1, 2, 3, 4, 5}>
print(type(s1))  #<class 'set'>

s2=set([10,20,30])  #{}로 집합 만들 수 있다, 리스트로 집합 생성
print(s2)  #<{10, 20, 30}>
print(type(s2))  #<class 'set'>

s3=set((100,200,300))  #튜플로 집합 생성
print(s3)  #<{200, 100, 300}>
print(type(s3))  #<<class 'set'>>

#인덱스 사용 불가 특징지님
#s1[0]

#데이터 추가 .add  (append -> x)
s2.add(90)
print(s2)   #<{10, 20, 90, 30}>
s1.add(-9)
print(s1)   #<{1, 2, 3, 4, 5, -9}>

#데이터 삭제 .remove()
s1.remove(-9)
print(s1)   #<{1, 2, 3, 4, 5}>
# s1.remove(8)
# print(s1)   #값 에러 발생
s1.discard(0)
s1.discard(7)
s1.discard(4)
print(s1)   #<{1, 2, 3, 5}> 값이 없어도 에러 발생 X

s1.clear()
print(s1)  #<et()>

#집합 연산 : union, intersection, difference

s1 = {3,4,1,6}
s2 = {2,4,1,8}
print(s1.union(s2))  #<{1, 2, 3, 4, 6, 8}> 합집합, 중복 없이 정렬
print(s1.intersection(s2))  #<{1, 4}> 교집합
print(s1.difference(s2)) #<{3, 6}> 차집합
print(s2.difference(s1)) #<{8, 2}>

print(s1|s2)  #<{1, 2, 3, 4, 6, 8}>
print(s1&s2)  #<{1,4}>
print(s1-s2)  #<{3,6}>

#set 컴프리핸션
a={x for x in 'abracadabra' if x not in 'abc'}
print(a)

#mutable : 변경가능 / Immutable : 변경 불가능

