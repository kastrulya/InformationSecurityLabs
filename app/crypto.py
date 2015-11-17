import hashlib
import os
import psutil
from common import config
from common import files

__author__ = 'bubble'


def get_hash_md5(string):
    hash_object = hashlib.md5(string.encode())
    return hash_object.hexdigest()


def get_computer_info():
    computer_info = []
    mem = psutil.virtual_memory()
    # computer_info.append(str(root.winfo_screenwidth()))
    computer_info.append(str(mem.total))
    computer_info.append(str(os.statvfs('/').f_bsize))
    return "".join(computer_info)


def check_right():
    app_name = "." + config.get_app_name()
    home_dir = files.get_home_dir()
    path = os.path.join(home_dir, app_name)
    hash_info = get_hash_md5(get_computer_info())

    if not files.compare_file_content(path, hash_info):
        raise ValueError("You haven't access")
