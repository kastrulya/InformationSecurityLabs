import os
from os.path import expanduser
import tempfile

__author__ = 'bubble'


def read_from_file(path):
    try:
        file = open(path, "r")
        data = file.read()
        file.close()
        return data
    except IOError as e:
        return e


def write_to_file(path_storage, data, delimiter):
    if os.path.exists(path_storage):
        old_data = read_from_file(path_storage) + delimiter
        data = old_data + data + delimiter
    overwrite_file(path_storage, data)


def overwrite_file(path_storage, data):
    file = open(path_storage, "w")
    file.write(data)
    file.close()


def get_temp_dir():
    tempdir_src = str(tempfile.gettempdir())
    return tempdir_src + "/labs"


def get_home_dir():
    return expanduser("~")


def compare_file_content(file1, str):
    str_file = read_from_file(file1)
    return str_file==str
