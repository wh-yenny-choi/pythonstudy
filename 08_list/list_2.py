# 리스트의 주요 메소드

# 리스트의 길이 계산 함수 : Len(리스트명)
# 리스트의 요소 몇개인지 찾는 메소드 : count()
# 리스트 요소 추가, 삽입 메소드 : append(), insert()
# 리스트의 요소 제거 : remove(), pop()
# 리스트의 길이 확장 : extend()
# 리스트의 각 항목 요소를 정렬 : sort() 오름차순 , reverse() 내림차순
# 리스트의 요소 찾기 : index()
# 리스트의 요소 중 큰 값(max()), 작은 값(min())


# 리스트의 길이 계산 함수 : Len(리스트명)
a = [1,2,3,4,5,6]
print('리스트의 길이 %d' %len(a))  #리스트의 길이 6

# 리스트의 요소 몇개인지 찾는 메소드
print(a.count(3))   #3의 개수 1
# a = [1,2,3,4,5,6,3,3]
# print(a.count(3))   #3의 개수 3

# 리스트 요소 추가, 삽입 메소드 : append(), insert()
a.append(100)  #새로운 요소를 뒤쪽에 추가
print(a)  #[1, 2, 3, 4, 5, 6, 100]
a.append([110,120])  #새로운 리스트형태의 요소를 뒤쪽에 추가
print(a)  #<[1, 2, 3, 4, 5, 6, 100, [110, 120]]>

a.insert(2,120)  # (삽입하고자 하는 위치, 삽입하고자 하는 내용)
print(a)         # 2번째 자리에 120 삽입  <[1, 2, 120, 3, 4, 5, 6, 100, [110, 120]]>

b = []
print(b)       #<[]>
b.append(5.5)
print(b)       #<[5.5]>
b.append(10.5)
print(b)       #<[5.5, 10.5]>
b.append(6.5)
print(b)       #<[5.5, 10.5, 6.5]>

scores = []
for i in range(10):
    score = int(input('점수입력:')) #실수 > float, 숫자 > int
    #scores.append(score)
    scores.insert(0, score)

print(scores)
total = n = 0
scores = []
for i in range(3):
    score = int(input('점수 입력 : '))
    scores.append(score)
    total += score
    n += 1
print(scores)
print(f'총합 {total},평균 {total/n}')