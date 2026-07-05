#! /usr/bin/python3

# 複数の画像を縮小して格子状に並べ、指定したサイズの画像を作る

# ＜動作＞
# 出力画像のサイズを指定する
# 出力画像の格子のうち、横に並べる数を指定する
# 出力画像の格子の縦の数は自動計算
# 出力画像に収まらなかった分は、つぎの出力画像になる
# 出力画像のディレクトリとファイル名の先頭は指定できる
# 複数の出力画像は連番になる

import math
import sys
from PIL import Image

extentions = ('.jpg', '.jpeg', '.png', '.bmp')

def create_tiled_image(output_path, width, height, columns, input_paths):
    # 入力パス群のうち、画像ファイルだけをソートして使う
    input_imgs = [p for p in input_paths if p.endswith(extentions)]
    input_imgs = sorted(input_imgs)
    print('images count:', len(input_imgs))
    #print('imgs:', input_imgs)

    # グリッドの最大サイズ（横のみ指定）
    grid_width = width // columns

    # グリッドの横サイズの縮小率を元に、
    # 実際の画像を一つだけサンプリングしてグリッドの縦サイズを計算
    for i in range(len(input_imgs)):
        try:
            with Image.open(input_imgs[i]) as img:
                grid_height = img.height // (img.width / grid_width)
                break
        except Exception as e:
            pass

    # 出力画像当たりのグリッド数を計算。はみ出さないように。
    rows = height // grid_height
    nimgs = columns * rows

    # 出来上がりのダミー画像を作成
    canvas = Image.new('RGB', (width, height), color='white')
    n = 0
    saved = True

    # 作るよ
    for i in range(len(input_imgs)):
        row = (i % nimgs) // columns
        col = i % columns
        # 出力画像切り替え
        if ((i % nimgs) == 0):
            # 保存
            if (not saved):
                n = n + 1
                canvas.save(output_path + "thumb_" + str(n).zfill(4) + ".jpg")
            # 出来上がりのダミー画像を作成
            canvas = Image.new('RGB', (width, height), color='white')
            saved = False
        try:
            with Image.open(input_imgs[i]) as img:
                # アスペクト比を保ったままリサイズ
                img.thumbnail(size=(grid_width, img.height))
                # 貼り付け
                canvas.paste(img, (int(grid_width * col), int(grid_height * row)))
        except Exception as e:
            print(f'画像読み込み失敗( {input_imgs[i]} ) : {e}')
    # 保存しきれなかった分を保存
    if (not saved):
        n = n + 1
        canvas.save(output_path + "thumb_" + str(n).zfill(4) + ".jpg")



def help():
    print(' usage:')
    print('    command  f  w  h  c  imgs')
    print('     f: output file')
    print('     w: output canvas width')
    print('        if w = 0, canvas width determined by h and c')
    print('     h: output canvas height')
    print('        if h = 0, canvas height determined by w and r')
    print('     c: images count in horizontal')
    print('     imgs: images for input')
    exit(1)

if __name__ == '__main__':
    args = sys.argv
    print(args)
    if (len(args) < 6):
        help()
    output_path = args[1]
    print(f'output file={output_path}')
    w = int(args[2])
    if (w == 0):
        help()
    print(f'width={w}')
    h = int(args[3])
    if (h == 0):
        help()
    print(f'height={h}')
    c = int(args[4])
    if (c == 0):
        help()
    print(f'column count={c}')
    paths = args[5:]
    #print(f'paths={paths}')

    # 作る
    create_tiled_image(output_path, w, h, c, paths)

