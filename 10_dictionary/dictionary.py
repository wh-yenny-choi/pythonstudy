# 딕셔너리 dictionary
# 키와 값으로 구성 {키1:값1, 키2:값2,...} 중괄호 처리

# 딕셔너리 만들기
d = {} # 빈 딕셔너리
d ={1:'a', 2:'b', 3:'c'} # item(키:값)구분은 콤마(,)로
print(d)  # <{1: 'a', 2: 'b', 3: 'c'}>
print(type(d))  # <<class 'dict'>>

# 딕셔너리 요소 접근
print(d[1])  # <a>

d2={'name':'Lee','tel':'010-1111-1111'}
print(d2['name'])   #<Lee>

#딕셔너리에 요소 추가
d[4]='f'
print(d)  #<{1: 'a', 2: 'b', 3: 'c', 4: 'f'}>

d2['address']='서울시 강남구'
print(d2)  #<{'name': 'Lee', 'tel': '010-1111-1111', 'address': '서울시 강남구'}>

d3={'name':'daum',
    'url':'www.daum.net',
    'userid':'dm',
    'pw':1234}

#keys(), values(), items()
print(d3.keys())  #<dict_keys(['name', 'url', 'userid', 'pw'])>
d3_Key = d3.keys()
print(type(d3_Key))  #<<class 'dict_keys'>>
print(d3_Key)  #<dict_keys(['name', 'url', 'userid', 'pw'])>
print(list(d3_Key))  #요소 추출하려면 우선 리스트 형태로 변환 <['name', 'url', 'userid', 'pw']>
print(list(d3_Key)[1]) #<url>

d3_values = d3.values()
print(list(d3_values))  #<['daum', 'www.daum.net', 'dm', 1234]>

d3_items = d3.items()
print(d3_items) #키,값을 튜플형태로 <dict_items([('name', 'daum'), ('url', 'www.daum.net'), ('userid', 'dm'), ('pw', 1234)])>
print(list(d3_items)) #리스트 형태로 변환  <[('name', 'daum'), ('url', 'www.daum.net'), ('userid', 'dm'), ('pw', 1234)]>
print(list(d3_items)[0])  #변환 후 추출 <('name', 'daum')>

#for문 이용
for key in d3.keys():   #<name \n url \n userid \n pw>
    print(key)

for value in d3.values():    #<daum \n www.daum.net \n dm \n 1234>
    print(value)

for item in d3.items():   #<('name', 'daum') \n ('url', 'www.daum.net') \n ('userid', 'dm') \n ('pw', 1234)>
    print(item)

print(d3['name']) #<daum>
#print(d3['add']) #KeyError: 'add'
print(d3.get('name')) #<daum>
print(d3.get('add'))  #<None>
print(d3.get('add','not exist'))  #<not exist>

k='link'
if d3.get(k) is None:
    print(k+'에 대한 데이터가 없음.')  #<link에 대한 데이터가 없음.>

#in/not in
print('link'in d3) #왼쪽의 요소가 있는지 확인  <False>
print('link'not in d3) #<True>
print('name'in d3) #<True>

# print(dir(d3))
# [['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
#   '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__',
#   '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__',
#   '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
#   'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']]

print(d3.popitem())  #<('pw', 1234)>
print(d3)  #<{'name': 'daum', 'url': 'www.daum.net', 'userid': 'dm'}>

#zip()
#컴프리헨션
a={x for x in 'abracadabra' if x not in 'abc'}
print(a)   #<{'d', 'r'}>

y= [x**2 for x in (2,3,4)]  # [4, 9, 16]
print(y)

z = {x : x**2 for x in (2,3,4)} # {2: 4, 3: 9, 4: 16}
print(z)

for key,val in d3.items():
    print('%s:%s'%(key,val))
    #<name:daum
    # url:www.daum.net
    # userid:dm>

students = {1:[80,86,60],
            2:[87,90,30],
            3:[]}

endDict={}
endDict['dog']='개'
endDict['cat']='고양이'