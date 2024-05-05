#!/usr/bin/python3
'''
Keep it clean!
'''
from fabric.api import *
env.hosts = ['34.232.67.117', '34.229.255.100']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_clean(number=0):
    '''
    Fabric script (based on the file 3-deploy_web_static.py)
    that deletes out-of-date archives, using the function do_clean:
    '''
    if number == 1 or number == 0:
        number = 1
        with lcd('versions'):
            local('ls -cr | head --lines -1 | xargs rm -rf')
        with cd('/data/web_static/releases'):
            run('ls -cr | head --lines -1 | xargs rm -rg')
