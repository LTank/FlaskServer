from flask import Flask, render_template, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
import os
import json
import api
from mock import jsonstr
import formValidator

app = Flask(__name__)
app.secret_key = os.urandom(12)
Bootstrap(app)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    # This is the code to use!
    msgs = api.get_all_messages()
    return render_template('index.html', msgs=msgs)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            session['current_usr'] = None
            print(session)
            return redirect(url_for('message'))
    return render_template('login.html', error=error)


@app.route('/logout', methods=['GET'])
def logout():
    session['logged_in'] = False
    print(session)
    return redirect(url_for('index'))


@app.route('/message', methods=['GET', 'POST'])
def message():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        if request.method == 'GET':
            return render_template('message.html')
        else:

            dict_to_send = {'msg': request.form['message'], 'user_id': session.get('current_usr')}
            json_to_send = json.dumps(dict_to_send)
            # Calls API from here /message POST
            return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run()
