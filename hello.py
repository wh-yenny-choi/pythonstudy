# 첫번째 프로그램

# print ('Choi wonhee')


# 변수에 값을 저장
x=10
y=20
z=30

print (x,y,z)
print (x)
print (y)
print (z)

# 여러개의 변수에 여러개의 값을 각각 저장
x, y, z = 10, 20, 30

print (x,y,z)
print (x)
print (y)
print (z)

#여러개의 변수에 동일한 값을 할당
a=b=c=100

print (a,b,c)



#두 변수의 값을 교환 (swap)
a, b= 10, 20

print('a=', a)
print('b=', b)


print ('[swap]')

c=a
a=b
b=c


a,b=b,a

print('a=', a)
print('b=', b)


# 변수를 삭제

x=100
print (x)
print(id(x))
print(type(x))

del x

print (x)


# 문자열에 큰 따옴표 사용

name = "최원희"
age = 27

print (name, age)

address = '경기도 부천시'

# str() : 형변환 함수, 숫자형을 문자열로 변환
# + : 문자만 연결
# , : 숫자, 문자 연결

print (name + "는 " + address + "에 삽니다.")
print (name + '는 ' + address + '에 삽니다.')
print (name + '는 ' + str(age) + '살 입니다.')
print (name + '는 ', age , '살 입니다.')


# 사각형의 면적을 구하는 프로그램

width = 100
height = 50
area = width * height
print ('사각형의 면적은', area)

# 변수 연습문제1
name = '홍길동'
no = 2016001
year = 4
grade = 'A'
average = 93.5

print ('성명 :' ,name)
print ('학번 :' ,no)
print ('학년 :' ,year)
print ('학점 :', grade)
print ('평균 :', average)

name, no, year, grade, average ='홍길동', 2016001, 4, 'A', 93.5
print ('성명 : ' + name)
print ('학번 :', no)
print ('학년 :', year)
print ('학점 : '+ grade)
print ('평균 :', average)

name = '홍길동'
no = 2016001
year = 4
grade = 'A'
average = 93.5



#포맷함수

print ('성명 : %s' % name)
print ('학번 : %s' %no)
print ('학년 : %d' %year)
print ('학점 : %s' %grade)
print ('평균 : %.2f' %average)

print ('이름 : %s, 학년 : %d' %(name,year))


# %로 출력

rate = 80
print ('이름 : %s, 출석률 : %d%%' %(name,rate)) #반드시 괄호로 묶는다.
print (format (average, '.2f'))


#포맷 코드 연습문제

kor=90
eng=80
math=80
sum = kor+eng+math
ave = sum/3
print('총점: %d'%sum, '평균: %.2f'%ave)
print('총점: %d, 평균: %.2f' %(sum,ave))


INT_Rate = 0.03

deposit = 10000
interest = deposit * INT_Rate
balance = deposit + interest

print(balance)
print(int(balance)) #정수형으로 변환, 천단위 구분 기호 사용
print(format(int(balance), ','))

print("first", end='@')
print("second")


print('하하하')
print(200 + 100)
print('200 + 100')
print(int('200') + 100)


print('%05d' % 543)
print('%10s' % '파이썬')
print('%1.1f ' % 123.45)


print('500 + 500')
print('%d' % (500 + 500))
print('%d' % (500, 600))
print('%d %d' % (700))

print('%d / %d = %d' % (10, 4, 10 / 4))
print('%d / %d = %f ' % (10, 4, 10 / 4))
print('%d / %d = %5.1f ' % (10, 4, 10 / 4))
print('%d / %d = %5.0f ' % (10, 4, 10 / 4))

'''

print('%1.1f ' % 123.45)
'''