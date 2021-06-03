# 리스트의 일치 검사

list1=[1,2,3]
list2=[1,2,3]
# == != > <
print(list1==list2)  #True
print(list1!=list2)  #False
print(list1>list2)   #False

# 2차원 리스트

list3=[[1,2,3],[4,5,6],[7,8,9]]
list4=[[1,2,3],[1,2],[1,3,4,5]]
print(list3)  #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in list3:
    print(i)  #한 행씩 출력

for i in list3:
    for j in i:
        print(j,end=' ')   #<1 2 3 4 5 6 7 8 9 >
    print()  #1 2 3
             #4 5 6
             #7 8 9
for i in list4:
    for j in i:
        print(j,end=' ')
    print()

list3=[[1,2,3,0],[4,5,6,1],[7,8,9,6]]
print(list3[1][1])  #<5>
print(len(list3))  #<3>
print(len(list3[0]))  #<4>

#2차원 리스트 연습 문제
#10명 학생 국,영,수 점수 2차원 리스트 형식저장, 세과목 총점, 평균, 과목점수와 함께 출력
#[90,85,70]
#[90,85,70], 245, 81.7
#test2