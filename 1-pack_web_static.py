#!/usr/bin/python3
'''Fabric script to generate .tgz archive
and distribute it on env.host servers'''

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ Packs all the content of the webstatic 
	folder into a tgz compressed archive
    """
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    path = 'versions/web_static_' + datetime.now().\
                   strftime('%Y%m%d%H%M%S') + '.tgz'
    try:
        local("tar -cvzf {} web_static".format(path))
        archize_size = os.stat(path).st_size
    except Exception:
        path = None
    return path
