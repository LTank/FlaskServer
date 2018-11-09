from flask import Flask, render_template, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)
Bootstrap(app)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            print(session)
            return redirect(url_for('admin'))
    return render_template('login.html', error=error)


@app.route('/logout', methods=['GET'])
def logout():
    session['logged_in'] = False
    print(session)
    return redirect(url_for('index'))


@app.route('/admin', methods=['GET'])
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template('admin.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run()
