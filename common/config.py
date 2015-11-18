from ConfigParser import SafeConfigParser
import os
from os.path import expanduser
import tempfile

__author__ = 'bubble'

parser = SafeConfigParser()


def init():
    parser.read('../bin/config.ini')


def get_remote_zip_url():
    return parser.get('REMOTE', 'zip_url')


def get_app_name():
    return parser.get('APP', 'name')


def get_user_file():
    return parser.get('APP', 'user_file')


def get_certificate_path():
    return parser.get('APP', 'certificate')


def get_data_store_name():
    return parser.get('DATA_STORE', 'name')


def get_temp_dir():
    tempdir_src = str(tempfile.gettempdir())
    return tempdir_src + "/labs"


def get_home_dir():
    return expanduser("~")


def get_registry_file():
    app_name = "." + get_app_name()
    home_dir = get_home_dir()
    path = os.path.join(home_dir, app_name)
    return path

init()
