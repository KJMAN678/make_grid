import numpy as np
from bokeh.layouts import column
from bokeh.models import Button
from bokeh.plotting import curdoc, figure
from PIL import Image

image_path = "a.jpeg"
img = Image.open(image_path).convert("RGBA")
img = np.array(img)

imgH, imgW, ch = img.shape

# int32にint8×4ch(RGBA)をviewを使って代入する
img_plt = np.empty((imgH, imgW), dtype=np.uint32)
view = img_plt.view(dtype=np.uint8).reshape((imgH, imgW, 4))
view[:, :, 0:3] = np.flipud(img[:, :, 0:3])  # 上下反転あり
view[:, :, 3] = 255

p = figure(x_range=(0, imgW), y_range=(0, imgH))
p.image_rgba(image=[img_plt.tolist()], x=0, y=0, dw=imgW, dh=imgH)

button = Button(label="Load and Display Image", button_type="success")

layout = column(button, p)
curdoc().add_root(layout)
