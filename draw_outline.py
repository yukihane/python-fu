#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import *

def select_opaque_pixels(image, layer):
    pdb.gimp_message_get_handler(ERROR_CONSOLE)
    thickness = 3
    position = pdb.gimp_image_get_item_position(image, layer)

    pdb.gimp_image_select_item(image, 0, layer)
    pdb.gimp_selection_grow(image, thickness)
    new_layer = gimp.Layer(image, "ol_" + layer.name, layer.width + (thickness * 2), layer.height + (thickness * 2), RGBA_IMAGE, 100, NORMAL_MODE)
    gimp.message(str(layer.offsets))
    new_layer.set_offsets(layer.offsets[0] - thickness, layer.offsets[1] - thickness)
    image.add_layer(new_layer, position + 1)
    pdb.gimp_edit_fill(new_layer, BACKGROUND_FILL)

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
