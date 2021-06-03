# 1. my_variable 이름의 비어있는 튜플을 만들라.
my_Variable=tuple()

# 2. 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
print('튜플요소는 변경 불가능')

# 3. 숫자 1 이 저장된 튜플을 생성하라.
num_tuple = (1,)

# 4. 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
tuple

# 5. 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
print('5.')

t = ('a', 'b', 'c')
tt = list(t)
tt[0] = 'A'
t = tuple(tt)
print(t)

print('-------------------------')

# 6. 다음 튜플을 리스트로 변환하라.
print('6.')

interest = ('삼성전자', 'LG전자', 'SK Hynix')
print(type(interest))
interest_List = list(interest)
print(type(interest_List))

print('-------------------------')

# 7. 다음 리스트를 튜플로 변경하라.
print('7.')

interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(type(interest))
interest_Tuple = tuple(interest)
print(type(interest_Tuple))

print('-------------------------')

# 8. 파티에 참석한 사람이 다음과 같을 때 집합을 생성하고, 아래 조건에 맞게 출력하시오.
print('8.')

partyA = {"Park","Kim","Lee"}
partyB = {"Park","길동","몽룡"}

print('1) 파티에 참석한 모든 사람은? {}'.format(partyA|partyB))
print('2) 2개의 파티에 모두 참석한 사람은? {}'.format(partyA&partyB))
print('3) 파티 A에만 참석한 사람 {}'.format(partyA))
print('4) 파티 B에만 참석한 사람 {}'.format(partyB))

