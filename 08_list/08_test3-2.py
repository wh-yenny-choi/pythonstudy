print('4. 학생 점수 내림차순 정렬 출력 추가')

# total=over=0
# scoreL = []
# Name = int(input('학생 수 입력 : '))
# for n in range(Name):
#     score = int(input('학생%d 점수 입력 : ' %(n+1)))
#     total += score
#     n += 1
#     if (score>=80):
#         score=over
#         over += 1
#     #scoreL.append(score)
# #scoreL.sort(True)
#
# print('총점 : {}'.format(total))
# print('평균 : %.2f' %(total/n))
# print('80점 이상 학생 : %d'%over)
# print('점수 내림차순 정렬 : {}'.format(scoreL))
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
scores.sort(reverse=True)
avg = total/n
print(f'총점 : {total}\n평균 : {avg}\n80점 이상 학생 : {stu_hs}')
print('점수 내림차순 정렬 : ',end='')
for c in scores:
    print(c,end=' ')


print('\n\n5.사자성어 맞추기 게임')

word_L = ['개과천선','구사일생','군계일학','무용지물','동고동락','유비무환','입신양명','괄목상대','막역지우','고장난명']
meaning_L = ['잘못을 고치고 옳은 길에 들어섬','죽을 고비를 여러 번 겪으며 살아나다','평범한 사람 가운데 뛰어난 사람',
             '아무짝에나 쓸모 없는 것','고통과 증거움을 함께 한다','미리 준비해두면 근심 걱정이 없다',
             '사회적으로 인정받고 출세하여 이름을 세상에 드날림','다른 사람의 학식이나 업적이 크게 진보한 것을 말함',
             '생사를 같이 할 수 있는 친밀한 벗','상대 없이 혼자서는 어떤 일을 이룰 수 없다']
print('사자성어 맞추기 게임을 시작합니다.')
print('-'*30)
from random import randint
num = randint(1,11)
while 1:
    print(meaning_L[num])
    anwer = input('사자성어 : ')
    if word_L[num] == anwer:
        print('정답!')
        break
    else:
        print('오답. 다시도전!')


# from random import randint
# num = randint(1,11)
# meaning = meaning_L[num]
# while True :
#     print(meaning)
#     A = input('이말의 사자성어는? : ')
#     if (word_L[num] == A):
#         print('맞습니다. 게임을 종료합니다.')
#         break
#     else:
#         print('틀렸습니다. 다시 도전!')


# from random import randint
# num = randint(1,11)
# meaning = meaningL[num]
# while True:
#     print(meaning)
#     answer = input("이말의 사자성어는? : ")
#     if(sajaL[num] == answer):
#         print("맞습니다.. 게임을 종료합니다.")
#         break
#     else:
#         print("틀렸습니다...다시 도전!")
