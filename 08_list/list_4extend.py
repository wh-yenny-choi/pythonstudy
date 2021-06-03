#리스트의 길이 확장 : extend()
#extend() : append() + insert()

#append > 맨뒤 추가
#insert > 지정위치 추가

a = [3,6,0,-4,1]
b = [40,30,20,50]
# a.append(b)
# print(a)         #<[3, 6, 0, -4, 1, [40, 30, 20, 50]]>
# a.insert(2,b)
# print(a)         #<[3, 6, [40, 30, 20, 50], 0, -4, 1, [40, 30, 20, 50]]>
a.extend(b)
print(a)           #[3, 6, 0, -4, 1, 40, 30, 20, 50]