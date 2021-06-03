# #리스트에 저장되어 있는 성적에 따라 합격 불합격을 판별하시오
# #리스트에 저장된 점수가 60점 이상이면 합격 아니면 불합격
# #출력 양식 : 리스트 저장 순서에 따라
# #1번 90점 합격
# score_list = [90,57,88,45,78]
# num=0
# for score_list in score_list:
#     num+=1
#     if score_list>=60:
#         result="합격"
#     else:
#         result="불합격"
#     print("{}번 {}점 {}".format(num,score_list,result))
#
# #필요변수 생성
# s = [90,57,88,45,78] #리스트 변수 생성, 리스트는 []안 요소를 나열해서 생성
# num = 0
#
# for s in s :
#     num += 1
#     if s >= 60 :
#         result = '합격'
#     else :
#         result = '불합격'
#     print ('%d번 %d점 %s' %(num,s,result ))


#숫자 10개를 입력받아서 양,음,0의 개수 출력
pos=neg=zero=0
for i in range(1,11):
    num = int(input("숫자{} 입력 : ".format(i)))
    if num>0:
        pos+=1
    elif num<0:
        neg+=1
    else:
        zero+=1
print('------------')
print("양의 개수 : {}\n음의 개수 : {}\n0의 개수 : {}".format(pos,neg,zero))


num = plus = minus = zero = 0
for i in range(1,11):
    num = int(input('숫자%d입력 : ' %i))
    if(num>0):
        plus += 1
    elif (num<0):
        minus += 1
    else :
        zero += 1
print('----------------')
print('\n양의 개수 : %d \n음의 개수 : %d \n0의 개수 : %d' %(plus,minus,zero))


pos, neg, zero = 0,0,0
for i in range(10):
    number = int(input('숫자 {} 입력 :'.format(i+1)))
    #input('숫자 %d 입력 : ' %(i+1))
    if number > 0:
        pos += 1
    elif number == 0:
        zero +=1
    else:
        neg += 1
print('--------------------')
print('양의개수 : %d' %pos)
print('음의개수 : %d' %neg)
print('0의개수 : %d' %zero)
