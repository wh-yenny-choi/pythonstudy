#리스트의 기본 개념
#리스트 요소는 다양하게 가질 수 있음

intL = [1,3,2,10]
floatL = [1.5,3.2,5.4]
nameL = ['홍','성','변','방']
numL = [1,3,4,[1,2]]  #리스트 안에 리스트 가능
samL = [1,3,.5,'하하']

print(intL)  #[1, 3, 2, 10]
print(type(intL))  #<class 'list'>
print(numL)  #[1, 3, 4, [1, 2]]
print(samL)  #[1, 3, 0.5, '하하']

for x in numL:
    print(x)
# 출력결과값 : 15번 for문 = 18번 for문
for i in range(0,len(numL)):
    print(numL[i])

a,b,c = floatL
print(a)
print(b)
print(c)


intL = [1,3,2,10]
floatL = [1.5,3.2,5.4]
nameL = ['홍','성','변','방']
numL = [1,3,4,[1,2]]  #리스트 안에 리스트 가능
samL = [1,3,.5,'하하']

#인덱싱(indexing) :각각의 요소를 가져옴
#슬라이싱(slicing)
print(nameL[-1])  #맨 뒤의 요소를 프린트 <방>
print(nameL[:])   # :(콜론) 이용시 전체 요소 프린트 ['홍', '성', '변', '방']
print(nameL[1:3]) # 1~2의 요소 프린트  ['성', '변']
print(numL[-1])  #리스트 마지막  [1, 2]
print(numL[-1][0]) #리스트 안의 리스트에서 0번째 요소 프린트 []한 번 더 사용 1

#allL = []   #빈 리스트 생성
#allL = list()  #빈 리스트 생성

allL = [intL, floatL, nameL, numL]
print(allL)  #<[[1, 3, 2, 10], [1.5, 3.2, 5.4], ['홍', '성', '변', '방'], [1, 3, 4, [1, 2]]]>
print(allL[-1])  #<[1, 3, 4, [1, 2]]>
print(allL[-1][-1][0])  #<1>

print(nameL[:-1])  #맨마지막 리스트 +1 된 위치까지      <['홍', '성', '변']>
print(nameL[-1:])  #맨 마지막꺼만 가져옴 , 리스트의 형태  <['방']>
print(nameL[-1])   #요소만 가져옴                     <방>
n = len(nameL)
print(nameL[:n])   #<['홍', '성', '변', '방']>

# 리스트의 +, * 연산 
sumL=numL+samL
print(sumL)  #[1, 3, 4, [1, 2], 1, 3, 0.5, '하하']
print(numL*3)  #[1, 3, 4, [1, 2], 1, 3, 4, [1, 2], 1, 3, 4, [1, 2]]

# 리스트의 내용 변경
print(numL) #<[1, 3, 4, [1, 2]]>
numL[3]=10  #3번째 위치에 10 할당, 값의 내용 변경
print(numL) #[1, 3, 4, 10]
numL[2:4] = []  #2~3까지 빈 리스트로 변경
print(numL)  #[1, 3]

# test1