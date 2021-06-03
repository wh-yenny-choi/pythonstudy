#replace()

text = 'Java Programming'
#print(text.replace('Java','Python'))
text = text.replace('Java','Python')  #text.replace('원래문자' , '바꿀문자')
print(text)                           # <Python Programming>

#대문자/소문자 변환
#upper() : 대문자로 변경
#Lower() : 소문자로 변경
#capitalize() : 첫 문자를 대문자로 변경
#title() : 각 단어의 첫글자를 대문자로 변경
#swapcase() : 대문자는 소문자로, 소문자는 대문자로 변경

text = 'java programming is Fun'
print(text.upper())   #<JAVA PROGRAMMING IS FUN>
print(text.lower())   #<java programming is fun>
print(text.title())   #<Java Programming Is Fun>
print(text.capitalize())  #<Java programming is fun>
print(text.swapcase())    #<JAVA PROGRAMMING IS fUN>

#공백문자 제거 strip(), Lstrip(), Rstrip()
text = '   java programming is Fun   '
print(text + '---')            #<   java programming is Fun   --->
print(text.strip())            #<java programming is Fun>
print(text.lstrip())           #<java programming is Fun   >
print(text.rstrip() + '---')   #<   java programming is Fun--->

