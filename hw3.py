discount_rate = int(input('할인율은?'))

def get_fixed_price(name) :
    price = int(input(name + '상품의 할인된 가격은?'))
    
    fixed_price = price/(1-discount_rate/100)
    print(name , '상품의 정가는', int(fixed_price),'원')

get_fixed_price('A')
get_fixed_price('B')

