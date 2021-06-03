#두 숫자를 입력받아 이 수 사이의 숫자의 합 구하기

total=0
num1=int(input("입력1 : "))
num2=int(input("입력2 : "))
for i in range(num1,num2+1):
    total += i
print("{}과 {}사이의 합은 {}".format(num1,num2,total))


total = 0
num1 = int(input('숫자1 입력 : '))
num2 = int(input('숫자2 입력 : '))
for i in range(num1,num2):
    total += i
print('%d과 %d 사이의 합은 %d' %(num1,num2,total))

'''
if (num1 <= num2):
for i in range(num1, num2+1):
sum += i
else:
for in in range(num2, num1+1):
sum += i
'''

#단 수 입력받아 해당 구구단 출력

#dan=int(input("단 수 입력 : "))
print("구구단을 외우자")
for x in range(1,10):  #n = 앞글자
    for y in range(9):
        y += 1
        print("{}X{}={}".format(x,y,(x*y)))


num3 = int(input('단 수 입력 : '))
for i in range(10):
    print('%d X %d = %d' %(num3,i,num3*i))

for dan in range(2.10):
    for n in range(1,10):
        print('%d * %d = %d'%(dan,n,dan*n))
        #print('%d * %d = %2s'%(dan,n,dan*n))

#카운트 다운 프로그램 작성

count = int(input("시작 숫자를 입력하시오 : "))
for i in range(count,0,-1):
    print("{}".format(i),end=' ')  #print(i,end=' ')
print("발사")

num4 = int(input('시작 숫자를 입력하시오 : '))
for i in range (int(num4),0,-1):
    print(i, end=' ')
print('발사')