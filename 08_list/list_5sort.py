#리스트의 각 항목 요소를 정렬 : sort() 오름차순 , reverse() 내림차순

a = [3,6,0,-4,1]
print(a)     #<[3, 6, 0, -4, 1]>

a.sort()
print(a)     #<[-4, 0, 1, 3, 6]>
a.sort(reverse=True)
a.reverse()
print(a)    #<[-4, 0, 1, 3, 6]>

#reverse() : 메소드 사용하지 않고 리스트를 역순으로 생성하여 출력
b = []  #빈 리스트 지정
for i in range(len(a)):
    a.pop()   #맨 마지막 값 가져오면서 삭제
    item=a.pop()
    print(item)
    b.append(item)
    b.append(a.pop())
print(a)
print(b)

a = [3,6,0,-4,1]
#sorted()함수
c = sorted(a)
print(a)  #[3, 6, 0, -4, 1]
print(c)  #[-4, 0, 1, 3, 6]

string = ['GRAPE','Apple','aPPle','banana','melon','apple']
string.sort()
print(string)    #<['Apple', 'GRAPE', 'aPPle', 'apple', 'banana', 'melon']>
string.sort(key=str.lower)
print(string)    #<['Apple', 'aPPle', 'apple', 'banana', 'GRAPE', 'melon']>
string.sort(key=str.upper)
print(string)    #<['Apple', 'aPPle', 'apple', 'banana', 'GRAPE', 'melon']>


