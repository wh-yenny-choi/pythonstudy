#1. 회원이름 입력받아 회원명단 리스트 생성, 회원명단 리스트 내용 출력

nameL =[]
n=1
for name in range(3):
    name = input(f'회원 {n}입력: ')
    n += 1
    nameL.append(name)
print('회원 명단: {}'.format(nameL))

nameL = []
name = input('회원 입력 : ')
name2 = input('회원 입력 : ')
name3 = input('회원 입력 : ')
allL = [name,name2,name3]
print('회원 명단 : {}'.format(allL))
#리스트 앞 괄호

#2. 학생 수 입력받아 학생 수만큼 점수 입력받은 후 총점과 평균 계산, 80이상인 학생 수 출력. 학생 점수는 리스트로 생성
scores = []
n=total=avg=stu_hs=0
stu_num = int(input('학생 수 입력 : '))
for i in range(1,stu_num+1):
    score = int(input(f'학생{i} 점수 입력: '))
    total += score
    n += 1
    scores.append(score)
    if score >=80:
        stu_hs+=1

avg = total/n
print(f'총점 : {total}\n평균 : {avg}\n80점 이상 학생 : {stu_hs}')
print(scores)

scores = []
total=0
Name = int(input('학생 수 입력 : '))
for n in range(Name):
    score = int(input('학생 점수 입력 : '))
    total += score
    n += 1
    over = (score >= 80)
    over += 1

print('총점 : {}'.format(total))
print('평균 : %.2f' %(total/n))
print('80점 이상 학생 : %d'%over)


#3. 상품을 리스트에 추가하고 엔터키 누르면 입력종료, 등록된 상품 리스트 출력 코드
goodsL = []
while (1):
    goods = input('상품 등록 (엔터키 누르면 종료) : ')
    goodsL.append(goods)
    if goods == '':
        break

print(f'등록된 상품 : ',end='')
for i in range(len(goodsL)):
    print(goodsL[i],end=' ')


goodsL = []
count = 0
while True:
    goods = input('상품 등록 (엔터키 누르면 종료) : ')
    if goods == '':
        break
    else:
        goodsL.append(goods)
        count += 1
print('등록된 상품 : ',end='')
for i in range (count):
    print(goodsL[i],end=' ')
