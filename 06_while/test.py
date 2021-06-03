# # for i in range(4):
# #     for j in range(5):
# #         print('*', end=' ')
# #     print()
# #
# # #중첩for 이용
# #
# # for x in range(5):
# #     print('*', end='')
# # for x in range(4):
# #     print('*', end='')
# # for x in range(3):
# #     print('*', end='')
# # for x in range(2):
# #     print('*', end='')
# # for x in range(1):
# #     print('*', end='')
#
# #1. for문 이용 * 출력
#
# print('1)')
# for y in range (5,0,-1):
#     for x in range(y):
#         print('*', end=' ')
#     print()
#
# print('2)')
#
# for x in range(6):
#     for y in range(5,x,-1):  #4 5번째 자리까지 공백
#         print(' ', end=' ')
#     for z in range(x*2 - 1):
#         print('*', end=' ')#x자리에 별표 찍기
#     print()
#
# for j in range(5,0,-1):
#     for i in range(j):
#         print(' ', end='')  #앞에 4칸 > 3칸 > 2칸 > 1칸으로 반복하면서 빈칸 주기
#     for i in range(j):
#         print('*', end='')
#
# for i in range(1,6):
#     print(' '*(6-i)+'*'*(2*i-1))
#
# for i in range(1,6):
#     for j in range (5-i):
#         print(end=' ')
#     for j in range(1, 2*i):
#         print('*',end='')
#     for j in range(i,5):
#         print(end='')

# print('----------------------------')
#
# #2. 7입력까지 입력 반복, 7입력시 종료
# num=int(input("숫자 입력 : "))
# while True:
#     if num==7:
#         print("7입력! 종료")
#         break
#     else:
#         num=int(input("다시 입력 : "))
#
#
# num = int(input('숫자 입력 : '))
# # while (1):
# while num != 7:
#     num = int(input('다시 입력 : '))
#     if num == 7:
#         print("끗")
#         break
#
#     if num == 7:
#         print('7입력! 종료')  #print(num, '입력! 종료')
#         break
#     else:
#         num = int(input('다시 입력 : '))
#
# print('----------------------------')

# #3. 노래방 이용 프로그램
# 노래 1곡을 불렀습니다.
# 현재 8000원 남았습니다.
# 노래 2곡을 불렀습니다.
# 현재 6000원 남았습니다.
# 노래 3곡을 불렀습니다.
# 현재 4000원 남았습니다.
# 노래 4곡을 불렀습니다.
# 현재 2000원 남았습니다.
# 노래 5곡을 불렀습니다.
# 잔액이 없습니다. 종료합니다.

money=10000
song=rest=0
while True:
    for song in range(money):
        if money>0:
            song += 1
            print("노래를 {}곡 불렀습니다.".format(song))
            money -= 2000
            rest = money
            if rest>0:
                print("현재 {}원 남았습니다.".format(rest))
            elif rest==0:
                print("잔액이 없습니다. 종료합니다.")
                break

money = 10000
song = 0
while (1):
    for rest in range(money-2000,-1,-2000):
        song += 1
        print('노래 %d곡을 불렀습니다.' %song)
        if rest == 0:
            print('잔액이 없습니다. 종료합니다.')
        else:
            print('현재 %d원 남았습니다.' %rest)
    break


song = 0
money = 10000
while True:
    song += 1
    if money - 2000 * song == 0:
        print('노래를 {}곡 불렀습니다.\n잔액이 없습니다. 종료합니다.' .format(song))
        break
    else:
        print('노래를 {}곡 불렀습니다.\n현재 {}원 남았습니다.' .format(song,money- 2000 * song))
