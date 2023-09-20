import files as f
import parse as p
import image as im
from config import *

list = p.load_deck_file()

# ファイルをクリアする
f.refresh()

for name in list:
     f.is_file(name)

# 画像ファイルをDLする
for name in list:
    f.download_file_to_dir(name)

im.create_result(list)