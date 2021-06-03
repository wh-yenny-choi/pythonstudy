#예외 발생 상황

# ##ZeroDivisionError: division by zero
# # print(10/0)
# try:
#     print(10/0)
#     #print(10/2)
# except:
#     print('오류가 발생되었습니다')
# finally:
#     print('나누기')   #finally : 항상 나오는 코드

# #예외처리 클래스 지정
# try:
#     # print(10/0)
#     #print(10/2)
# except ZeroDivisionError:
#     print('0으로 나누었네요.')
# except Exception:
#     print('오류가 발생되었습니다')
# finally:
#     print('나누기')   #finally : 항상 나오는 코드

# try:
#     print(10/0)
#     #print(10/2)
# except ZeroDivisionError as e:
#     print('0으로 나누었네요. - ',e)
# except Exception:
#     print('오류가 발생되었습니다')
# finally:
#     print('나누기')   #finally : 항상 나오는 코드


##TypeError: can only concatenate str (not "int") to str
# print('age='+23)
# +는 문자끼리 연결

# try:
#     print('age'+23)
# except Exception as e:
#     print(e)       #can only concatenate str (not "int") to str

# try:
#     print('age'+23)
# except TypeError as e:
#     print(e)   #can only concatenate str (not "int") to str


#예외처리를 여러개 지정하더라도 가장 먼저 나온 에러만 처리
# try:
#     # print(10/0)       # 첫번째일때 division by zero
#     print('age='+23)   # 첫번쨰일때 can only concatenate str (not "int") to str
#     print(10 / 0)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)

#여러 개의 예외 처리 : 함께 처리 가능
# try:
#     print('age='+23)
#     print(10 / 0)
# except (ZeroDivisionError,TypeError) as e:
#     print(e)

# try:
#     num = int(input('input number : '))
# except ValueError:
#     print('정수가 아닙니다')
# else:
#     print(num)
# finally:
#     print('종료')

try:
    f=open('testex.txt','r')
except FileNotFoundError:
    pass
else:
    data = f.read()
    print(data)
    f.close()
finally:
    print('종료')



##NameError: name 'x' is not defined
# print(x)

##ValueError: incomplete format
# a=100
# print("%" %a)

##SyntaxError: invalid syntax
# if x>10
#     print('kim')

##IndexError: list index out of range
# a=[1,2,3]
# print(a[3])

##unboundLocalError :
# def add():
#     a += 1

##ModuleNotFoundError: No module named 'modd'
# import modd

##FileNotFoundError: [Errno 2] No such file or directory: 'readfile.txt'
# f = open('readfile.txt','r')
# data = f.read()

# #OSError: [Errno 22] Invalid argument: 'c:\readfile.txt'
# f=open('c:\readfile.txt','r')



