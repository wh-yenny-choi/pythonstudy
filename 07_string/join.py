#join() : 특수문자를 넣어서 합친다

a = 'aa'
print(a.join('bbb'))  #<baabaab>   print(사이에 끼는 특수문자.join(원래 문자열))

b = '-'
print(b.join('1234'))  #<1-2-3-4>

numbers = ['10','20','30','40','50']
print(numbers)  #<['10', '20', '30', '40', '50']>
sep = ','
result = sep.join(numbers)  #떨어져 있는것을 하나의 문자열로 합침
print(result)               # <10,20,30,40,50>

data = ['1990','01','01']
sep = '-'
print(sep.join(data))  #<1990-01-01>


