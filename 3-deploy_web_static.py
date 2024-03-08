#!/usr/bin/python3
"""Executes the full deployment of files to servers"""

from datetime import datetime
from fabric.api import *
import os.path

env.hosts = ["18.204.9.242", "18.204.20.168"]
env.user = "ubuntu"

def do_pack():
    """Compresses the files in web_static"""
    try:
        time = datetime.now()
        folder = local("mkdir -p versions", capture=True)
        filename = f"versions/web_static_{time.strftime('%Y%m%d%H%M%S')}.tgz"
        local(f"tar -cvzf {filename} web_static")
        local(f"chmod g+w {filename}")
        return filename
    except Exception as e:
        return None

def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if not os.path.isfile(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        arch_name =  archive_path.split('/')[1].split('.')[0]
        arch_file = f"{arch_name}.tgz"
        run(f"mkdir -p /data/web_static/releases/{arch_name}")

        # creates /data/web_static/releases/{arch_name}/web_static folder
        run(f"tar -xzf /tmp/{arch_file} -C /data/web_static/releases/{arch_name}")
        run(f"rm /tmp/{arch_file}")
        run(f"mv /data/web_static/releases/{arch_name}/web_static/* /data/web_static/releases/{arch_name}")
        run(f"rm -rf /data/web_static/releases/{arch_name}/web_static")
        run("sudo rm /data/web_static/current")
        run(f"ln -s /data/web_static/releases/{arch_name} /data/web_static/current")
        return True
    except Exception as e:
        return False

def deploy():
    """Deploys files tp web servers"""

    # Pack files into archive
    archive_file = do_pack()

    # Deploy archived file to web server
    output = do_deploy(archive_file)
    return output
