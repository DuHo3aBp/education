from flask import Flask, render_template, request, escape #render_template принимает имя шаблона со всеми аргументами и возвращает строку с разметкой HTML
from vsearch6 import search4letters

app = Flask (__name__)

def log_request(req: 'flask_request', res: str) -> None:        #req передает объект запроса
        with open('vsearch.log', 'a') as log:                   #res передает результат вызова 
               """ print(req.form, file = log, end='|') #данные из html формы приложения
                print(req.remote_addr, file = log, end='|')  #IP-адрес приславшешго форму
                print(req.user_agent, file = log, end='|')   #строка, идент-ая веб браузер пользователя
                print(res, file = log)          #None говорит, что ф-я ничего не возвращает
                  """
               print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|') #один принт вместо 4х

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
