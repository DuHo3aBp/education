"""Вариант 2: Чтение данных csv в виде списков и вывод на экран построчно"""
import csv, os

os.chdir('/Users/OlegDev/Documents/python/buzzdata') #папка где находится файл

with open('buzzers.csv') as data:   #открывай файл с помощью with
    for line in csv.reader(data):   #затем читаем данные построчно с помощью csv.reader
        print(line)  