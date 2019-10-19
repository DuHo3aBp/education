"""Вариант 5: Чтение данных csv в виде СЛОВАРЯ, преобразование в своем словаре и вывод на экран"""
"""+используем генераторы, чтобы заменить код одной строкой - строка 24"""
import csv, os
import pprint   #pretty-printing позволяет более дружественный вывод на экран

"""Получая время в 24-м формате (в виде строки), церочка методов преобразует его в строку в 12-ти часовом формате"""
from datetime import datetime
def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

os.chdir('/Users/OlegDev/Documents/python/buzzdata') #папка где находится файл

with open('buzzers.csv') as data:   #открывай файл с помощью with
    ignore = data.readline()    #игнорировть заголовок
    flights = {}    #создаем новый пустой словарь
    for line in data:   #обработать каждую стоку
        k, v = line.strip().split(',')    #разбить каждую строку по разделителю на два значения ключ (время вылета) и значение (назначение), strip удаляет пробелы (\n \t \r), splint определяет разделитель
        flights[k] = v  #связать пункт назначения с временем вылета

pprint.pprint(flights)
print()

"""создаем новый генератор словарей в одну строку кода и преобразуем в 12 часовой формат и регистр заголовка"""
fts = {convert2ampm(k): v.title() for k, v in flights.items()}
pprint.pprint(fts)
print()

"""отобразим расписание вылета для каждого из пунктов в новом ненераторе словарей when"""
when = {dest: [k for k, v in fts.items() if v == dest] for dest in set(fts.values())}
pprint.pprint(when)