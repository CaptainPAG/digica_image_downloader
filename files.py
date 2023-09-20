import os
import urllib.error
import urllib.request
import shutil
from config import * 
import time

def refresh():
    if (not os.path.isdir(DST_DIR)):
        os.mkdir(DST_DIR)
    shutil.rmtree(DST_DIR)
    os.mkdir(DST_DIR)

def is_file(file_name):
    return os.path.isfile(f"{DST_DIR}/{file_name}{FORMAT_SUFFIX}")

def copy(path):
    update_path = f"{path}-{int(time.time() * 100000)}"

    shutil.copy(f"{DST_DIR}/{path}{FORMAT_SUFFIX}", f"{DST_DIR}/{update_path}{FORMAT_SUFFIX}")
    print(f"CP file: {DST_DIR}/{update_path}{FORMAT_SUFFIX}")

def download_file(path, dst_path):
    try:
        if is_file(path):
            copy(path)
        else:
            url = f"{BASE_URL}{path}{FORMAT_SUFFIX}"
            with urllib.request.urlopen(url) as web_file:
                data = web_file.read()
                with open(dst_path, mode='wb') as local_file:
                    local_file.write(data)
                    print(f"DL file: {local_file.name}")
    except urllib.error.URLError as e:
        print(e)

def download_file_to_dir(path):
    download_file(path, os.path.join(DST_DIR, f"{path}{FORMAT_SUFFIX}"))