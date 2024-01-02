#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import *

def select_opaque_pixels(image, layer):
    pdb.gimp_image_select_item(image, 0, layer)
    pdb.gimp_selection_grow(image, 3)
    new_layer = gimp.Layer(image, "outline", layer.width, layer.height, RGBA_IMAGE, 100, NORMAL_MODE)
    # new_layer.set_offsets(layer.offsets)
    new_layer.fill(0)
    image.add_layer(new_layer, 0)

register(
    "draw_outline",#コマンドラインまたはスクリプトから呼び出す場合のコマンドの名前
    "Draw outline",#プラグインの説明
    "Draw outline",#プラグインの詳細な説明
    "yukihane",#プラグインの作成者
    "yukihane",#プラグインの著作権保有者 (通常は author と同じ)
    "2024/01/02",#著作権の日付
    "<Image>/Filters/Languages/Python-Fu/select_opaque", #メニューの中でプラグインに使用されるラベル
    "RGB*, GRAY*", #プラグインで処理する対象となる画像のタイプex. RGB*, GRAY* など
    [],#引数(型, 名前（プロシージャブラウザに表示される）,説明, 初期値)
    [], # 戻り値
    select_opaque_pixels) # メソッド名

main()
