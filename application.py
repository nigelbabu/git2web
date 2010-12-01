# all the imports
import sqlite3
import ConfigParser
import os
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from werkzeug import secure_filename

# configuration
GITOSIS_PATH = ''
DEBUG = True
SECRET_KEY = 'asdkfnkq2o428yoidnhjlabsndfkdbsad'
USERNAME = 'admin'
PASSWORD = 'pass123'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

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

# index, project list
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
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    config = ConfigParser.ConfigParser()
    config.read(path_to_conf())
    section = 'group ' + groupname
    if section not in config.sections():
        flash('Group not found')
        return redirect('/')
    return render_template('group.html', config=config,  group=groupname, section=section)

#display people
@app.route('/people')
def showpeople():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    names = list_of_members()
    names.sort()
    return render_template('persons.html', names=names)

#add people
@app.route('/people/add', methods=['GET', 'POST'])
def add_persons():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        f = request.files['key_file']
        filename = secure_filename(f.filename)
        filepath = os.path.join(app.config['GITOSIS_PATH'], 'keydir', filename)
        if filename.rsplit('.', 1)[1] == 'pub':
            if not os.path.exists(filepath):
                f.save(filepath)
                flash('Key uploaded')
            else:
                flash('Key with same name already exists!')
        else:
            flash('Please upload a valid key')
            return redirect(url_for('showpeople'))
    return render_template('add_persons.html')

#delete people
@app.route('/people/del/<name>')
def delete_person(name):
    keyfile = name + '.pub'
    keypath = os.path.join(app.config['GITOSIS_PATH'], 'keydir', keyfile)
    if os.path.exists(keypath):
        if not os.remove(keypath):
            flash(name + ' deleted sucessfully')
        else:
            flash('Could not delete ' + name)
    else:
        flash('Unknown person')
    return redirect(url_for('showpeople'))
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

if __name__ == '__main__':
    app.run()
