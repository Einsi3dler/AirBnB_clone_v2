#!/usr/bin/python3
from fabric.api import *
from os.path import exists
from datetime import datetime
from fabric.api import local

env.hosts = ['34.224.3.244', '100.25.152.35']

def do_deploy(archive_path):
        """
        This inante method deploys to your webs server
    """
        if exists(archive_path) is False:
            return False
        file_name = archive_path.split('/')[1]
        file_path = '/data/web_static/releases'
        try:
            put(archive_path, '/tmp/')
            run('mkdir -p {}{}'.format(file_path, file_name[:-4]))
            run('tar -xzf /tmp/{} -C {}{}/'.format(file_name,
                                                   file_path, file_name[:-4]))
            run('rm /tmp/{}'.format(file_name))
            run('mv {}{}/web_static/* {}{}/'.format(file_path, file_name[:-4],
                                                    file_path, file_name[:-4]))
            run('rm -rf {}{}/web_static'.format(file_path, file_name[:-4]))
            run('rm -rf /data/web_static/current')
            run('ln -s {}{}/ /data/web_static/current'.format(file_path,
                                                              file_name[:-4]))
            return True
        except Exception:
            return False
