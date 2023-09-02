import numpy as np
from bokeh.layouts import column
from bokeh.models import Button, ColumnDataSource
from bokeh.plotting import curdoc, figure
from PIL import Image


# 画像を読み込んで表示するコールバック関数
def load_and_display():
    # ここでローカルの画像を読み込みます
    image_path = "a.jpeg"
    img = Image.open(image_path).convert("RGBA")
    img = np.array(img)

    imgH, imgW, ch = img.shape

    # int32にint8×4ch(RGBA)をviewを使って代入する
    img_plt = np.empty((imgH, imgW), dtype=np.uint32)
    view = img_plt.view(dtype=np.uint8).reshape((imgH, imgW, 4))
    view[:, :, 0:3] = np.flipud(img[:, :, 0:3])  # 上下反転あり
    view[:, :, 3] = 255

    # 画像データを更新
    source.data = dict(image=[img_plt], dw=[imgW], dh=[imgH])
    p.x_range.end = imgW
    p.y_range.end = imgH


# 初期の空の画像データ
source = ColumnDataSource(data=dict(image=[]))

# プロットを作成
p = figure(x_range=(0, 10), y_range=(0, 10), width=300, height=300, match_aspect=True)
p.image_rgba(image="image", x=0, y=0, dw="dw", dh="dh", source=source)

# ボタンを作成
button = Button(label="Load and Display Image", button_type="success")
button.on_click(load_and_display)

layout = column(button, p)
curdoc().add_root(layout)
