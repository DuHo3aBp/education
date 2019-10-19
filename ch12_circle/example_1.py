"""Примеры с генераторами"""
import csv, os
import pprint   #pretty-printing позволяет более дружественный вывод на экран

#пример 1
data = [1,2,3,4,5,6,7,8]
evens = [num for num in data if not num % 2] #оператор % выаолняет деление по модулю, т.е. возвращает остаток от деления первого числа на второе
pprint.pprint(evens)

#пример 2
data = [1, 'one', 2, 'two', 3, 'three', 4, 'four']
words = [num for num in data if isinstance(num, str)] #isinstance проверяет тип объекта на который ссылается переменная
print(words)

#пример 3
data = list('So long an thanks for all the fish'.split())
title = [word.title() for word in data] #
print(title)