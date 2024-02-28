#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo"""

from fabric.api import *
from datetime import datetime
import os.path

env.hosts = ["100.26.236.29", "100.26.216.44"]
env.user = "ubuntu"

def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if not os.path.isfile(archive_path):
        return False
    put(archive_path, "/tmp/")
    arch_name =  archive_path.split('.')[0]
    run(f"mkdir -p /data/web_static/releases/{arch_name}")

    # creates /data/web_static/releases/{arch_name}/web_static folder
    run(f"tar -xzf /tmp/{archive_path} -C /data/web_static/releases/{arch_name}")
    run(f"rm /tmp/{archive_path}")
    run(f"mv /data/web_static/releases/{arch_name}/web_static/* /data/web_static/releases/{arch_name}")
    run(f"rm -rf /data/web_static/releases/{arch_name}/web_static")
    run("rm /data/web_static/current")
    run("ln -s /data/web_static/releases/{arch_name} /data/web_static/current")
    return True
