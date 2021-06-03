#sting 관련 함수들
#Len() : 문자열의 Length
string = 'Python Programming'
n=len(string) #<18>
print(n)  #<2>

#count() : 문자열에서 찾고자 하는 문자(열)의 갯수
print(string.count('m'))  #<2>
print(string.count('o'))  #<2>
print(string.count('p'))  #<0>
print(string.count('P'))  #<2>

#find() : 특정 문자열이 존재 여부에 따라 위치인덱스나 -1 반환
print(string.find('ing'))  #<15>
print(string.find('ong'))  #<-1>

#index() :
print(string.index('ing'))  #<15>
print(string.index('ong'))  #오류