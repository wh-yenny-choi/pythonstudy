# 문자열의 구성요소 판단
# isalpha() : 문자여부 True False
# isdigit() :숫자인지 확인
# isspace() :공백
# isalpha() :알파벳(영어)
# isalnum() :알파벳(영어) 숫자
# isupper() : 대문자
# islower() : 소문자

text = '123457num'
print(text.isdigit())  #False
print(text.isalpha())  #False
print('    '.isspace())  #True
print(text.isalnum())  #True
print('Abc'.islower())  #False
print('AAA'.isupper())  #True


print('a'.isdigit())  #False
print('1'.isalpha())  #False
print('A'.islower())  #False
print('A'.isupper())  #True

# 연습문제. 문장을 입력하여 알파벳, 숫자, 스페이스, 그 외 문자의 개수를 계산 출력
# '나의 email 주소는 imlkm70@daum.net 입니다.
# isdigit() :숫자인지 확인
# isspace() :공백
# isalpha() :알파벳(영어)
# isalpha() : 문자여부 True False

alp,num,spac,other = 0,0,0,0
addr = input('이메일 주소를 입력하세요 : ')
print('나의 email 주소는',addr,end='입니다')
for i in addr:
    if i.isalpha():
        alp += 1
    elif i.isdigit():
        num += 1
    elif i == ' ':
        spac += 1
    else:
        other += 1
print(f'\n알파벳 {alp}, 숫자 {num}, 공백 {spac}, 그외{other}')







# dig = alp = space = other = 0
# a = input('이메일 주소를 입력하세요 : ')
# aI = print(f'나의 email 주소는 {a} 입니다.')
# dig = alp = space = other = 0
# for i in a:
#     if i.isalpha():
#         alp += 1
#     elif i.isdigit():
#         dig += 1
#     elif i == ' ':
#         space += 1
#     else:
#         other += 1
#
# print(f'알파벳 개수: {alp},숫자 개수: {dig}, 공백: {space}, 그 외: {other}')
#
# text = input('문장을 입력하세요 : ')
# cnt_a, cnt_d, cnt_s, cnt_etc = 0, 0, 0, 0
# for i in text:
#     if i.isdigit():
#         cnt_d += 1
#     elif i.isalpha():
#         cnt_a += 1
#     elif i == ' ':
#         cnt_s += 1
#     else:
#         cnt_etc += 1
#
# print(f'알파벳 개수 : {cnt_a}')
# print(f'숫자 개수 : {cnt_d}')
# print(f'공백 개수 : {cnt_s}')
# print(f'그 외 개수 : {cnt_etc}')

#
# text = input('문장 입력 : ')
# alpha = num = sp = r = 0
# for i in text:
#     if i.isalpha():
#         alpha += 1
#     elif i.isdigit():
#         num += 1
#     elif i.isspace():
#         sp += 1
#     else:
#         r += 1
# print(f'문자의 개수 : {alpha}, 숫자의 개수 : {num}, 공백의 개수 : {sp}, 그외문자 개수 : {r}')

'''
alphas = digits = space = others = 0
string = input('문장을 입력하세요 : ')
for c in string:
    if c.isalpha():
        alphas += 1
    elif c.isdigit():
        digits += 1
    elif c.isspace():
        space += 1
    else:
        others += 1
print('문자 : %d개' %alphas)
print('숫자 : %d개' %digits)
print('공백 : %d개' %space)
print('그외 : %d개' %others)


addr = input('email주소를 입력하세요 : ')
print('나의 email 주소는',addr, end='입니다')

for c in string:
    if c.isalpha():
        alphas += 1
    elif c.isdigit():
        digits += 1
    elif c.isspace():
        space += 1
    else:
        others += 1
print('문자 : %d개' %alphas)
print('숫자 : %d개' %digits)
print('공백 : %d개' %space)
print('그외 : %d개' %others)
'''