class CountFromBy:
    def __init__(self, v:int=0, i:int=1) -> None: #атрибут self сохраняет значение переменной после завершения функции. это обязательный параметр при дальнейшем написании кода
        #при добавлении =0 или =1 в определении атрибута устанавливает значение по умолчанию и позволит избежать ошибок при вызове класса: g = CountFromBy()
        self.val = v
        self.incr = i
    def increase(self) -> None:
        self.val += self.incr
    def __repr__(self) -> str: #при определении любого метода важно помнить, что интерпритатор всегда передает значение для первого параметра (self)
        return str(self.val) # получает значение val, превращает в строку и возвращает значение

g = CountFromBy(100, 10)
print(g.val) #получить значение можем объединив имя объекта с именем атрибута
print(g.incr)
print('======================')
g.increase()
print(g.val)
print(g) #выводит <__main__.CountFromBy object at 0x0126DC10>
print('======================')
print('### объясняем почему такое возвращается <__main__.CountFromBy object at 0x0126DC10>')
j = CountFromBy(100, 10)
print('1.', j, sep= ' ') #выводим j
print('2.', type(j), sep= ' ') #type возвращает информацию о классе, из которого был создан объект
print('3.', id(j), sep= ' ') #id возвращает адрес объекта в памяти
print('4.', hex(id(j)), sep= ' ') #16-чное представление адреса
print('======================')
k = CountFromBy()   #пример использования значений по умолчанию в функции __init__
print(k)
k.increase()
print(k)

""" расскоментировать полностью для примера использования функции
def soundbite(from_outside):
    insider = 'James'
    outsider = from_outside
    print(from_outside, insider, outsider)

name = 'Bond'

soundbite(name)

print(name)

print(insider) #пример того, что переменная только инициализируется в функции и за ее пределами не работает
"""