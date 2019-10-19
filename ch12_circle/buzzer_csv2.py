"""Вариант 3: Чтение данных csv в виде СЛОВАРЯ и вывод на экран построчно"""
import csv, os

os.chdir('/Users/OlegDev/Documents/python/buzzdata') #папка где находится файл

with open('buzzers.csv') as data:   #открывай файл с помощью with
    for line in csv.DictReader(data):   #теперь данные становятся СЛОВАРЕМ
        print(line)  