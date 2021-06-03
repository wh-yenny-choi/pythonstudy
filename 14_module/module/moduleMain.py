#main Example

name='' #name이라는 이름으로 전역변수 생성

def inputName():  #name변수 지정
    global name #전역번수 name 사용 > return 사용 필요x
    name=input('이름 입력 : ')
    #return name

def getName():  #name변수를 가져옴
    if name =='' :
        return '무명씨'
    else:
        return name

def main():
    inputName()
    print(getName())

if __name__ == '__main__':
    main()

# __name__: 스페셜변수