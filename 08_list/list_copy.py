# 리스트의 복사

# 얕은 복사 : 주소만 복사
scores = [65,70,90,89,78]
value = scores
print('scores :',scores)  #5개 값을 가지고 있는 list 출력  scores : [65, 70, 90, 89, 78]
print('value :',value)  #value : [65, 70, 90, 89, 78]

scores[3]=98
print('scores 값을 변경 :',scores)  #scores 값을 변경 : [65, 70, 90, 98, 78]
print('value :',value)  #value : [65, 70, 90, 98, 78]

value[0]=100
print('scores :',scores)  #scores : [100, 70, 90, 98, 78]
print('value :',value)    #value : [100, 70, 90, 98, 78]

# 깊은 복사 (deep copy) : 리스트 전체 복사
value2 = scores.copy()
print('value2',value2)  #value2 [100, 70, 90, 98, 78]
scores[0] = 50
print('scores :',scores)  #scores : [50, 70, 90, 98, 78]
print('value :',value)   #value : [50, 70, 90, 98, 78]
print('value2',value2)   #value2 [100, 70, 90, 98, 78]

# 깊은 복사 (deep copy) : 리스트 전체 복사, .copy() list() deepcopy()
value3 = list(scores)
print('value3',value3)  #value3 [50, 70, 90, 98, 78]
print('scores :',scores)  #scores : [50, 70, 90, 98, 78]
scores[0] = 150
print('scores :',scores)  #scores : [150, 70, 90, 98, 78]
print('value3',value3)  #value3 [50, 70, 90, 98, 78]

import copy
value4 = copy.deepcopy(scores)
scores[2]=300
print('scores :',scores)  #scores : [150, 70, 300, 98, 78]
print('value4',value4)  #[150, 70, 90, 98, 78]