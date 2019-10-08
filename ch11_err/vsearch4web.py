from flask import Flask, render_template, request, escape, session #render_template принимает имя шаблона со всеми аргументами и возвращает строку с разметкой HTML
from flask import copy_current_request_context

from vsearch6 import search4letters

from DBmc import UseDatabase, CredentialsError, ConnectionError, SQLError
from checker import check_logged_in #импортируем декоратор

from time import sleep
from threading import Thread #модуль многопоточности 

app = Flask (__name__)

app.config['dbconfig'] = { 'host': '127.0.0.1',   #Flask использует словарь app.config. Добавляем его.
                           'user': 'vsearch',
                           'password': 'vsearchpasswd',
                           'database': 'vsearchlogDB', }

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in!'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out!'

@app.route('/search4', methods=['POST'])
@check_logged_in
def do_search() -> 'html': 
        @copy_current_request_context #юзаем декоратор, чтобы данные не очищались до выполнения ф-ии
        def log_request(req: 'flask_request', res: str) -> None:        #req передает объект запроса
            """Функция журналирует веб-запрос в БД и возвращает результаты"""
            """Теперь используем диспетчер контекста UseDatabase, которому передаем
            настройки app.config"""
            sleep(15) #this makes log_request wery slow...
            with UseDatabase(app.config['dbconfig']) as cursor:
                _SQL = """insert into log
                        (phrase, letters, ip, browser_string, results)
                        values
                        (%s, %s, %s, %s, %s)""" # создзаем строку с текстом запроса для записи в БД
                cursor.execute(_SQL, (req.form['phrase'],   #выполняем запрос
                                    req.form['letters'],
                                    req.remote_addr,
                                    req.user_agent.browser,   #из строки с описанием браузера извлекается только его название
                                    res,))
        """Извлекает данные из запроса, выполняет поиск, возвращает результаты"""
        phrase = request.form['phrase']
        letters = request.form['letters']
        title = 'Here are your results:'
        results = str(search4letters(phrase, letters))
        try:
            t = Thread(target=log_request, args=(request,results)) #вызов функции журналирования через многопоточность
            t.start()    #запускаем поток
        except Exception as err:
            print('***** Logging failed with this error:', str(err))
        return render_template('results.html', 
                               the_title = title,
                               the_phrase = phrase,
                               the_letters = letters,
                               the_results=results,)
        
@app.route('/')
@app.route('/entry')
@check_logged_in
def entry_page() -> 'html':
        """Выводит  HTML форму"""
        return render_template('entry.html', the_title='Welcome to search4letters web!')

@app.route('/viewlog')  #будем читать лог со страницы
@check_logged_in
def view_the_log() -> 'html':      #объявляем новую функцию
        """Выводит содержимое файла журнала в виде HTML таблицы"""
        try:
            with UseDatabase(app.config['dbconfig']) as cursor:
                    _SQL = """select phrase, letters, ip, browser_string, results 
                            from log"""
                    """отправляем запрос на сервер
                    затем извлекаем результаты (присваиваются
                    переменной contents"""        
                    cursor.execute(_SQL)
                    contents = cursor.fetchall()
            
            """определяем имена столбцов"""
            titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
            
            return render_template ('viewlog.html',
                                    the_title='View log',
                                    the_row_titles=titles,
                                    the_data=contents,)
        except ConnectionError as err:
            print('Is your database switched on? Error:', str(err))
        except CredentialsError as err:
            print('Wrong user ID or Password or wrong database. Error:', str(err))
        except SQLError as err:
            print('Is your query correct? Error:', str(err))
        except Exception as err:
            print('Something went wrong', str(err))
        return 'Sorry! There is an Error occured. Please try later or call to Oleg.'

app.secret_key = 'YouWillNeverGuessMySecretKey'

if __name__ == '__main__':      #позволяет запускать вебприл. локально
        app.run(debug=True) #режим отладки автомато перезапускает вебсервер если видит изменения
