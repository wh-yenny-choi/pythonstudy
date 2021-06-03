# split() 연습문제  a.split('나누는기준')
# 생일입력(연/월/일) : 1998/9/28
# 당신은 1998년에 태어나셨군요
# 생일은 9월 20일 이네요

bday = input('생일입력(연/월/일) : ')
bday_split = bday.split('/')
print('당신은 {}년에 태어나셨군요.'.format(bday_split[0]))
print('생일은 {}월 {}일 이네요.'.format(bday_split[1],bday_split[2]))

num = input('생일 입력(연/월/일) : ' )
birth = num.split('/')
year = birth[0]
month = birth[1]
day = birth[2]
print('당신은 %s년에 태어나셨군요' %year)
print('생일은 %s월 %s일 이네요' %(month,day))

birthday = input('생일 입력(연/월/일) : ')
birth_split = birthday.split('/')
print('당신은 %s년에 태어나셨군요' %birth_split[0])
print('생일은 %s월 %s일 이네요' %(birth_split[1],birth_split[2]))


# 주어진 데이터에서 점수만 추출하여 숫자화하고 총점과 평균을 구하시오
# data = "{a1:30},{a2:50},{a3:20},{a4:70},{a5:40}"
# split을 이용하여 분리

data = "{a1:30},{a2:50},{a3:20},{a4:70},{a5:40}"
split_data = data.split(',')
score=n=total=0
for d in split_data:
    item = d.split(':')  #d={a1:30} => ['{a1,30}']    :기준으로 분리
    item2 = item[1].split('}') # '30}' => ['30']
    score = int(item2[0])
    #score = int(item[1].split('}')[0])
    print(score)
    total += score
    n += 1  #n += 1생략시 > print( '' %(total, total/5))

print('총점 : %d, 평균 : %f' %(total, total/n))


data = "{a1:30},{a2:50},{a3:20},{a4:70},{a5:40}"
split_data = data.split(',')
score=n=total=0
for d in split_data:
    item = d.split(':')  #d={a1:30} => ['{a1,30}']    :기준으로 분리
    score = int(item[1].split('}')[0])
    print(score)
    total += score
    n += 1  #n += 1생략시 > print( '' %(total, total/5))

print('총점 : %d, 평균 : %f' %(total, total/n))


data = "{a1:30},{a2:50},{a3:20},{a4:70},{a5:40}"
total = score = avg = 0
data_split=data.split(',')   #['{a1:30}', '{a2:50}', '{a3:20}', '{a4:70}', '{a5:40}']
for d in data_split:
    item = d.split(':')   #['{a1', '30}']
    item2 = item[1].split('}')  #['30', '']
    score = int(item2[0])
    print(score)
    total += score
    avg = (total/5)
print('총점 : %d, 평균 : %.1f' %(total,avg))