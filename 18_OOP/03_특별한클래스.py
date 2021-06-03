#__str__(selr),__repr__(self),__del__(self)
# __add__(self),__le__(self),__lt__(self),__gt__(self),__ge__(self)
#__eq__(self),__ne__(self)

class Line:
    length = 0
    def __init__(self,length=0):
        self.length = length
        print('%s 길이의 선이 생성' %self.length)

    # def __del__(self):
    #     print('%s 길이의 선이 소멸' %self.length)

    def __repr__(self):
        print('선의 길이 : ' +str(self.length))

    def __add__(self, other):
        return self.length + other.length

    def __eq__(self, other):
        return self.length == other.length

    def __ne__(self,other):
        return self.length != other.length

    def __lt__(self, other):
        return self.length < other.length

line1=Line(15)
line2=Line(10)
# print(line1)
print('두 선의 길이의 합 : ',line1+line2)
# if line1 != line2:
#     print('같지 않아요.')
if line1 < line2:
    print('선 2가 더 크네요.')
# if line1 > line2:
#     print('선 1이 더 크네요.')
elif line1 == line2:
    print('길이가 달라요.')
else:
    print('몰라욧')





