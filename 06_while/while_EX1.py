#1~100까지의 정수 중 3의 배수의 합을 출력

n = 1
sum = 0
while n <= 100:
    if n%3 == 0:
        sum += n
    n += 1
print('1부터 100까지의 모든 3의 배수의 합은 %d입니다.' %sum)

n = 0
sum = 0
while n <= 100:
    sum += n
    n += 3
print('1부터 100까지의 모든 3의 배수의 합은 %d입니다.' %sum)

n=1
sum=0
while n*3 <= 100:
    sum += (n*3)
    n += 1
print('1부터 100까지의 모든 3의 배수의 합은 %d입니다.' %sum)