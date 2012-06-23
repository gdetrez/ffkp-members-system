from fabric.api import *
from datetime import datetime
from fabric.contrib import files, console
from fabric.contrib.project import rsync_project
from fabric import utils
import os

env.hosts = ['178.79.156.98']
env.user = 'gdetrez'
env.root = '/srv/members.ffkp.se'
env.project_root = os.path.join(env.root,'ffkp')
env.virtualenv_root = os.path.join(env.root,'env')
env.activate_script = os.path.join(env.virtualenv_root, 'bin','activate')

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
    '_static'
)

@task(default=True)
def deploy():
    if not console.confirm('Are you sure you want to deploy production?',
                           default=False):
        utils.abort('Production deployment aborted.')
    rsync()
    collectstatic()
    reload()


def virtualenv(command, use_sudo=False):
    if use_sudo:
        func = sudo
    else:
        func = run
    func('source "%s" && %s' % (env.activate_script, command))

def manage_py(command, use_sudo=False):
    with cd(env.project_root):
        virtualenv('python manage.py %s' % command, use_sudo)

@task
def collectstatic():
    #require('hosts', provided_by=[production])
    manage_py('collectstatic -l --noinput')

@task
def rsync():
    """ rsync code to remote host """
    extra_opts = '--omit-dir-times'
    rsync_project(
        env.root,
        exclude=RSYNC_EXCLUDE,
        delete=True,
        extra_opts=extra_opts,
    )

@task
def reload():
    """ Restart the wsgi process """
    sudo("supervisorctl restart members.ffkp.se")
