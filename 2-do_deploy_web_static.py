#!/usr/bin/python3
from fabric.api import *
import os

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
        if not (os.path.exists(archive_path):
            return False
        put('archive_path, /tmp/')
        new_file = archive_path[-18:-4]
         run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(new_file))
        run('sudo tar -xzf /tmp/archive_path -C\
                /data/web_static/releases/web_static_{}/'.format(new_file))
        run('sudo rm /tmp/archive_path')
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* /data/web_static/releases/web_static_{}'.format(new_file, new_file))
        run('rm -rf /data/web_static/releases/web_static_{}/web_static'.format(new_file))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln sudo ln -sf /data/web_static/releases/web_static_{}\
                /data/web_static/current'.format(new_file))
        return True
    except Exception as e:
        return False
