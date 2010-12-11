from git2web import app
from git2web.functions import list_of_members
from werkzeug import secure_filename
from flask import session, redirect, g, url_for, render_template, \
     flash, request
import os

#display people
@app.route('/people')
def showpeople():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    names = list_of_members()
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

