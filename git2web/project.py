from git2web import app
from git2web.functions import path_to_conf
from configobj import ConfigObj
from flask import session, redirect, g, url_for, render_template, \
    flash
     
# index, project list
@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    config = ConfigObj(path_to_conf())
    return render_template('index.html', config=config)

#add person to project
@app.route('/group/<groupname>/delete/<person>')
def remove_project_person(groupname, person):
    config = ConfigObj(path_to_conf())
    section = 'group ' + groupname
    members = config[section]['members'].split()
    if person in members:
        members.remove(person)
    config[section]['members'] = ' '.join(members)
    try
    config.write()
    flash('Deleted person')
    return redirect(url_for('showgroup', groupname=groupname))

# individual groups
@app.route('/group/<groupname>')
def showgroup(groupname):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    config = ConfigObj(path_to_conf())
    section = 'group ' + groupname
    if section not in config:
        flash('Group not found')
        return redirect(url_for('index'))
    else:
        return render_template('group.html', config=config,  group=groupname, section=section)
