# all the imports
from flask import Flask

# configuration
GITOSIS_PATH = '/home/nigelbabu/git-admin/'
DEBUG = True
SECRET_KEY = 'asdkfnkq2o428yoidnhjlabsndfkdbsad'
USERNAME = 'admin'
PASSWORD = 'pass123'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

import git2web.login
import git2web.people
import git2web.project
import git2web.functions

if __name__ == '__main__':
    app.run()
