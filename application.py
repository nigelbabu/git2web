import ConfigParser, os
from flask import render_template, Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    config = ConfigParser.ConfigParser()
    config.read('gitosis.conf')
    return render_template('index.html', config=config)

@app.route('/group/<groupname>')
def showgroup(groupname):
    config = ConfigParser.ConfigParser()
    config.read('gitosis.conf')
    section = 'group ' + groupname
    return render_template('group.html', config=config,  group=groupname, section=section)

if __name__ == '__main__':
    app.run(debug=True)
