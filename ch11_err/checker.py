"""Создаем отдельный модуль для декоратора, который будет использоваться в simple_webapp.py
чтобы избежать повтора копирования кода для проверки в системе ли пользователь.
Сам файл checker.py надо поместить в ту же директорию где simple_webapp.py"""
from flask import session

from functools import wraps #обяз.имп-ть ф-ю, кот.является декоратором из стандартной библиотеки

def check_logged_in(func):
    @wraps(func)    #декорируем ф-ю wrapper с пом.декоратора wraps
    def wrapper(*args, **kwargs):  #вложенная строка def означает начало вложенной функции wrapper
                                    #*args - означает список элементов, 
                                    # **rwargs - словарь ключей и значений позволяет принимать ф-ии wrapper любое кол-во аргументов
        if 'logged_in' in session:  #если пользователь браузера выполнид вход...
            return func(*args, **kwargs)    #...вызвать декорируемую функцию
        return 'You are NOT logged in.' #...иначе вернуть сообщение
    return wrapper  #возвращаем вложенную функцию