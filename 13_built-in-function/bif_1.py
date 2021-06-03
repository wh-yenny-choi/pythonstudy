#any(), all()
print(all([0,1,2,3]))
print(any([0,1,0]))
print(any([0,'',0]))
print(any([0,[],0]))

#ascill code 아스키 코드 value : chr(x)
print(chr(65)) #A
print(chr(97)) #a

#ord(c)
print(ord('a'))   #97
print(ord('\n'))  #10
print(ord(' '))   #32
print(ord('\t'))  #9
print(ord('\\'))  #92

#divmod(a,b) : 튜플형태 리턴, a>몫 반환 b>나머지 반환
print(divmod(7,3)) #(2,1)

#eval(expression) : 입력받은 값 형태로 반환
print(eval('13.5'))   #<13.5>
print(type(eval('13.5')))  #<<class 'float'>>
print(eval('3+5'))   #<8>
print(type(eval('3+5')))  #<class 'int'>


#help() : 설명
help(print)
help(map)
help(sum)