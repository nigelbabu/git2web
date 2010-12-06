from git2web import app
import git2web.functions
import os

# utility functions
def path_to_conf():
    return app.config['GITOSIS_PATH'] + 'gitosis.conf'

def list_of_members():
    path = app.config['GITOSIS_PATH']
    path_to_key = os.path.join(path, 'keydir')
    return map(lambda x: x.split('.pub')[0], os.listdir(path_to_key))
