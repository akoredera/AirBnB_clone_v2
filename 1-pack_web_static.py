#!/usr/bin/python3
from fabric.api import local
from time import strftime
from datetime import datetime


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
