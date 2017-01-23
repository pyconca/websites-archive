from fabric.api import task, env
from fabric.contrib.project import rsync_project

env.user = 'deploy'
env.hosts = ['portland.pynorth.org']
env.use_ssh_config = True

# Remote Directories
env.html_dir = '/srv/www/pycon.ca/{0}/html/'
env.archives = ['2012', '2013', '2015', '2016']


@task
def deploy():
    for archive in env.archives:
        rsync_project(remote_dir=env.html_dir.format(archive),
                      local_dir='./{0}.pycon.ca/'.format(archive))
