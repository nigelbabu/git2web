from git2web import app
from git2web.functions import path_to_conf, list_of_members
from configobj import ConfigObj
from flask import session, redirect, g, url_for, render_template, \
    flash, request
     
# index, project list
@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    config = ConfigObj(path_to_conf())
    return render_template('index.html', config=config)

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
    return render_template('group.html', config=config,  group=groupname, section=section)

#remove person from the project
@app.route('/group/<groupname>/delete/<person>')
def remove_project_person(groupname, person):
    config = ConfigObj(path_to_conf())
    section = 'group ' + groupname
    members = config[section]['members'].split()
    if person in members:
        members.remove(person)
    config[section]['members'] = ' '.join(members)
    try:
        config.write()
        flash('Deleted person')
    except:
        flash('Could not delete person')
    return redirect(url_for('showgroup', groupname=groupname))

#add person to project
@app.route('/group/<groupname>/add', methods=['GET', 'POST'])
def add_project_person(groupname):
    if request.method == 'POST':
        pass
    else:
        config = ConfigObj(path_to_conf())
        section = 'group ' + groupname
        existing_members = config[section]['members'].split()
        members = filter(lambda x: x not in existing_members, list_of_members())
        if not members:
            flash('No new members')
            return redirect(url_for('showgroup', groupname=groupname))
        return render_template('groupadd.html', members=members, group=groupname)
