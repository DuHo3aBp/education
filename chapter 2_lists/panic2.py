phrase = "Don't panic!"
plist = list(phrase)                        #трансформируем phrase в список и присваиваем переменной plist
print(phrase)
print(plist)

#Преобразуем "Don't panic!"" в "on tap" с помощью среза списка
new_phrase = ''.join(plist[1:3]+plist[5:6]+plist[4:5]+plist[-5:-7:-1])

print(plist)
print(new_phrase)
