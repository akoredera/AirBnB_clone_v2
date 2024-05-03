#!/usr/bin/python3
'''
Compress before sending
'''

from fabric.api import *
from datetime import datetime
'''
env.user = 'ubuntu'
env.hosts = ['34.229.255.100', '34.232.67.117']
'''


def do_pack():
    '''
    function generates a .tgz archive from the contents
    of the web_static folder of AirBnB Clone
    '''
    current_datetime = datetime.now()
    try:
        local('mkdir -p /root/AirBnB_clone_v2/versions')
        formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S")
        result = local('tar -cvzf versions/web_static_{}.tgz web_static/'
                       .format(formatted_datetime))
        return "/root/AirBnB_clone_v2/versions/web_static_{}.tgz"
    except Exception as e:
        return None
