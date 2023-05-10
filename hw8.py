def buy(dic):
    print('[구입]')
    item = input('상품명? ')
    num = input('수량은? ')
    if item == '':
        return False
    else :
        dic[item] = num
        print(f'장바구니에 {item} {num}개가 담겼습니다.')
        print()

def show(dic):
    print()
    print(f'>>장바구니 보기 : {dic}')

def find(dic):
    print()
    print('[검색]')
    item = input('장바구니에서 확인하고자 하는 상품은?')
    if item in dic :
        print(f'{item}은(는) {dic[item]}개 담겨 있습니다.')
    else :
        print(f'장바구니에 {item}은(는) 없습니다.')

shopping_bag = {}
while True :
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)