#!/usr/bin/python3
'''
Full deployment
'''
from fabric.api import *
from 2-do_deploy_web_static import do_deploy
from 1-pack_web_static import do_pack

env.hosts = ['34.232.67.117', '34.229.255.100']


def deploy():
    '''
    Fabric script (based on the file 2-do_deploy_web_static.py)
    that creates and distributes an archive to your web servers,
    using the function deploy
    '''
    output_file = do_pack()
    if output_file is None:
        return False
    return do_deploy(output_file)
