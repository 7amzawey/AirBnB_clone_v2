#!/usr/bin/python3
""" This module is for a Fabric script that generates a .tgz
archive from the contents of the web_static folder """
from fabric import task
from datetime import datetime
import os


@task
def do_pack(c):
    """Creates a .tgz archive of the web_static directory."""
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"versions/web_static_{timestamp}.tgz"

        if not os.path.exists("versions"):
            os.makedirs("versions")

        # Create the archive
        c.run(f"tar -zcvf {filename} web_static", hide=True)

        # Verify if the archive was created
        if os.path.isfile(filename):
            print(f"Archive created: {filename}")
            return filename
        else:
            print("Failed to create archive")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
