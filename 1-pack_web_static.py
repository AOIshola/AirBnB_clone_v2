#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static
folder"""

from fabric.api import *
from datetime import datetime


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
