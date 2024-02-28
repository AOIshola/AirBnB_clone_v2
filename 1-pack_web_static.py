#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo"""

from fabric.api import *
from datetime import datetime

def do_pack():
    try:
        time = datetime.now()
        folder = local("mkdir -p versions", capture=True)
        filename = f"versions/web_static_{time:%Y%m%d%H%M%S}.tgz"
        local(f"tar -cvzf {filename} web_static")
        size = local(f"du -b {filename} | cut -f1", capture=True)
        print(f"web_static packed: {filename} -> {size}")
        return filename
    except Exception as e:
        return None
