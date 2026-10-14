# 01 — Prerequisites

You do not need advanced mathematics, a GPU, or deep learning experience.

## Software
- Python 3.10+; choose a version supported by the current Stable-Baselines3 and PyTorch releases.
- VS Code or PyCharm.
- Terminal/PowerShell.
- Internet for initial installation.
- Git and GitHub are useful for version control.

## Python concepts used

| Concept | How the project uses it | Example |
|---|---|---|
| Variable | Stores values | steps = 0 |
| Function | Groups instructions | reset() |
| Class/object | Represents the environment | env = MazeEnv() |
| Tuple | Stores row/column | start = (0, 0) |
| Dictionary | Maps actions to movement | 1 maps to right |
| Import | Uses a library | import numpy as np |
| NumPy array | Stores the grid | np.zeros((5, 5)) |
| Condition | Checks walls and bounds | if inside_grid |

Learn missing concepts as they appear; do not wait to master all Python before starting.

## Check installation

    python --version
    python -m pip --version

Example output (versions will differ):

    Python 3.11.x
    pip 24.x

If Windows does not recognize python, try py --version.

## Official references
- [Python tutorial](https://docs.python.org/3/tutorial/)
- [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html)
- [Gymnasium environment creation](https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/)

## Videos
- [Python classes and objects — YouTube search](https://www.youtube.com/results?search_query=python+classes+objects+beginner+tutorial)
- [NumPy arrays — YouTube search](https://www.youtube.com/results?search_query=numpy+arrays+beginner+tutorial)

## Checkpoint
Explain what a variable, function, class, tuple, and NumPy array are in your own words.
