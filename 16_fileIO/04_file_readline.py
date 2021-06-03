# readline() 함수 이용하여 파일 읽어오기

# readline() : 1개의 행씩 읽어 오기, 행 끝에 '\n' 포함
# readlines() : 모든 행을 읽어 라인 단위별로 잘라서 리스트를 생성 (문자열 형태로)
#               ['..(데이터)..\n','..(데이터)..\n',...,'..(데이터)..\n']
# read() : 내용 전체를 한 문자열로 반환

print('-----첫번째 행 읽어오기-----')
f=open('test.txt','r')
line = f.readline()
print(line)
f.close()

#utf-8저장된 파일 읽기
f=open('test.txt','r')
line = f.readline()
print(line)
f.close()
#오류발생
#UnicodeDecodeError: 'cp949' codec can't decode byte 0xeb in position 6: illegal multibyte sequence

# 인코딩 utf-8로 지정하여 해결
f=open('test.txt','r',encoding='utf-8')
line = f.readline()
print(line)
f.close()
# -----첫번째 행 읽어오기-----
# 안녕하세요. 최원희입니다.

#여러 줄 읽기
f=open('test.txt','r',encoding='utf-8')
line = f.readline()
print(line)
line = f.readline()
print(line)
f.close()
#출력 형식 :
# -----첫번째 행 읽어오기-----
# 안녕하세요. 최원희입니다.
#
# 지금 파이썬을 공부하는 중이에요

f=open('test.txt','r',encoding='utf-8')
line = f.readline()
print(line, end='')
line = f.readline()
print(line)
f.close()
#-----첫번째 행 읽어오기-----
# 안녕하세요. 최원희입니다.
# 지금 파이썬을 공부하는 중이에요


#-----파일 전체 읽기-----
print('-----파일 전체 읽기-----')
# f=open('test.txt','r',encoding='utf-8')
# line = f.readline()
# print('1',line)
# line = f.readline()
# print('2',line)
# line = f.readline()
# print('3',line)
# line = f.readline()
# print('4',line)
# line = f.readline()
# print('5',line)
# line = f.readline()
# print('6',line)
# line = f.readline()
# print('7',line)
# line = f.readline()
# print('8',line)
# line = f.readline()
# print('9',line)
# line = f.readline()
# print('10',line)
# line = f.readline()
# print('11',line)
# line = f.readline()
# print('12',line)
# line = f.readline()
# print('13',line)
# line = f.readline()
# print('14',line)
# line = f.readline()
# print('15',line)
# line = f.readline()
# print('16',line)
# line = f.readline()
# print(type(line))  #<class 'str'>
# f.close()
#
# f = open('test.txt', 'r', encoding = 'utf-8')
# line = f.readline()
# print(line, end = '')
# while True:
#     line = f.readline()
#     if(line == ''):
#         break
#     print(line, end = '')
#
# f.close()


f = open('test.txt','r', encoding='utf-8')
while 1:
    try:
        line = f.readline()
        print(line, end="")
    except Exception:
        break
f.close()


# f=open('test.txt','r',encoding='utf-8')
# while True:
#     line = f.readline()
#     print(line, end='')
#     if line == '':
#         break
# f.close()

