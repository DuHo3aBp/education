import pprint

#создание списка в списке и красивый вывож на экран
people = {}
people['Ford'] = {  'Name': 'Ford prefect',
                    'Gender': 'Male',
                    'Ocupation': 'Researcher',
                    'Home Planet': 'Betelges seven' }
people['Buck'] = {  'Name': 'Buck prefect',
                    'Gender': 'Male',
                    'Ocupation': 'Researcher',
                    'Home Planet': 'Betelges seven' }

pprint.pprint(people)

#выводим на экран значение объекта в списке
print("------------")
print(people['Ford']['Ocupation'])