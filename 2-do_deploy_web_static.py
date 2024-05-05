#!/usr/bin/python3
from fabric.api import *
import os

env.hosts = ['34.232.67.117', '34.229.255.100']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    '''
    function generates a .tgz archive from the contents
    of the web_static folder of AirBnB Clone
    '''
    current_datetime = datetime.now()
    formatted_datetime = strftime("%Y%m%d%H%M%S")
    try:
        local('mkdir -p versions')
        result = local('tar -cvzf versions/web_static_{}.tgz web_static/'
                       .format(formatted_datetime))
        return "versions/web_static_{}.tgz".format(formatted_datetime)
    except Exception as e:
        return None


def do_deploy(archive_path):
    '''
     Fabric script (based on the file 1-pack_web_static.py) that
     distributes an archive to your web servers, using the
     function do_deploy
    '''
    try:
        if not (os.path.isfile(archive_path)):
            return False
        put(archive_path, '/tmp/')
        new_file = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(new_file))
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C\
                /data/web_static/releases/web_static_{}/'
            .format(new_file, new_file))
        run('sudo rm /tmp/web_static_{}.tgz'.format(new_file))
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/*\
                /data/web_static/releases/web_static_{}/'
            .format(new_file, new_file))
        run('sudo rm -rf /data/web_static/releases/web_static_{}/web_static'
            .format(new_file))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s /data/web_static/releases/web_static_{}\
                /data/web_static/current'.format(new_file))
        return True
    except Exception as e:
        return False
