from flask import Flask, render_template, request, escape #render_template принимает имя шаблона со всеми аргументами и возвращает строку с разметкой HTML
from vsearch6 import search4letters

app = Flask (__name__)

def log_request(req: 'flask_request', res: str) -> None:        #req передает объект запроса
    """изменили функцию, Журналирует веб-запрос в БД и возвращает результаты"""
    dbconfig = { 'host': '127.0.0.1',   #определяем параметры соединения
                 'user': 'vsearch',
                 'password': 'vsearchpasswd',
                 'database': 'vsearchlogDB', }
    import mysql.connector  #импортируем драйвер
    conn = mysql.connector.connect(**dbconfig)  #устанавливаем соединение
    cursor = conn.cursor()  #создаем курсор
    _SQL = """  insert into log
                (phrase, letters, ip, browser_string, results)
                values
                (%s, %s, %s, %s, %s)""" # создзаем строку с текстом запроса для записи в БД
    cursor.execute(_SQL,(req.form['phrase'],   #выполняем запрос
                         req.form['letters'],
                         req.remote_addr,
                         req.user_agent.browser,   #из строки с описанием браузера извлекается только его название
                         res,))
    conn.commit()   #записываем данные в БД и закрываем курсор и соединение
    cursor.close()
    conn.close()

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
        phrase = request.form['phrase']
        letters = request.form['letters']
        title = 'Here are your results:'
        results = str(search4letters(phrase, letters))
        log_request(request,results)    #вызов функции журналирования
        return render_template('results.html', 
                               the_phrase = phrase,
                               the_letters = letters,
                               the_title = title,
                               the_results=results,)
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
        return render_template('entry.html', the_title='Welcome to search4letters web!')

@app.route('/viewlog')  #будем читать лог со страницы
def view_the_log() -> 'html':      #объявляем новую функцию
        contents = []   #создать новый пустой список
        with open('vsearch.log') as log:        #открываем файл журнала для чтения и связываем с log
                for line in log:        #организовать цикл по строкам в файловом потоке log
                        contents.append([])     #добавить новый, пустой список в конец contents
                        for item in line.split('|'): #разбить строку а затем обработкать каждый эл-т в списке
                                contents[-1].append(escape(item)) #записать экранированные данные в конец списка
        titles = ('Form data', 'Remote_addr', 'User_agent', 'Results')
        return render_template ('viewlog.html',
                                the_title='View log',
                                the_row_titles=titles,
                                the_data=contents,)

if __name__ == '__main__':      #позволяет запускать вебприл. локально
        app.run(debug=True) #режим отладки автомато перезапускает вебсервер если видит изменения
