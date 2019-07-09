from flask import Flask, render_template, request #render_template принимает имя шаблона со всеми аргументами и возвращает строку с разметкой HTML
from vsearch6 import search4letters

app = Flask (__name__)

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
        phrase = request.form['phrase']
        letters = request.form['letters']
        title = 'Here are your results:'
        results = str(search4letters(phrase, letters))
        return render_template('results.html', 
                               the_phrase = phrase,
                               the_letters = letters,
                               the_title = title,
                               the_results=results,)
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
        return render_template('entry.html', the_title='Welcome to search4letters web!')

app.run(debug=True) #режим отладки автомато перезапускает вебсервер если видит изменения
