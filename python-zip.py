# -*- encoding:utf-8 -*-
import os
import re
import zipfile

PATTERN = re.compile(r'^webapp\.log\.(\d{4})-(\d{2})-(\d{2}).*')

DIRNAME = "C:\\Users\\nsfocus\\Desktop\\temp"
UNZIPTODIR = "C:\\Users\\nsfocus\\Desktop\\nkx"
ZIPFILENAME = "C:\\Users\\nsfocus\\Desktop\\temp.zip"

def zip_dir(dirname=DIRNAME, zipfilename=ZIPFILENAME):
    if not os.path.isdir(dirname):
        return False
    filelist = [dirname]
    with zipfile.ZipFile(zipfilename, 'w', zipfile.zlib.DEFLATED) as fp:
        while len(filelist) > 0:
            dirpath = filelist[-1]
            pathlist = []
            for file in os.listdir(dirpath):
                filepath = os.path.join(dirpath, file)
                file = filepath[len(dirname):]
                if os.path.isfile(filepath):
                    searchfile(filepath)
                    fp.write(filepath, file)
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


def searchfile(filepath):
    result = re.search(PATTERN, filepath)
    if result is not None:
        year = result.group(1)
        mouth = result.group(2)
        day = result.group(3)


status = zip_dir()
if status:
    unzip_dir(ZIPFILENAME, UNZIPTODIR)