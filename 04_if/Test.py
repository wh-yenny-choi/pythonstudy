#1. 16진수 구분 코드 작성

jinsu = input("16진수 한 글자 입력 : ").upper()
if jinsu >= 'A' and jinsu <= 'F':
    result = int(jinsu,16)
    print('10진수 ==> %d' %result)
elif (jinsu >= '0' and jinsu <= '16'):
    result = int(jinsu,16)
    print('10진수 ==> %d' % result)
else:
    print("16진수 범위 내 입력하세요.")

try:
    num = int(input("16진수 한글자 입력 : "),16)
    print("10진수 ==> %d"%num)
except:
    print("16진수가 아닙니다.")

num = int(input('16진수 한 글자 입력 :'),16)
if (num):
    print('10진수 ==> %d' %num)
else :
    print('16진수가 아닙니다.')

'''
(num >= 'A' and num <= 'Z' or num >= 'a' and num <= 'z')
'''

print('=====================')

##2.잔돈 교환 프로그래밍
money = int(input('교환할 돈은 얼마 ? '))
a = money // 50000
b = money % 50000 // 10000
c = money % 10000 // 5000
d = money % 5000 // 1000
e = money % 1000 // 500
f = money % 500 // 100
g = money % 100 // 50
h = money % 50 // 10
rest = money % 10

print('50000원 %d장, 10000원 %d장, 5000원 %d장, 1000원 %d장, '
      '500원 %d개, 100원 %d개, 50원 %d개, 10원 %d개'
      %(a,b,c,d,e,f,g,h))
print('바꾸지 못한 돈 ==> %d원' %rest)


#divmod는 인자로 받은 두 수의 몫과 나머지를 튜플 형태로 반환한다.
money = int(input("교환할 돈은 얼마? "))
ohman,money = divmod(money,50000)
man,money = divmod(money,10000)
ohcheon,money = divmod(money,5000)
cheon,money = divmod(money,1000)
ohbaeg,money = divmod(money,500)
baeg,money = divmod(money,100)
ohsib,money = divmod(money,50)
sib,money = divmod(money,10)
print('50000원 %d장, 10000원 %d장, 5000원 %d장, 1000원 %d장, '
      '500원 %d개, 100원 %d개, 50원 %d개, 10원 %d개'
      %(ohman,man,ohcheon,cheon,ohbaeg,baeg,ohsib,sib))
print('바꾸지 못한 돈 ==> %d원' %money)


print('=====================')

#3. 주사위 게임

from random import randint
A = randint(1,7)
B = randint(1,7)
print('A의 주사위 숫자는 {}입니다.'.format(A))
print('B의 주사위 숫자는 {}입니다.'.format(B))
if A>B:
    print("A가 이겼다.")
elif A<B:
    print("B가 이겼다.")
else:
    print("비겼습니다.")


from random import randint
ANum = randint(1,7) #1이상 7미만범위
BNum = randint(1,7)
#A,B 가 던진 주사위 값이 저장 되는 부분
print('A의 주사위 숫자는 %d 입니다.' %ANum)
print('B의 주사위 숫자는 %d 입니다.' %BNum)
if(ANum > BNum):
    print('A가 이겼다.')
elif(ANum < BNum):
     print('B가 이겼다.')
else:
    print('비겼습니다.')

