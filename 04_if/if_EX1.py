#if~else 문 연습문제

# 등록된ID : flower
# 비밀번호 : 1234
# 아이디 입력 : abcd
# 비밀번호 입력 : 1234
# 로그인 실패!

# ID = 'flower'
# password = '1234'
# if_id = input('아이디 입력 : ')
# if_password = input('비밀번호 입력 : ')
# if (if_id == ID and if_password == password):
#     print('로그인 성공!')
# else:
#     print('로그인 실패!')

num1 = input('아이디 입력 : ')
num2 = input('비밀번호 입력 : ')
if (num1 == 'flower' and num2 == '1234'):
    print('로그인 성공!')
else:
    print('로그인 실패!')

ID = 'flower'
PW = '1234'

input_id = input('아이디 입력:')
input_pw = input('비밀번호 입력:')

if(input_id==ID and input_pw==PW):
    print('로그인 성공')
else:
    print('로그인 실패')
