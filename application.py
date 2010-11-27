# all the imports
import sqlite3
import ConfigParser
import os
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# configuration
GITOSIS_PATH = ''
DEBUG = True
SECRET_KEY = 'asdkfnkq2o428yoidnhjlabsndfkdbsad'
USERNAME = 'admin'
PASSWORD = 'pass123'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# utility functions
def path_to_conf():
    return app.config['GITOSIS_PATH'] + 'gitosis.conf'

def list_of_members():
    path = app.config['GITOSIS_PATH']
    path_to_key = os.path.join(path, 'keydir')
    return map(lambda x: x.split('.pub')[0], os.listdir(path_to_key))

# index
@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    config = ConfigParser.ConfigParser()
    config.read(path_to_conf())
    list_of_members()
    return render_template('index.html', config=config)

# individual groups
@app.route('/group/<groupname>')
def showgroup(groupname):
    config = ConfigParser.ConfigParser()
    config.read(path_to_conf())
    section = 'group ' + groupname
    return render_template('group.html', config=config,  group=groupname, section=section)

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

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect('/')

if __name__ == '__main__':
    app.run()
