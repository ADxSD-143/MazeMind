# 02 — Installation

## 1. Open the repository folder
If you cloned MazeMind from GitHub, open that folder in the terminal. Do not create a second nested MazeMind folder.

## 2. Create a virtual environment

    python -m venv .venv

Activate it:

Windows PowerShell:
    
    .venv\Scripts\Activate.ps1

Windows Command Prompt:

    .venv\Scripts\activate.bat

macOS/Linux:

    source .venv/bin/activate

A virtual environment isolates this project's packages from other projects.

## 3. Install packages

    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt

- **Gymnasium:** standard environment interface: observations, actions, rewards, reset and step.
- **Stable-Baselines3:** supplies the PPO algorithm.
- **NumPy:** grid and numerical data.
- **Matplotlib:** charts.
- **PyTorch:** installed as a dependency of Stable-Baselines3; no GPU setup is required.

## 4. Verify imports

    python -c "import gymnasium, stable_baselines3, numpy, matplotlib; print('All imports OK')"

Expected output:

    All imports OK

After creating environment.py, check its interface:

    python -c "from stable_baselines3.common.env_checker import check_env; from environment import MazeEnv; check_env(MazeEnv()); print('Environment OK')"

Expected output: Environment OK, without a checker exception.

## Troubleshooting
- **ModuleNotFoundError:** activate the virtual environment and reinstall requirements.
- **Python/package version conflict:** check supported versions in the official installation guide.
- **PowerShell activation error:** use Command Prompt or invoke .venv\Scripts\python.exe directly.
- **Slow install:** install packages before the bus ride.

## Official references
- [Python venv](https://docs.python.org/3/library/venv.html)
- [pip guide](https://pip.pypa.io/en/stable/user_guide/)
- [Stable-Baselines3 installation](https://stable-baselines3.readthedocs.io/en/master/guide/install.html)

## Video
- [Python virtual environments — YouTube search](https://www.youtube.com/results?search_query=python+venv+virtual+environment+windows+beginner)
- [Stable-Baselines3 installation — YouTube search](https://www.youtube.com/results?search_query=Stable+Baselines3+installation+PPO+tutorial)
