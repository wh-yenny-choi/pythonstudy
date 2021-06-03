#컴퓨터와 게임하는 경우
#1~100 사이에 랜덤 숫자로 결정

# from random import randint
# num1 = randint(1,100)
# num2 = randint(1,100)
# print('computer : {} vs human : {}' .format(num1,num2))
# if num1>num2:
#     print('You Lose :(')
# else:
#     print('You Win! :)')



from random import randint
compNum = randint(1,100)
myNum = randint(1,100)
print('com : %d vs my : %d' %(compNum, myNum))
if(myNum > compNum):
    print('You Win!')
else:
    print('You Lose')