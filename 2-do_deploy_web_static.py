#!/usr/bin/python3
from fabric.api import *

env.hosts = ['34.232.67.117', '34.229.255.100']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    '''
     Fabric script (based on the file 1-pack_web_static.py) that
     distributes an archive to your web servers, using the
     function do_deploy
    '''
    try:
        if not archive_path:
            return False
        put('archive_path, /tmp/')
        new_file = archive_path[:-4]
        run('sudo tar -xzf /tmp/archive_path -C\
                /data/web_static/releases/{}'.format(new_file))
        run('sudo rm /tmp/archive_path')
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln sudo ln -sf /data/web_static/releases/{}\
                /data/web_static/current'.format(new_file))
        return True
    except Exception as e:
        return False
