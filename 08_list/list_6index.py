# 리스트의 요소 찾기 : index()

a = [3,6,0,-4]
  # [0,1,2, 3]
b = a.index(6)
print(b)   # 해당 index의 위치 반환  <1>
# b = a.index(10)  #오류
# print(b)
b = a.index(-4)
print(b)  #<3>

# in / not in
if 2 in a:
    print('Exist')
else:
    print('Not exist!')
#<Not exist!>

if 2 not in a:
    print('Exist')
else:
    print('Not exist!')
#<Exist>