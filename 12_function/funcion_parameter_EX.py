# def order():
#     a = int(input("상품가격 입력 : "))
#     b = int(input("주문수량 입력 : "))
#     print('------------------')
#     c = a*b
#     return a,b,c
#
# c = order()
# print("상품가격 : %d원\n주문수량 : %d개\n주문액 : %d원" %(c[0],c[1],c[2]))
# 상품가격 price 주문수량 qty 주문액 amount 할인액discount 지불액 total
#price * qty
#price, qty =0

def order(price,qty):
    amount = price * qty
    if amount >= 100000:
        discount = int(amount *0.1)
    elif amount >= 50000:
        discount = int(amount * 0.05)
    else:
        discount = 0
    total = int(amount-discount)
    return amount,discount,total

price = int(input('상품 가격 입력 : '))
qty=int(input('주문 수량 입력 : '))
orders=order(price,qty)
print('-'*20)
print("주문액 : {}원" .format(orders[0]))
print("할인액 : {}개" .format(orders[1]))
print("지불액 : {}원" .format(orders[2]))


# def order(price, qty):
#     amount = price * qty
#     if(amount >= 100000):
#         discount = int(amount * 0.1)
#     elif(amount < 100000 and amount >= 50000):
#         discount = int(amount * 0.05)
#     else:
#         discount = 0
#     total = amount - discount
#     return amount, discount, total
#
# price = int(input('상품 가격 입력 : '))
# qty = int(input('주문 수량 입력 : '))
# result = order(price, qty)
# print('주문액 : {0}원\n할인액 : {1}원\n지불액 : {2}원'.format(result[0], result[1], result[2]))


# def order():
#     price = int(input('상품가격 : '))
#     qty = int(input('주문수량 : '))
#     amount = int(price * qty)
#     if amount >= 100000:
#         discount = amount*0.1
#     elif amount >= 50000:
#         discount = amount*0.05
#     else:
#         discount = amount
#     total = int(amount-discount)
#
#
#
#     print('상품가격 : ',price,'원')
#     print('주문수량 : ',qty,'개')
#     print('='*20)
#     print('주문액 : ',amount,'원')
#     print('할인액 : ',discount,'원')
#     print('지불액 : ',total,'원')
#
#     return price,qty,amount,discount,total
#
# order()

