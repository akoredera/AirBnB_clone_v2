#!/usr/bin/python3
'''
Keep it clean!
'''
from fabric.api import *
env.hosts = ['34.232.67.117', '34.229.255.100']


def do_clean(number=0):
    '''
    Fabric script (based on the file 3-deploy_web_static.py)
    that deletes out-of-date archives, using the function do_clean:
    '''
    number = 1 if int(number) == 0 else int(number)
    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
