#문자열의 기본 형식과 이해

crawling = 'Data crawling is fun'
parsing = 'Data parsing is also fun'

print(crawling)   #<Data crawling is fun>
print(parsing)    #<Data parsing is also fun>

print(type(crawling))  #<<class 'str'>>
print(type(parsing))   #<<class 'str'>>

pi = 3.1415
r = 10
result = '반지름' + str(pi) + '인 원의 넓이는 '+ str(pi*r*r)  #str() 문자열 연결에 이용
print(result)   #<반지름3.1415인 원의 넓이는 314.15000000000003>

print('hello'*3)   #<hellohellohello>

#slicing : 문자열의 일부분을 추출
crawling = 'Data crawling is fun'

print(crawling[0])  #<D>
print(crawling[-1])  #<n>
print(crawling[1:6])  #<ata c>
print(crawling[:-1])  #<Data crawling is fu>
print(crawling[-1:])  #마지막 문자 <n>
print(crawling[:])   #문자열 전체 <Data crawling is fun>
print(crawling[0:10])  #<Data crawl>