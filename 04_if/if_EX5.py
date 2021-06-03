#도형 선택해서 면적 구하기

# <출력결과>
#
# 도형입력(1: 사각형, 2: 삼각형, 3: 원) : 1
# 가로입력 : 10
# 세로입력 : 20
# 사각형의 면적 = 200

# 도형입력(1: 사각형, 2: 삼각형, 3: 원) : 2
# 밑변입력 : 10
# 높이입력 : 20
# 삼각형의 면적 = 100
#
# 도형입력(1: 사각형, 2: 삼각형, 3: 원) : 3
# 반지름입력 : 10
# 원의 면적 = 314.16


# num = int(input('도형입력(1: 사각형, 2: 삼각형, 3: 원) : '))
# if num == 1:
#     garo = int(input('가로 입력 : '))
#     sero = int(input('세로 입력 : '))
#     print('사각형의 면적 = {}' .format(garo*sero))
# elif num == 2:
#     width = int(input('밑변 입력 : '))
#     height = int(input('높이 입력 : '))
#     print('삼각형의 면적 = {}'.format(width*height/2))
# else:
#     half = int(input('반지름 입력 : '))
#     print('원의 면적 = {}'.format(half**2*3.14))


shape = input("도형 입력(1: 사각형, 2: 삼각형, 3: 원) : ")
if shape == '1':
    w = int(input("가로 입력 : "))
    h = int(input("세로 입력 : "))
    a = w * h
    print("사각형의 면적 = %d" % a)
elif shape == '2':
    w = int(input("밑변 입력 : "))
    h = int(input("높이 입력 : "))
    a = w * h / 2
    print("삼각형의 면적 = %d" % a)
else:
    r = int(input("반지름 입력 : "))
    a = r**2*3.141592
    print("원의 면적 = %.2f" % a)



a = input('도형입력(1: 사각형, 2: 삼각형, 3: 원) :')
if (a == '1'):
    w = int(input('가로입력:'))
    h = int(input('세로입력:'))
    num1 = w*h
    print('사각형의 면적 = %d' %num1)
elif (a == '2'):
    w = int(input('밑변입력:'))
    h = int(input('높이입력:'))
    num2 = w*h/2
    print('삼각형의 면적 = %d' %num2)
elif (a == '3'):
    r = int(input('반지름입력:'))
    num3 = r**2*3.14
    print('원의 면적 = %f' %num3)
else:
    print('실패')
