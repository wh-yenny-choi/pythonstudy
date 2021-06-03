#continue문

x=0
while x<10:
    x+=1
    if x %2 == 0:
        continue
        #break
    print(x, end=' ')

print()

x=0
while x<10:
    x+=1
    if x %2 != 0:
        continue
        #break
    print(x, end=' ')

print()

#무한 반복(Loop&break)
print("반복시작")
while True:
    a = input("종료하려면 x입력 : ")
    if a=='x':
        print("반복종료")
        break

while True:
    print('반복시작')
    answer = input('종료하려면 x입력 : ')
    if answer == 'x':
        break
print('반복종료')