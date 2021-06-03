#1에서 20까지 정수 중 3 배수 출력하고 합계

total=0
for i in range(3,21):
    if i%3==0:
        print(i, end=' ')
        total += i
print("\n합계 : {}".format(total))


sum = 0
for i in range (3,21,3):
    print(i, end=' ')
    sum += i
print('\n합계 : %d' %sum)


total = 0
for n in range (0,20,3):
    print (n, end=' ')
    total += n
print ('\n1~20사이의 3의 배수 합 : %d' %total)


print ('=================')
#range()의 step 인수 사용하지 않고 3의 배수 출력하고 합계

sum2 = 0
for i in range (3,21):
    if (i%3==0):
        sum2 += i
        print (i, end=' ')
    else :
        pass
print('\n합계 : %d' %sum2)


total = 0
for n in range(20):
    if n % 3 == 0:
        print(n, end = ' ')
        total += n
print('\n1~20사이의 3의 배수 합 : %d' %total)

total = 0
for n in [1,2,3,4,5,6]:
    x = n*3
    print (x, end=' ')
    total += x
print('\n1~20사이의 3의 배수 합 : %d' %total)
