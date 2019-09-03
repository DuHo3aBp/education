from flask import Flask, session

from checker import check_logged_in #импортируем декоратор

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello from simple webapp.'

@app.route('/page1')
@check_logged_in    #применяем декоратор к ф-ии
def page1() -> str:
    return 'This is Page1'

@app.route('/page2')
@check_logged_in    #применяем декоратор к ф-ии
def page2() -> str:
    return 'This is Page2'

@app.route('/page3')
@check_logged_in    #применяем декоратор к ф-ии
def page3() -> str:
    return 'This is Page3'

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in!'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out'

"""Ф-ю можно удалить, после того как импортируем декоратор check_logged_in
@app.route('/status')
def check_status() -> str:
    if 'logged_in' in session:
        return 'You are currently logged in'
    return 'You are NOT logged in'
"""
app.secret_key = 'YouWillNeverGuessMySecretKey'

if __name__ == '__main__':
    app.run(debug=True)