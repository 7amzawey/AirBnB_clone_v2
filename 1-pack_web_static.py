#!/usr/bin/python3
""" this module is for a fabric script that generates a .tgz
archive from the contents of the web_static folder"""
from fabric import task
from datetime import datetime
import os


@task
def do_pack(c):
    """
    makes a .tgz to the directory web_static
    """
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"web_static_{timestamp}.tgz"
        if not os.path.exists("versions"):
            os.makedirs("versions")

        c.local(f"tar -zcvf {filename} /web_static")

        if os.path.exists(filename):
            return filename
        else:
            return None
    except Exception:
        return None
