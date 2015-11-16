import os

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