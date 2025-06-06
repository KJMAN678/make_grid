import random

import numpy as np
from bokeh.layouts import column, row
from bokeh.models import Button, ColumnDataSource, Slider
from bokeh.models.widgets import Div
from bokeh.plotting import curdoc, figure

from pogema import GridConfig, pogema_v0
from pogema.svg_animation.animation_wrapper import AnimationMonitor

SVG_FILE_PATH = "mapf.svg"
INIT_SIZE = 10
size = INIT_SIZE
cell_size = 20  # 各セルのサイズ
output_grid_list = []

#####################


# クリックイベントのコールバック
def grid_click_callback(attr, old, new):
    global output_grid_str, output_grid_list
    inds = new
    if inds:
        index = inds[0]
        current_color = source.data["colors"][index]
        new_color = "blue" if current_color == "white" else "white"
        new_text = "#" if current_color == "white" else "."
        source.data["colors"][index] = new_color
        source.data["texts"][index] = new_text
        source.data = dict(source.data)

        output_grid_list = np.array(source.data["texts"]).reshape(size, size).tolist()
        output_grid_list.reverse()
        output_grid_str = "\n".join(["".join(row) for row in output_grid_list])


def running_mapf_and_display_svg(file_path=SVG_FILE_PATH, num_agents=2):
    global display_svg_div, output_grid_list

    num_agents = slider_agent_num.value

    output_grid_list = np.array(output_grid_list)
    np.where(output_grid_list == ".")

    blank_coordinate_list = []

    # INIT_SIZE - 3 を上限としないとエラーがでる？
    for i, j in zip(
        np.where(output_grid_list == ".")[0], np.where(output_grid_list == ".")[1]
    ):
        if (
            i >= int(size * 0.3)
            and j >= int(size * 0.3)
            and i <= size - int(size * 0.4)
            and j <= size - int(size * 0.4)
        ):
            blank_coordinate_list.append([i, j])

    agents_xy = []
    targets_xy = []
    for _ in range(num_agents):
        index_agents = random.randint(0, len(blank_coordinate_list) - 1)
        index_targets = random.randint(0, len(blank_coordinate_list) - 1)
        agents_xy.append(blank_coordinate_list[index_agents])
        targets_xy.append(blank_coordinate_list[index_targets])

    print(agents_xy, targets_xy)

    grid_config = GridConfig(
        num_agents=num_agents,
        density=0.4,
        seed=1,
        max_episode_steps=512,
        obs_radius=3,
        map=output_grid_str,
        agents_xy=agents_xy,
        targets_xy=targets_xy,
    )

    env = pogema_v0(grid_config=grid_config)
    env = AnimationMonitor(env)

    obs, info = env.reset()

    terminated = truncated = [False, ...]

    while not all(terminated) and not all(truncated):
        # Use random policy to make actions
        obs, reward, terminated, truncated, info = env.step(
            [env.action_space.sample() for _ in range(grid_config.num_agents)]
        )

    env.save_animation(file_path)

    # MAPF のSVGを表示する
    svg_content = load_svg(SVG_FILE_PATH)
    display_svg_div.text = svg_content


def load_svg(svg_path):
    with open(svg_path, "r") as f:
        return f.read()


# グリッドの作成

slider_grid_size = Slider(
    start=10, end=30, value=size, step=1, title="グリッドのサイズ"
)
slider_agent_num = Slider(start=2, end=10, value=2, step=1, title="エージェントの数")

# 初期のグリッドサイズ
source = ColumnDataSource(data=dict(x=[], y=[], colors=[], texts=[]))

# プロットを作成
grid_plot = figure(
    width=size * cell_size,
    height=size * cell_size,
    tools="tap",
    title="Adjustable and Clickable Grid",
)
grid_plot.rect("x", "y", 1, 1, color="colors", source=source)
grid_plot.text(
    "x", "y", text="texts", text_align="center", text_baseline="middle", source=source
)
grid_plot.grid.visible = False
grid_plot.axis.visible = False


# グリッドを更新する関数
def update_grid_gui():
    global size
    x = [i % size for i in range(size * size)]
    y = [i // size for i in range(size * size)]
    colors = ["white"] * (size * size)
    texts = ["."] * (size * size)
    source.data = dict(x=x, y=y, colors=colors, texts=texts)
    grid_plot.width = size * cell_size
    grid_plot.height = size * cell_size


# ボタンのコールバック
def button_update_grid_size_callback():
    global size
    size = slider_grid_size.value
    update_grid_gui()


source.selected.on_change("indices", grid_click_callback)

# グリッドの確定
button_make_grid = Button(label="グリッドのサイズ変更", button_type="success")
button_make_grid.on_click(button_update_grid_size_callback)

update_grid_gui()

# MAPFの実行および表示
button_running_mapf = Button(label="MAPFの実行", button_type="success")
button_running_mapf.on_click(running_mapf_and_display_svg)

display_svg_div = Div(text="", width=100, height=100)

layout = row(
    column(
        slider_grid_size,
        slider_agent_num,
        button_make_grid,
        grid_plot,
        button_running_mapf,
    ),
    column(display_svg_div),
)
curdoc().add_root(layout)
