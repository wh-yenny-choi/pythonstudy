#산술연산자 : +, -, *, /, //, %, **
#할당연산자 : =
#대입연산자 : +=, -=, *=, /=, //=, %=, **=
#관계연산자 : >, <, >=, <=, ==, !=  => 결과값이 참(True), 거짓(False)
#논리연산자 : and, or, not
#비트연산자 : 정수를 2진수로 변환한 수 각각의 비트별로 연산

#산술연산자 우선 순위 : () > 지수** > 곱셈 = 나눗셈 = 몫  > 덧셈 = 뺄셈


#문제 10000초는 몇시간 몇분 몇초인가?
s = 10000
m = s // 60
r = s % 60
h = m // 60
print('%d분 %d초' %(m,r))

secs=10000%60
min=(10000%3600) // 60
hour=10000 // 3600
print('10000초는 %d시간 %d분 %d초 입니다.'%(hour,min,secs))


a = 100
a += 10

sum = 1
sum = sum + 2
sum += 2
print(sum)
'''
b -= 10 #b=b-10
c *= 10 #c=c*10
d /= 10 #d=d/10
e **= 3 #e=e**3
'''
100 > 3 #True
a = 100
b = 1001
a > b
print(a>b)
print(a!=b)
print(a>b and b==1001)# and연산 > 곱하기 or연산 > 더하기 (둘중 하나만 참이여도 참)
print(a>b or b==1001)
print(not(a>b))
# &(논리곱), |(논리합), ^(xor), ~(not), <<(왼쪽시프트), >>(오른쪽시프트)
print(10&3) #1010 & 0011 => 0010
print(10|3) #1010 | 0011 => 1011
print(10^3) #1010 ^ 0011 => 1001
print(~3)   #~0011 => 1100
print(~3+1)
print(10<<1)
print(10<<2)
print(10<<3)
print(10>>1)
print(10>>2)
print(10>>3)

print('잔액:', format(1235000, ',.0f'))
#<잔액: 1,235,000>
print('잔액:', format(1235000.123, ',.1f'))
#잔액: 1,235,000.1
print('잔액:', format(1235000, ',d'))
#잔액: 1,235,000


#현금이 5000원이 있고, 사탕가격이 120원인경우
#최대한 살 수 있는 사탕의 개수와 나머지 돈은 얼마인가?

a = 5000 // 120
b = 5000 % 120
print('살 수 있는 사탕개수:%d' %a, '나머지 돈:%d' %b)

'''
money = 5000
candyP= 120
num = money // candyP

'''





