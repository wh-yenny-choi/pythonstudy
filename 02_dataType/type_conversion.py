
#타입 변환
#str() 함수 : 숫자를 문자열로 변환
#print('나는 현재 나이가',27,'살입니다')
#print('나는 현재 나이가 '+str(23)+'살입니다')
# 23(숫자)는 +로 연결 X +는 문자열 연결

# int() : 정수형식의 문자열을 정수로 변환
num = input ('숫자를 입력하세요 :') #키보드로 입력받은 자료를 num변수에 할당
print(type(num))
print (num+100)
print(int(num) + 100) #num : 문자열 100 : 숫자열 >> 오류발생 >> int 함수 사용

print(int('123', 8)) #8진수 0o123     2진수:1010011
print(int('123', 16))
print(int('1111', 2))

#float(문자열) : 문자열을 실수로 변환
print(float(num)+100)


#키보드로부터 두 개의 정수를 입력받고, 두 수의 합과 평균을 구하시오
num1 = input('첫번째 숫자 :')
num2 = input('두번째 숫자 :')
sum = int(num1)+int(num2)
avg = sum/2
print('총합 = %d, 평균 = %.2f' %(sum,avg))
print('두 수의 합은 {0}, 평균은 {1}' .format(sum, avg))

num1 = input("첫번째 숫자 입력 : ")
num2 = input("두번째 숫자 입력 : ")


total = int(num1) + int(num2)
avg = total / 2

print("총합은 %d이고, 평균은 %.2f입니다." %(total, avg))

num1 , num2 = input('num1 : '), input('num2 : ')

total = int(num1) + int(num2)
avg = total/2

print('total : %d, avg : %.2f' % (total,avg))




