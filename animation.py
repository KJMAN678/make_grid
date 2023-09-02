from bokeh.layouts import column
from bokeh.models.widgets import Div
from bokeh.plotting import curdoc

# SVG ファイルを読み込む
with open("mapf.svg", "r") as f:
    svg_content = f.read()

# SVG を Div ウィジェットに埋め込む
div = Div(text=svg_content, width=500, height=500)

curdoc().add_root(column(div))
