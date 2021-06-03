#함수명 : order()
#상품가격, 주문수량 입력받아 주문액 계산 반환

def order():
    a = int(input("상품가격 입력 : "))
    b = int(input("주문수량 입력 : "))
    print('------------------')
    c = a*b
    return a,b,c

c = order()
print("상품가격 : %d원\n주문수량 : %d개\n주문액 : %d원" %(c[0],c[1],c[2]))