#append mode를 사용하여 파일 끝에 추가

f=open('text2.txt','a',encoding='utf-8')

# data= '\n\nPython programing'
# f.write(data)
# f.close()

# 읽기모드로 파일을 열어서 내용 출력

data='\nR Python programing\n'
f.write(data)

f = open('text2.txt','r',encoding='utf-8')
print(f.read())
f.close()

