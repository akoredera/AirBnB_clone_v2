#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    '''
    function generates a .tgz archive from the contents
    of the web_static folder of AirBnB Clone
    '''
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S")
    try:
        local('mkdir -p /root/AirBnB_clone_v2/versions')
        result = local('tar -cvzf versions/web_static_{}.tgz web_static/'
                       .format(formatted_datetime))
        return "versions/web_static_{}.tgz".format(formatted_datetime)
    except Exception as e:
        return None
