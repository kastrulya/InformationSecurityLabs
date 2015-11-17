import os
import shutil
import tempfile
import urllib2
import re
import zipfile
from os.path import expanduser
import psutil

__author__ = 'bubble'


def get_temp_dir():
    tempdir_src = str(tempfile.gettempdir())
    return tempdir_src + "/labs"


def get_home_dir():
    return expanduser("~")


def unzip(file_path, target_dir, mask='.'):
    pattern = re.compile(mask)
    fh = open(file_path, 'rb')
    z = zipfile.ZipFile(fh)
    names = [f for f in z.namelist() if pattern.match(f)]
    tempdir = os.path.join(get_temp_dir(), "unzip")
    for name in names:
        outpath = tempdir
        z.extract(name, outpath)
    fh.close()
    move_tree(os.path.join(tempdir, z.namelist()[0]), target_dir)


def move_tree(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    shutil.move(src, dst)


def download_file(url, target_dir=get_temp_dir()):
    file_name = os.path.basename(url)

    os.umask(0002)
    u = urllib2.urlopen(url)
    f = os.path.join(target_dir, file_name)

    dir = os.path.dirname(f)
    if not os.path.exists(dir):
        os.makedirs(dir)

    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    with open(f, 'wb') as fp:
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            fp.write(buffer)
            status = r"%10d  [%3.2f%%]" % (
                file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8) * (len(status) + 1)
            print status

    return f


def get_computer_info():
    computer_info = []
    mem = psutil.virtual_memory()
    # computer_info.append(str(root.winfo_screenwidth()))
    computer_info.append(str(mem.total))
    computer_info.append(str(os.statvfs('/').f_bsize))
    return "".join(computer_info)


def overwrite_file(path, data):
    file = open(path, "w")
    data = file.write(data)
    file.close()
    return data