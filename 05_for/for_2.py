for i in range(10):  #range(0,11,1) 증가 >(초기,끝-1까지,증가)
    print (i, end=' ')

print('\n---------------')

for i in range(1,10):
    print(i, end=' ')

print('\n---------------')

for i in range(2,11,2):
    print(i, end=' ')    #<2 4 6 8 10 >

print('\n---------------')

for i in range(12,1,-1):  #감소 > (초기, 끝+1까지 , 감소)
    print(i, end=' ')     #<12 11 10 9 8 7 6 5 4 3 2 >

print('\n---------------')

#1~10사이 수를 더하고 더한 결과 출력

total=0
for n in range (11):
    total += n  #total = total + n
print('합은 %d' %total)