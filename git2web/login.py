from git2web import app
import git2web.functions
from flask import request, session, g, redirect, url_for, \
     render_template, flash

#login
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid login credentials'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect('/')
    return render_template('login.html', error=error)

#logout
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect('/')
