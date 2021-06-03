#2차원 리스트 연습 문제
#10명 학생 국,영,수 점수 2차원 리스트 형식저장, 세과목 총점, 평균, 과목점수와 함께 출력
#[90,85,70]
#[90,85,70], 245, 81.7
total = 0
score = [[90,85,70],[88,71,92],[100,100,90],[90,60,50]]
for i in score:
    total += i
    print(f'총합 {total}')

score = [[90, 85, 70], [88, 72, 92], [100, 100, 90], [90, 60, 50], [60, 90, 75], [88, 66, 77], [100, 100, 100], [62, 77, 56], [100, 60, 50], [67, 89, 93]]
for i in score:
    sum = 0
    for j in i:
        sum += j
    avg = sum / 3

    print('{}, {}, {:.1f}'.format(i, sum, avg))


total = n = 0
score = [[90,85,70],[88,71,92],[100,100,90],[90,60,50]]
for n in score:
    total = sum(n)
    avg = total / len(n)
    print(n, '총점 : %d' %total, '평균 : %d' % avg)


# n= score[0][0]+score[0][1]+score[0][2]
# print(score[0], '총점 : %d' %n, '평균 : %d' %(n

'''
score = [[90,85,70],[88,71,92],[100,100,90],[90,60,50]]
for i in score:
    total = sum(i)
    avg = total/3
print('{},{},{:.2f}' .format(i,total,avg))

# sum=avg=0
# kor = int(input('국어 점수 입력 : '))
# eng = int(input('영어 점수 입력 : '))
# math = int(input('수학 점수 입력 : '))
# sub_list = [kor,eng,math]
# sum = kor+eng+math
# avg = sum/3
# print(sub_list,' %d'%sum,' %.2f'%avg)

score_list = [[90,85,70],[88,71,92],[100,100,90],[90,60,50]]
for i in score_list:
    scores=sum(i)
    avg=scores/len(i)
    print(i,' %d' %scores,' %.2f' %avg)

#print("")
'''

list2 = [[90,85,70], [88,72,92], [100,100,90],
         [90,60,50], [50,100,60], [80,50,50],
         [100, 100, 100], [85,95,95], [90,90,93],
         [100,80,90]]

totalList = []
avgList = []

total = 0
avg = 0
for i in range(0,10):
    for j in range(3):
        total += list2[i][j]
        avg = total / 3
        totalList.append(total)
        avgList.append(avg)
    print(list2[i], end = ", ")
    print("%d, %.2lf" %(total, avg))
