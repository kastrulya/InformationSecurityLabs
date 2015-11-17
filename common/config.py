from ConfigParser import SafeConfigParser

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


init()