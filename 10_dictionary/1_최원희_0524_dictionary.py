# #1. 딕셔너리 이용, 총점, 평균 계산 출력

students = [
   {"name" : "홍길동", "korean" : 87, "math" : 98, "english" : 88, "science" : 95},
   {"name" : "이몽룡", "korean" : 92, "math" : 98, "english" : 96, "science" : 98},
   {"name" : "성춘향", "korean" : 76, "math" : 96, "english" : 94, "science" : 90},
   {"name" : "변학도", "korean" : 98, "math" : 92, "english" : 96, "science" : 92},
   {"name" : "박지성", "korean" : 95, "math" : 98, "english" : 98, "science" : 98},
   {"name" : "류현진", "korean" : 64, "math" : 88, "english" : 92, "science" : 92}]

print('%s %8s %8s' %("이름","총점","평균"))
for d_students in students:
   sum = d_students["korean"] + d_students["math"] + d_students["english"] + d_students["science"]
   avg = sum/4
   print("%s %8d %8.1f" %(d_students["name"],sum,avg))

#5.영단어
# word=''
# endDict= dict()
# #endDict['cat']='고양이'
# while True:
#     word = input("영어 단어 등록 (종료는 quit) : ")
#     if word == 'quit':
#         break
#     elif endDict.get(word):
#         print('이미 등록된 단어 입니다.')
#         continue
#     else:
#         mean = input('{}의 뜻입력 (종료는 quit) : '.format(word))
#         endDict[word] = mean
#
# while True:
#     word2 = input('검색할 단어 입력 (종료는 quit) : ')
#     if word2 == 'quit':
#         print()
#         print("종료합니다.")
#         break
#     elif word2 not in endDict:
#         print('{}는 사전에 없는 단어 입니다.'.format(word2))
#         continue
#     else:
#         print('%s 뜻은 %s입니다.' %(word,endDict[word2]))

endDict= dict()
#endDict['cat']='고양이'
while True:
    word = input("영어 단어 등록 (종료는 quit) : ")
    if word == 'quit':
        break
    elif endDict.get(word):
        print('이미 등록된 단어 입니다.')
    else:
        mean = input("{}의 뜻입력 (종료는 quit) : ".format(word))
        endDict[word] = mean
while True:
    word2 = input('검색할 단어 입력 (종료는 quit) : ')
    if word2 == 'quit':
        print("종료합니다.")
        break
    elif word2 not in endDict:
        print('{}는 사전에 없는 단어 입니다.'.format(word2))
    else:
        print('{}의 뜻은 {}입니다.'.format(word2, endDict[word2]))

word=''
endDict={}
#endDict['cat']='고양이'
while True:
    word = input("영어 단어 등록 (종료는 quit) : ")
    if word == 'quit':
        break
    elif endDict.get(word):
        print('이미 등록된 단어 입니다.')
        continue
    mean = input("{}의 뜻입력 (종료는 quit) : ".format(word))
    if mean =='quit':
        break
    endDict[word] = mean
while True:
    word2 = input('검색할 단어 입력 (종료는 quit) : ')
    if word2 == 'quit':
        print()
        print("종료합니다.")
        break
    elif word2 not in endDict:
        print('{}는 사전에 없는 단어 입니다.'.format(word2))
        continue
    elif word2 in endDict:
        print('{}의 뜻은 {}입니다.'.format(word2,mean))