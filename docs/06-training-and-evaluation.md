# 06 — Training, evaluation, and plots

Run commands from the repository root with the virtual environment active.

## 1. Validate the environment

    python -c "from stable_baselines3.common.env_checker import check_env; from environment import MazeEnv; check_env(MazeEnv()); print('Environment OK')"

Expected: Environment OK.

## 2. Train PPO

    python train.py

The script checks the environment, wraps it in Monitor, trains PPO for 20,000 timesteps, and saves the model.

Expected final message:

    Saved model to: outputs/mazemind_ppo.zip

Logs and actual results vary. Saving a model does not prove that it learned.

## 3. Evaluate

    python evaluate.py

The script runs 30 episodes for the random baseline and 30 for PPO. It reports:
- **Success rate:** fraction of episodes reaching the goal.
- **Mean steps:** average steps before the episode ended.
- **Mean reward:** average sum of rewards.

Output format (illustrative only):

    Random baseline: success=..., mean steps=..., mean reward=...
    PPO agent: success=..., mean steps=..., mean reward=...
    Saved evaluation results to: outputs/evaluation.npz

Record your actual results; do not present illustrative numbers as real.

## 4. Plot

    python visualize.py

This creates outputs/evaluation.png and opens a Matplotlib window. The charts compare success rate and mean steps.

## Interpret results
- Higher success rate is better.
- Fewer steps is useful only alongside success rate; a model that fails quickly can look deceptively efficient.
- One run is weak evidence. Repeating with several seeds is optional for this small MVP.
- If PPO does not beat random, report it honestly.

## Common errors
- Model not found: run train.py first.
- Evaluation file not found: run evaluate.py first.
- No plot window: inspect outputs/evaluation.png.
- Low success rate: check maze reachability, reward, observation, and action mapping. More training is not always the only fix.
- Environment checker errors: compare reset() and step() to the Gymnasium API.

## Official references
- [SB3 PPO](https://stable-baselines3.readthedocs.io/en/master/modules/ppo.html)
- [SB3 Monitor](https://stable-baselines3.readthedocs.io/en/master/common/monitor.html)
- [SB3 environment checker](https://stable-baselines3.readthedocs.io/en/master/common/env_checker.html)
- [Matplotlib quick start](https://matplotlib.org/stable/users/explain/quick_start.html)
- [NumPy savez](https://numpy.org/doc/stable/reference/generated/numpy.savez.html)

## Video
- [RL agent evaluation — YouTube search](https://www.youtube.com/results?search_query=reinforcement+learning+agent+evaluation+success+rate)
- [Matplotlib bar charts — YouTube search](https://www.youtube.com/results?search_query=matplotlib+bar+chart+beginner+tutorial)
