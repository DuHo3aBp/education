"""Вариант 1: Читает данные из файла и выводит на экран"""
import os

os.chdir('/Users/OlegDev/Documents/python/buzzdata') #папка где находится файл

with open('buzzers.csv') as raw_data:
    print(raw_data.read())  #метод read читает все файлы за один прием