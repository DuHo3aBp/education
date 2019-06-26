person1 = ['Ford prefect','Male','Researcher','Betelges seven']
print(person1)

person2 = ['Name','Ford prefect','Gender','Male','Ocupation','Researcher',
'Home Planet','Betelges seven']
print(person2)

#определяем словарь person3 с ключем/значением
person3 = { 'Name': 'Ford prefect',
            'Gender': 'Male',
            'Ocupation': 'Researcher',
            'Home Planet': 'Betelges seven' }
print(person3)
#выводим на экран значение ключа Ocupation
print(person3['Ocupation'])

#добавление новой пары ключ/значение в словарь person3 и выведем весь словарь на экран
person3['Age'] = 33
print(person3)
