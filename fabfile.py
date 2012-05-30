from fabric.api import *
from datetime import datetime
from fabric.contrib import files, console
from fabric.contrib.project import rsync_project
from fabric import utils
import os

env.hosts = ['178.79.156.98']
env.user = 'gdetrez'
env.root = '/srv/members.ffkp.se'
env.virtualenv_root = os.path.join(env.root,'env')

RSYNC_EXCLUDE = (
    '.DS_Store',
    '.git',
    'env',
    '*.pyc',
    '*.db',
    '*~',
    'local_settings.py',
    'fabfile.py',
    'bootstrap.py',
)

@task(default=True)
def deploy():
    """ rsync code to remote host """
    if not console.confirm('Are you sure you want to deploy production?',
                           default=False):
        utils.abort('Production deployment aborted.')
    extra_opts = '--omit-dir-times'
    rsync_project(
        env.root,
        exclude=RSYNC_EXCLUDE,
        delete=True,
        extra_opts=extra_opts,
    )
    touch()

def touch():
    """ touch wsgi file to trigger reload """
    #require('code_root', provided_by=('staging', 'production'))
    apache_dir = os.path.join(env.root, 'ffkp', 'ffkp')
    with cd(apache_dir):
        run('touch wsgi.py')
