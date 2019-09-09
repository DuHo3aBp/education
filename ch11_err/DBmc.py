import mysql.connector

class UseDatabase:
    """Метод init принимает словарь, который мы назвали config.
    Необяз аннотация None указывает, что метод не возвращает значение.
    Значение аргумента config присваивается атрибуту configuration. """
    def __init__(self, config:dict) -> None:
        self.configuration = config
    """Метод __enter__ должен подключиться к БД """
    def __enter__(self) -> 'cursor': #эта аннотация говорит пользователям класса, что будет возвращаться
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor
    """Метод __exit__ передает значения в БД, закрывает курсор и соединение с БД   """
    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()