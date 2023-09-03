import numpy as np
from bokeh.layouts import column
from bokeh.models import Button, ColumnDataSource, Slider
from bokeh.plotting import curdoc, figure

# 初期のグリッドサイズ
INIT_SIZE = 10
size = INIT_SIZE
cell_size = 20  # 各セルのサイズ

# source = ColumnDataSource(data=dict(x=[], y=[], colors=[], texts=[]))

# # プロットを作成
# p = figure(width=size * cell_size, height=size * cell_size, tools="tap", title="Adjustable and Clickable Grid")
# p.rect("x", "y", 1, 1, color="colors", source=source)
# p.text("x", "y", text="texts", text_align="center", text_baseline="middle", source=source)
# p.grid.visible = False
# p.axis.visible = False


# グリッドを更新する関数
def update_grid():
    global size
    x = [i % size for i in range(size * size)]
    y = [i // size for i in range(size * size)]
    colors = ["white"] * (size * size)
    texts = ["."] * (size * size)
    source.data = dict(x=x, y=y, colors=colors, texts=texts)
    p.width = size * cell_size
    p.height = size * cell_size


# クリックイベントのコールバック
def callback(attr, old, new):
    inds = new
    if inds:
        index = inds[0]
        current_color = source.data["colors"][index]
        new_color = "blue" if current_color == "white" else "white"
        new_text = "#" if current_color == "white" else "."
        source.data["colors"][index] = new_color
        source.data["texts"][index] = new_text
        source.data = dict(source.data)

        output_grid = np.array(source.data["texts"]).reshape(size, size).tolist()
        output_grid.reverse()
        output_grid = "\n".join(["".join(row) for row in output_grid])
        print(output_grid)
        print()


# ボタンのコールバック
def button_callback():
    global size
    size = slider.value
    update_grid()


source = ColumnDataSource(data=dict(x=[], y=[], colors=[], texts=[]))

# プロットを作成
p = figure(width=size * cell_size, height=size * cell_size, tools="tap", title="Adjustable and Clickable Grid")
p.rect("x", "y", 1, 1, color="colors", source=source)
p.text("x", "y", text="texts", text_align="center", text_baseline="middle", source=source)
p.grid.visible = False
p.axis.visible = False

source.selected.on_change("indices", callback)

slider = Slider(start=5, end=100, value=INIT_SIZE, step=1, title="Grid Size")

button = Button(label="Update Grid", button_type="success")
button.on_click(button_callback)

layout = column(slider, button, p)
curdoc().add_root(layout)

update_grid()
