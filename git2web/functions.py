from git2web import app
import git2web.functions
from subprocess import Popen
from datetime import datetime
import os

# utility functions
def path_to_conf():
    return app.config['GITOSIS_PATH'] + 'gitosis.conf'

def list_of_members():
    path = app.config['GITOSIS_PATH']
    path_to_key = os.path.join(path, 'keydir')
    member_names = map(lambda x: x.split('.pub')[0], os.listdir(path_to_key))
    member_names.sort()
    return member_names
    
def git_commit():
	commit_cmd = 'git commit -a -m \'Change from git2web at %s\'' % (str(datetime.now()))
	p = Popen(commit_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, errors = p.communicate()
	
def git_add():
    add_cmd = 'git add . '
    p = Popen(add_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, errors = p.communicate()
