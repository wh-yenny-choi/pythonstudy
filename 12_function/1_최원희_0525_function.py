#1
print("1번")
def print_coin():
    print("비트코인")

print(print_coin())

#2
print("\n2번")
print_coin()

#3
# print("\n3번")
# for i in range(100):
#     print_coin()

#4
# print("\n4번")
# def print_coins():
#     for i in range(100):
#         print("비트코인")

#5
print("\n5번")
print('hello 함수 정의 X')

#6
print("\n6번")
print('-----------내 예측 -------')
print('A\nB\nC\nA\nB')
print('-----------결과-----------')
def message() :
    print("A")
    print("B")
message()
print("C")
message()

#7
print("\n7번")
print('-----------내 예측 -------')
print('A\nA\nC\nB')
print('-----------결과-----------')
print("A")
def message() :
    print("B")
print("A")
print("C")
message()

#8. 아래 코드의 실행 결과를 예측하시오.
print("\n8번")
print('-----------내 예측 -------')
print('A\nC\nB\nE\nD')
print('-----------결과-----------')
print("A")
def messages1() :
    print("B")

print("C")
def messages2() :
    print("D")

messages1()
print("E")
messages2()

#9
print("\n9번")
print('-----------내 예측 -------')
print(': 가 생략되어있는 코드 > 오류발생, 수정후 결과 예측 \nB\nA')
print('-----------결과-----------')
def message1():
    print("A")
def message2():
    print("B")
    message1()

message2()

#10
print("\n10번")
print('-----------내 예측 -------')
print(': 가 생략되어있는 코드 > 오류발생, 수정후 결과 예측 \nB\nC\nA')
print('-----------결과-----------')
def message1():
    print("A")
def message2():
    print("B")
def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()
message3()

#11
print("\n11번")
def mul(x,y):
    return x*y
x=int(input('숫자1 입력 : '))
y=int(input('숫자2 입력 : '))

print('{} X {} = {}'.format(x,y,mul(x,y)))

#12
print("\n12번")
def text(ticker):
    return ticker.upper()

print("소문자 ticker를 대문자로 변환 => {}".format(text('ticker')))

#13. 함수로 인자로 리스트를 입력 받은 후 해당 리스트에서 짝수만 모아서 리턴하는 pickup_even() 함수를 작성하세요.
print("\n13번")
def pickup_even(a):
    p_list=[]
    for i in a:
        if i % 2 == 0:
            p_list.append(i)
    return p_list
num = 1,2,3,4,5,6,7,8,9
print('{} 중 짝수만 추출 : {}' .format(num, pickup_even(num)))



def sootja():
    e=[]
    while 1:
        n= input('숫자를 입력하세요.(엔터키 누르면 종료) : ')
        if n=='':   #엔터키 누르면 종료하게 하는것
           break
        else:
           e.append(int(n))
    return e

print(sootja())
def pickup_even():
    e = sootja()
    f=[]
    for i in e:
        if i % 2==0 :
            f.append(i)
        else:
            continue
    return f

pickup_even()
