import files as f
import image as im
from config import *

def main(list):
    # ファイルをクリアする
    f.refresh()

    for name in list:
        f.is_file(name)

    # 画像ファイルをDLする
    for name in list:
        f.download_file_to_dir(name)

    im.create_result(list)