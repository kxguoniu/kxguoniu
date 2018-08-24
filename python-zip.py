# -*- encoding:utf-8 -*-
import os
import re
import zipfile
from datetime import datetime

PATTERN = re.compile(r'^webapp\.log\.(\d{4}-\d{2}-\d{2}).*')

DIRNAME = "C:\\Users\\nsfocus\\Desktop\\temp"
UNZIPTODIR = "C:\\Users\\nsfocus\\Desktop\\nkx"
ZIPFILENAME = "C:\\Users\\nsfocus\\Desktop\\temp.zip"
LOGFILE = "C:\\Users\\nsfocus\\Desktop\\datetime.txt"


def zip_dir(dirname=DIRNAME, zipfilename=ZIPFILENAME):
    if not os.path.isdir(dirname):
        return False
    filelist = [dirname]
    s_time = read_time()
    print '上次结束时间',s_time
    with zipfile.ZipFile(zipfilename, 'w', zipfile.zlib.DEFLATED) as fp:
        while len(filelist) > 0:
            dirpath = filelist[-1]
            pathlist = []
            for file in os.listdir(dirpath):
                filepath = os.path.join(dirpath, file)
                file = filepath[len(dirname)+1:]
                if os.path.isfile(filepath) and searchfile(file, s_time):
                    fp.write(filepath, file)
                    print '压缩文件',file
                elif os.path.isdir(filepath):
                    fp.write(filepath, file)
                    pathlist.append(filepath)
            filelist.pop(-1)
            pathlist.reverse()
            filelist.extend(pathlist)
    return True


def unzip_dir(zipfilename, unziptodir):
    if not os.path.exists(unziptodir):
        os.mkdir(unziptodir)
    with zipfile.ZipFile(zipfilename) as fp:
        for name in fp.namelist():
            filepath = os.path.join(unziptodir, name)
            filepath = filepath.replace('/','\\')
            if name.endswith('\\'):
                if not os.path.isdir(filepath):
                    os.mkdir(filepath)
            else:
                dirpath = os.path.dirname(filepath)
                if not os.path.exists(dirpath):
                    os.mkdir(dirpath)
                fp.extract(name, unziptodir)


def searchfile(filepath, s_time):
    print '匹配文件',filepath
    result = re.search(PATTERN, filepath)
    if not s_time:
        return True
    if result is not None:
        time = result.group(1)
        print time
        e_time = datetime.strptime(time, '%Y-%m-%d')
        if (e_time - s_time).days > 0:
            print '通过',filepath
            return True


def read_time():
    if not os.path.isfile(LOGFILE):
        return False
    with open(LOGFILE, 'r+') as file:
        time = file.read()
        s_time = datetime.strptime(time, '%Y-%m-%d')
    return s_time


def save_time():
    time = datetime.now().strftime('%Y-%m-%d')
    with open(LOGFILE, 'w') as file:
        file.write(time)


status = zip_dir()
if status:
    save_time()
    unzip_dir(ZIPFILENAME, UNZIPTODIR)