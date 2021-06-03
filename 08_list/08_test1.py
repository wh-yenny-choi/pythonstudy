
total = avg =0
data = "{a1:30},{a2:50},{a3:20},{a4:70},{a5:40}"
dataS = data.split(',')
for i in dataS:
    id, score = i.split(':')
    score = int(score.split('}')[0])
    print(score)
    total += score
avg = total/5
print(f'총합 : {total} \n평균 : {avg}')


data = "{a1:30},{a2:50},{a3:20},{a4:70},{a5:40}"
split_data = data.split(',')
n=total=0
for d in split_data:
    id,score = d.split(':')  #d={a1:30} => ['{a1,30}']   # :기준으로 분리
    # print(id,',',score)
    # print(type(split_data))
    score = int(score.split('}')[0]) # '30}' => ['30'] => 30
#     score = int(item2[0])
#     score = int(item[1].split('}')[0])
    print(score)
    # print(type(score))
    total += score
    n += 1  #n += 1생략시 > print( '' %(total, total/5))

print('총점 : %d, 평균 : %f' %(total, total/n))
