crawling = 'Data crawling is fun'

print(crawling.find('i'))  # find > 위치찾기 count > 개수구하기 <10>
print(crawling.rfind('i')) #<14>
print(crawling.find('i',1,9)) #<-1>

print('--------------')
print(crawling.index('i'))  #<10>
print(crawling.rindex('i'))  #<14>
#print(crawling.index('i',1,9)) #오류


#split() : 지정된 문자로 문자열을 분할함, 리스트 형식으로

token = crawling.split()
print(token)  #<['Data', 'crawling', 'is', 'fun']>

names = 'Lee,Kim,Choi,Park'
nameL = names.split(',') # , 로 문자열 분할 ['Lee','Kim','Choi','Kang']

for n in nameL:
    print(n)     #<Lee\nKim\nChoi\nPark>

for i in range(len(nameL)):
    print(nameL[i])  #<Lee\nKim\nChoi\nPark>

for c in crawling:  #문자열 요소 하나씩 출력
    print(c)