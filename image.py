import cv2
import parse as p
import numpy as np
from config import *

def create_result(list):
    row_l = 10
    col_l = 7

    image = cv2.imread(f"{DST_DIR}/{list[0]}{FORMAT_SUFFIX}")

    # 画像の縦横サイズを取得
    height, width, channels = image.shape

    # 画像を横に10列、縦に7行に並べるためのキャンバスを作成
    canvas_width = width * row_l
    canvas_height = height * col_l
    canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

    for i in range(col_l):
        for j in range(row_l):
            index = i * row_l + j
            if index < len(list):
                image = cv2.imread(DST_DIR + "/" + list[index] + FORMAT_SUFFIX)
                canvas[i * height:(i + 1) * height, j * width:(j + 1) * width] = image

    cv2.imwrite(f"{DST_DIR}/result.png", canvas)
