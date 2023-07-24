#!/usr/bin/python3
"""
Fabscript for deployment
"""
from datetime import datetime as dt
from fabric.api import run, env, put
from os import path

env.hosts = ["34.224.3.244", "100.25.152.35"]

def do_deploy(archive_path):
    """Deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    """
    if not path.exists(archive_path):
        return False
    file_name = path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "~/data/web_static/releases/{}/".format(folder_name)
    Mode = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("sudo mkdir -p {}".format(folder_path))
        run("sudo tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("sudo rm -rf /tmp/{}".format(file_name))
        run("sudo mv {}web_static/* {}".format(folder_path, folder_path))
        run("sudo rm -rf {}web_static".format(folder_path))
        run("sudo rm -rf ~/data/web_static/current")
        run("sudo ln -s {} ~/data/web_static/current".format(folder_path))
        print('New version deployed!')
        Mode = True
    except Exception:
        Mode = False
    return Mode
