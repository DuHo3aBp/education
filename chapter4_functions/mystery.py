#разбираемся с симантикой вызова по значению
def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)

#демонстрация симантики вызова по ссылке
def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)