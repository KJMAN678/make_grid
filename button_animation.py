from bokeh.layouts import column
from bokeh.models import Button
from bokeh.models.widgets import Div
from bokeh.plotting import curdoc


def load_svg(svg_path):
    with open(svg_path, "r") as f:
        return f.read()


def update_div():
    svg_content = load_svg("mapf.svg")
    div.text = svg_content


button = Button(label="Load SVG", button_type="success")
button.on_click(update_div)

div = Div(text="", width=800, height=600)

layout = column(button, div)
curdoc().add_root(layout)
