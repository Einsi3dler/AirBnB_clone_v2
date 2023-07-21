#!/usr/bin/python3
"""
This script creates a tgz archive of the contents of web_static
"""
from fabric.api import *
import os
from datetime import datetime

env.hosts = ['localhost']


def do_pack():
    '''
    This method is an inbuilt method responsible for said archive
    '''
    try:
        filepath = 'versions/web_static_' + datetime.now().\
                   strftime('%Y%m%d%H%M%S') + '.tgz'
        local('mkdir -p versions')
        local('tar -zcvf versions/web_static_$(date +%Y%m%d%H%M%S).tgz\
        web_static')
        print('web_static packed: {} -> {}'.
              format(filepath, os.path.getsize(filepath)))
    except Exception:
        return None
