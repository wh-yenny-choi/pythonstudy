#in
#문자열 안의 in

string = 'Python is programming'

print('Python' in string) #True
print('python' in string) #False
print("wonhee" in string)

if 'Python' in string:  #in 기준 왼쪽이 찾는것 오른쪽이 원문
    print('있습니다.')
else:
    print('없습니다.')

#
names = ['홍','변','성','이']
name = input('input name : ')
if name in names:
    print('yes')
else:
    print('no')

names = ['홍','변','성','이']
while True:
    name = input('input name : ')
    if name in names:
        print("Yes")
        break
    else:
        print("No")



'''
    +---+---+---+---+---+---+
    | P | y | t | h | o | n |
    +---+---+---+---+---+---+
    0   1   2   3   4   5   6
   -6 - 5 - 4 - 3 - 2 - 1
'''