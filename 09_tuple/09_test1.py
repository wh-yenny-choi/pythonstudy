#tuple 연습문제
# tt=((1,2,3),(4,5,6),(7,8,9))

#출력결과
#1 2 3
#4 5 6
#7 8 9

# for i in tt:
#     for j in i:
#         print(j,end=' ')
#     print()





a = [[1,2,3],[4,5,6],[7,8,9]]
for i in a:
    for j in i:
        print(int(j+i*3),end=' ')
    print()
