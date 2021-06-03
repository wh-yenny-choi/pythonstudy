#팩토리얼 계산 함수 factorial()
# n! = n*(n-1)*(n-2)*...*2*1

def factorial(n):
    pass

#print(factorial(3))
result=factorial(3)
print(result)

def factorial(n):
    a=n
    for i in range(a-1,0,-1):
        a*=i
    return a
print(factorial(3))

def factorial(n):
    answer = 1
    for i in range(int(n)):
        answer *= (i + 1)
    return answer
print(factorial(5))

def factorial(n):
    return n*factorial(n-1) if n>1 else 1
n = int(input('n = '))

def factorial(n):
    f = 1
    for i in range(n):
        f *= (i+1)
    return print(f)
factorial(n)

#재귀함수 , 메모리 차지 많이 함
def factorial(n):
    if n== 1:
        return 1
    return n*factorial(n-1)

f(4) : 4*f(3) = 4*3*2*1
f(3) : 3*f(2) = 3*2*1
f(2) : 2*f(1) = 2*1
f(1) : 1

