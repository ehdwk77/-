def rep_char(c,n):
    print(c*n)


def show_message(name):
    msg1 = f' Hello {name},'
    msg2 = f' Welcome to Seoul.'
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-', nstr+1)
    print(msg1)
    print(msg2)
    rep_char('-', nstr+1)

name = input('Input his/her name: ')
show_message(name)
