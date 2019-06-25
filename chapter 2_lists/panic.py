phrase = "Don't panic!"
plist = list(phrase)                        #трансформируем phrase в список и присваиваем переменной plist
print(phrase)
print(plist)

#Преобразуем "Don't panic!"" в "on tap"
for i in range(4):                          #этот цикл извлекает последние 4 объекта, 
    plist.pop()                             #удаляя nic!
plist.pop(0)                                #извлекаем первую букву D, индекс 0
plist.remove("'")                           #находим и удаляем апостроф
plist.extend([plist.pop(5),plist.pop(4)])     #меняем местами 2 объекта в конце списка, первую а, вторую р. extend в таком порядке и вставляет обратно
plist.insert(2,plist.pop(3))                #извлекаем пробел (индекс 3) и вставляем обратно в список (индекс 2)

new_phrase = ''.join(plist)                 #превразаем plist обратно в строку
print(plist)
print(new_phrase)
