import ConfigParser
import os
from flask import render_template, Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    config = ConfigParser.ConfigParser()
    config.read(path_to_conf())
    list_of_members()
    return render_template('index.html', config=config)

@app.route('/group/<groupname>')
def showgroup(groupname):
    config = ConfigParser.ConfigParser()
    config.read(path_to_conf())
    section = 'group ' + groupname
    return render_template('group.html', config=config,  group=groupname, section=section)

def path_to_gitosis():
    config = ConfigParser.ConfigParser()
    config.read('git2web.cfg')
    return config.get('git2web', 'gitosis-path')

def path_to_conf():
    return path_to_gitosis() + 'gitosis.conf'

def list_of_members():
    path = path_to_gitosis()
    path_to_key = os.path.join(path, 'keydir')
    return map(lambda x: x.split('.pub')[0], os.listdir(path_to_key))

if __name__ == '__main__':
    app.run(debug=True)
