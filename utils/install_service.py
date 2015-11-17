import os
import urllib2
import config
from utils import files, crypto

__author__ = 'bubble'


def test_connection():
    try:
        response = urllib2.urlopen('http://github.com', timeout=1)
        return True
    except urllib2.URLError as err:
        pass
    return False


def get_url():
    return config.get_remote_zip_url()


def get_path_from():
    return config.get_existed_version()


def set_registry_info():
    app_name = "." + config.get_app_name()

    registry_path = os.path.join(files.get_home_dir(), app_name)
    hash_computer_info = crypto.get_hash_md5(files.get_computer_info())
    files.overwrite_file(registry_path, hash_computer_info)


def install_app(path_to_install):
    if test_connection():
        # download latest (if connection is established)
        url = get_url()
        zip_file = files.download_file(url)
    else:
        # existing version
        zip_file = get_path_from()

    files.unzip(zip_file, path_to_install)
    set_registry_info()
