import numpy as np
from bokeh.layouts import column
from bokeh.models import Button
from bokeh.models.widgets import Div
from bokeh.plotting import curdoc

from pogema import GridConfig, pogema_v0
from pogema.animation import AnimationMonitor

SVG_FILE_PATH = "mapf_button.svg"


def mapf(file_path=SVG_FILE_PATH, num_agents=2):
    grid = """
    .....#.....
    .....#.....
    ...........
    .....#.....
    .....#.....
    #.####.....
    .....###.##
    .....#.....
    .....#.....
    ...........
    .....#.....
    """

    agents_xy = np.random.randint(2, 4, (num_agents, 2)).tolist()
    targets_xy = np.random.randint(2, 4, (num_agents, 2)).tolist()

    grid_config = GridConfig(
        num_agents=num_agents,
        density=0.4,
        seed=1,
        max_episode_steps=128,
        obs_radius=3,
        map=grid,
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


def load_svg(svg_path):
    with open(svg_path, "r") as f:
        return f.read()


def update_div():
    svg_content = load_svg(SVG_FILE_PATH)
    div.text = svg_content


button_running_mapf = Button(label="MAPF RUN", button_type="success")
button_running_mapf.on_click(mapf)

button_load_mapf_svg = Button(label="Load SVG", button_type="success")
button_load_mapf_svg.on_click(update_div)

div = Div(text="", width=100, height=100)

layout = column(button_running_mapf, button_load_mapf_svg, div)
curdoc().add_root(layout)
