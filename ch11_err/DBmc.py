import mysql.connector

"""Исключение в виде пустого класса, наследующего Exception"""
class ConnectionError(Exception):
    pass

class CredentialsError(Exception):
    pass

class SQLError(Exception):
    pass

class UseDatabase:
    """Метод init принимает словарь, который мы назвали config.
    Необяз аннотация None указывает, что метод не возвращает значение.
    Значение аргумента config присваивается атрибуту configuration. """
    def __init__(self, config:dict) -> None:
        self.configuration = config
    """Метод __enter__ должен подключиться к БД """
    def __enter__(self) -> 'cursor': #эта аннотация говорит пользователям класса, что будет возвращаться
        try:
            self.conn = mysql.connector.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except mysql.connector.errors.InterfaceError as err:
            raise ConnectionError(err)
        except mysql.connector.errors.ProgrammingError as err:
            raise CredentialsError(err)

    """Метод __exit__ передает значения в БД, закрывает курсор и соединение с БД   """
    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()