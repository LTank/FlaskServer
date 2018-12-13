from flask import Flask, render_template, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
import os
import json
import api

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
        usr = api.get_user(request.form['username'], request.form['password'])
        if usr is None:
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            session['current_usr'] = usr
            print(session)
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/logout', methods=['GET'])
def logout():
    session['logged_in'] = False
    session['current_usr'] = None
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
            api.post_message(json_to_send)
            return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and request.form['password'] == request.form['retype']:
        dict_to_send = {'usr_name': request.form['username'], 'usr_pswd': request.form['password']}
        json_to_send = json.dumps(dict_to_send)
        api.create_user(json_to_send)
        return redirect(url_for('login'))
    else:
        return render_template('register.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run()
