# MazeMind 🧩

A small reinforcement-learning project where a PPO agent learns to navigate one fixed 5×5 maze.

**Goal:** learn the RL workflow, custom environment design, training, and evaluation—not build a production robot.

## What it does
- Defines a maze with Gymnasium.
- Trains a PPO agent with Stable-Baselines3.
- Compares PPO with a random-action baseline.
- Measures success rate and episode length, then plots results.

**Scope:** one fixed maze, one PPO model, and a small experiment. No web app, paid API, or pretrained model. Results vary; training is not guaranteed to solve the maze.

## Architecture

    Maze grid → Gymnasium MazeEnv → PPO training
              → Evaluate PPO vs random actions
              → Metrics and Matplotlib plots

## Project structure

    MazeMind/
    ├── README.md
    ├── requirements.txt
    ├── environment.py
    ├── train.py
    ├── evaluate.py
    ├── visualize.py
    └── docs/
        ├── 01-prerequisites.md
        ├── 02-installation.md
        ├── 03-python-basics.md
        ├── 04-maze-environment.md
        ├── 05-reinforcement-learning.md
        ├── 06-training-and-evaluation.md
        └── 07-resources.md

## Prerequisites
- Python 3.10+; use a version supported by current Stable-Baselines3/PyTorch packages.
- Basic Python: variables, functions, classes, tuples, imports, and NumPy arrays.
- Internet for initial package installation. Training runs locally.
- No GPU required.

## Quick start

Create a virtual environment:

    python -m venv .venv

Windows PowerShell:

    .venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt

macOS/Linux:

    source .venv/bin/activate
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt

Check the environment:

    python -c "from stable_baselines3.common.env_checker import check_env; from environment import MazeEnv; check_env(MazeEnv()); print('Environment OK')"

Expected output: Environment OK, with no checker exception.

Train, evaluate, and plot:

    python train.py
    python evaluate.py
    python visualize.py

Outputs are saved in outputs/. Do not expect a particular success rate before running the experiment.

## Read the guides in order
1. [Prerequisites](docs/01-prerequisites.md)
2. [Installation](docs/02-installation.md)
3. [Python concepts used](docs/03-python-basics.md)
4. [Maze environment](docs/04-maze-environment.md)
5. [Reinforcement learning and PPO](docs/05-reinforcement-learning.md)
6. [Training and evaluation](docs/06-training-and-evaluation.md)
7. [References and videos](docs/07-resources.md)

## Limitations
- The maze layout is fixed; unseen-maze generalization is not tested.
- A saved model does not prove that it learned.
- The random baseline may occasionally reach the goal.
- Report actual results honestly; this is a learning prototype, not a benchmark.

## License
Choose a license before accepting outside contributions or reuse.