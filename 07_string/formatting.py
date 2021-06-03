#formatting: %d %f %s %c
# %3d %5.2f

alphas=20; digit=30
height = 179.33
string = 'python'
tt='문자: %d개' %alphas
print(tt)
print('문자 : %d개' %alphas)
print('문자 : ' , format(alphas,'d') , '개')
print('문자 : {0}개'.format(alphas))
print('문자 : {0}개, 숫자 : {1}개'.format(alphas, digit))
print('문자 : {alp}개, 숫자 : {dig}개'.format(alp=alphas, dig=digit))

print('키는 {0:5.1f}'.format(height))  #<키는 179.3>

print('{0}'.format(string))
print('{0:<10}'.format(string))   #왼쪽 정렬 <python    >
print('{0:>10}'.format(string))   #오른쪽 정렬 <    python>
print('{0:^10}'.format(string))   #가운데 정렬 <  python  >
print('{0:-^10}'.format(string))  #<--python-->
print(string.ljust(10))  #왼쪽 정렬
print(string.rjust(10))  #오른쪽 정렬
print(string.center(10)) #가운데 정렬


#날짜. 시간 출력 포맷
from datetime import date, datetime, timedelta #날짜 계산

today = date.today()
print(today. year)   #시스템 당일 년
print(today. month)  #시스템 당일 월
print(today. day)    #시스템 당일 일

cur_time = datetime.now()
print(cur_time)    #<2021-05-24 03:19:04.197972>
cur_time = datetime.now().time()
print(cur_time)    #<03:19:04.197972>
print(cur_time.hour)
print(cur_time.minute)
print(cur_time.second)
print(cur_time.microsecond)

cur_time = datetime.now()
print(today + timedelta(days =- 1)) #1일 전
print(today + timedelta(days = 7))  #7일 후
print(cur_time + timedelta(days = 1, hours = 2))  #2021-05-25 05:19:04.197972

print(today.strftime('%Y-%m-%d %H : %M %S'))      #2021-05-24 00 : 00 00