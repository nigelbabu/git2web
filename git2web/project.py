from git2web import app
from git2web.functions import path_to_conf
import ConfigParser
from flask import redirect, g, session, url_for, render_template, flash
     
# index, project list
@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    config = ConfigParser.ConfigParser()
    config.read(path_to_conf())
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
