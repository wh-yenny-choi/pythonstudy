print('1번')
print('3')
mylist = ['apple' ,'banana', 'grape']
result = list(enumerate(mylist))
print(result)
print('\n2번')
print('4')
cat_song = "my cat has blue eyes, my cat is cute"
print({i:j for j,i in enumerate(cat_song.split())})
#키값은 가장 최근에 업데이트된 값을 가짐 따라서 my: 0 > 5(최종) cat: 1 > 6
print('\n3번')
print('예측')
print('orange&pink&brown&black&white')
print('결과')
colors = ['orange', 'pink', 'brown', 'black', 'white']
result = '&'.join(colors)
print(result)

print('\n4번')
print('예측')
print("{'students': 0, 'superuser': 1, 'professor': 2, 'employee': 3}")
print('결과')
user_dict = {}
user_list = ["students","superuser", "professor", "employee"]
for value_1, value_2 in enumerate(user_list):
    user_dict[value_2] = value_1
print(user_dict)

print('\n5번')
print('예측 ')
print('0 2,4,6,8'
      '\n '
      "\n'zero','one','two','three'"
      '\ncs50')
print('결과 ')
print('0, 2, 4, 6, 8]'
      "\n['zero one ','three']"
      "\n['zero', 'one', 'two', 'three']"
      '\ncs50')

print('\n6번')
print('예측')
print(['Cat','Panda','Owl'])
print('결과')
animal = ['Fox', 'Dog', 'Cat', 'Monkey', 'Horse', 'Panda', 'Owl']
print([ani for ani in animal if 'o' not in ani])

print('\n7번')
print('예측')
print('GilUniversity')
print('결과')
name = "Hanbit University"
student = ["Hong", "Gil", "Dong"]
split_name = name.split()   #HongGilDong
join_student = ''.join(student)
print(join_student[-4:] + split_name[1])  #뒤에서 4번째부터 마지막까지 Dong

print('\n8번')
print('예측')
print('20')
print('결과')
kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]
print(midterm_score[0][2])

print('\n9번')
print('예측')
print('2')
print('결과')
print('[[12, 3], [15, 3]]')

print('\n10번')
print('예측')
print('yellow')
print('결과')
week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
list_data = [week, rainbow]
print(list_data[1][2])

print('\n11번')
print('예측')
print('score:72')
print('결과')
kor_score = [30, 79, 20, 100, 80]
math_score = [43, 59, 0, 30, 90]
eng_score = [49, 72, 48, 67, 15]
midterm_score = [kor_score, math_score, eng_score]
print ("score:",midterm_score[2][1])

print('\n12번')
print('예측')
print("['a','2','error']")
print('결과')
alist = ["a", "b", "c"]
blist = ["1", "2", "3"]
abcd= ['error']
for a, b in enumerate(zip(alist, blist)):  #zip : 같은위치끼리 묶음
    try:
        abcd.append(b[a])
    except IndexError:
        abcd.append("error")
print(abcd)

print('\n13번')
for a,b in zip(alist,blist):
    print(a,b)

print('\n14번')
print('예측')
print('')
print('결과')
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h"]
nums = [i for i in range(20)]
answer = [alpha+str(num)
          for alpha in alphabet
          for num in nums
          if num%2==0]
print(answer)  #0~19까지 2의 배수는 10개 + 알파벳 8개 
# ['a0', 'a2', 'a4', 'a6', 'a8', 'a10', 'a12', 'a14', 'a16', 'a18',
#  'b0', 'b2', 'b4', 'b6', 'b8', 'b10', 'b12', 'b14', 'b16', 'b18',
#  'c0', 'c2', 'c4', 'c6', 'c8', 'c10', 'c12', 'c14', 'c16', 'c18',
#  'd0', 'd2', 'd4', 'd6', 'd8', 'd10', 'd12', 'd14', 'd16', 'd18',
#  'e0', 'e2', 'e4', 'e6', 'e8', 'e10', 'e12', 'e14', 'e16', 'e18',
#  'f0', 'f2', 'f4', 'f6', 'f8', 'f10', 'f12', 'f14', 'f16', 'f18',
#  'g0', 'g2', 'g4', 'g6', 'g8', 'g10', 'g12', 'g14', 'g16', 'g18',
#  'h0', 'h2', 'h4', 'h6', 'h8', 'h10', 'h12', 'h14', 'h16', 'h18']
print(len(answer))