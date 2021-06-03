#calculator module
#계산기 함수 : add(x,y), sub(x,y), mul(x,y), div(x,y)



def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y


print('calculator.py __name__: ' ,__name__)


# __name__ 변수 사용 : ' __ main()__'
if __name__ == '__main__':
    print('Here is Calculator module') #메인변수
    print('__name__: ' ,__name__)


print('Here is Calculator module')  