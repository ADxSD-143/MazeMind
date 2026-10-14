# 04 — The maze environment

File: environment.py

An environment is the world an agent interacts with. The agent chooses an action; the environment updates its state and returns an observation, reward, and episode-ending flags.

## Grid and coordinates
- 0 = free cell; 1 = wall.
- Start = (0, 0); goal = (4, 4).
- Coordinates are (row, column), not (x, y).

## Actions

Discrete(4) means the agent chooses one integer:

| Action | Movement |
|---:|---|
| 0 | Up: (-1, 0) |
| 1 | Right: (0, +1) |
| 2 | Down: (+1, 0) |
| 3 | Left: (0, -1) |

If a move leaves the grid or enters a wall, the agent stays in place but spends a step.

## Observation

The observation contains three 5×5 layers: walls, goal, and current agent position. They are stacked and flattened into 75 numbers between 0 and 1.

The wall and goal layout is fixed, but the agent position changes every step, so the policy needs the position too.

## Rewards
- Ordinary step: -0.01.
- Reach goal: +1.0.
- Goal ends the episode with terminated=True.
- Reaching the 50-step limit ends it with truncated=True.

The small step penalty encourages shorter routes but does not guarantee fast learning.

## Gymnasium API

reset() starts a new episode and returns (observation, info).

step(action) returns:

    observation, reward, terminated, truncated, info

- observation: what the agent sees next.
- reward: feedback for the action.
- terminated: task ended by reaching the goal.
- truncated: step limit ended the episode.
- info: optional extra data; currently empty.

## Try it

    from environment import MazeEnv

    env = MazeEnv()
    observation, info = env.reset(seed=42)
    print(observation.shape)
    print(env.render())

Expected first line:

    (75,)

The maze text uses A for agent, G for goal, # for walls, and . for free cells.

## Validate the environment

    from stable_baselines3.common.env_checker import check_env
    from environment import MazeEnv

    check_env(MazeEnv())
    print("Environment OK")

The checker catches common API and shape problems before training.

## Official references
- [Gymnasium environment creation](https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/)
- [Gymnasium Env API](https://gymnasium.farama.org/api/env/)
- [Gymnasium spaces](https://gymnasium.farama.org/api/spaces/)
- [SB3 custom environments](https://stable-baselines3.readthedocs.io/en/master/guide/custom_env.html)

## Video
- [Create a custom Gymnasium environment — YouTube search](https://www.youtube.com/results?search_query=Gymnasium+custom+environment+tutorial)
