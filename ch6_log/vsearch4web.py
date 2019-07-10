from flask import Flask, render_template, request, escape #render_template принимает имя шаблона со всеми аргументами и возвращает строку с разметкой HTML
from vsearch6 import search4letters

app = Flask (__name__)

def log_request(req: 'flask_request', res: str) -> None:        #req передает объект запроса
        with open('vsearch.log', 'a') as log:                   #res передает результат вызова 
                print(req, res, file = log)                     #None говорит, что ф-я ничего не возвращает

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
def view_the_log() -> str:      #объявляем новую функцию
        with open('vsearch.log') as log:        #открываем журнал для чтения
                contents = log.read()   #читаем файл целиком и присваиваем его содержимое переменной
        return escape(contents) #возвращаем список строк, escape экранирует символы <> для отобр-я в браузере

if __name__ == '__main__':      #позволяет запускать вебприл. локально
        app.run(debug=True) #режим отладки автомато перезапускает вебсервер если видит изменения
