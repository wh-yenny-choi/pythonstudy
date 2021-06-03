#리스트의 요소 제거 : remove(), pop()

#remove(삭제하려는값) : 가장 첫번째 만나는 값을 삭제

n = [1,2,3,4,5,3,4,-1,-5,10]
#n.remove(20)
print(n)
cnt = n.count(3)
print(cnt)

#pop() : 가장 맨뒤의 메소드를 가져옴 or 지정 인덱스 위치 값 가져옴
#pop() : 맨마지막 값은 삭제, pop(index) : index위치의 값을 삭제, 반환
data = n.pop()
print(n)
print(data)

data = n.pop(4)
print(n)
print(data)