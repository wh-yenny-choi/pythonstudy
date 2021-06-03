#정수 3개를 입력받아서 제일 큰 수 출력

a = int(input('정수1 입력:'))
b = int(input('정수2 입력:'))
c = int(input('정수3 입력:'))

if(a>b and a>c):
    max_num = a
elif (b>a and b>c):
    max_num = b
else:
    max_num = c
print('제일 큰 수: %d' %max_num)


#최소값 출력
a = int(input('정수1 입력:'))
b = int(input('정수2 입력:'))
c = int(input('정수3 입력:'))
if(a<b and a<c):
    min_num = a
elif(b<c and b<c):
    min_num = b
else:
    min_num =c
print('제일 작은 수: %d' %min_num)