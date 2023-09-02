import numpy as np
from bokeh.layouts import column
from bokeh.models import Button
from bokeh.plotting import curdoc

from pogema import GridConfig, pogema_v0
from pogema.animation import AnimationMonitor


def mapf(file_path="mapf_button.svg", num_agents=2):
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


button = Button(label="MAPF RUN", button_type="success")
button.on_click(mapf)

layout = column(button)
curdoc().add_root(layout)
