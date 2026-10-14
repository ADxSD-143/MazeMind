"""Evaluate the trained agent against a random-action baseline."""

from pathlib import Path

import numpy as np
from stable_baselines3 import PPO

from environment import MazeEnv


MODEL_PATH = Path("outputs/mazemind_ppo.zip")
RESULTS_PATH = Path("outputs/evaluation.npz")
EPISODES = 30


def run_episode(env, model=None):
    """Run one episode; model=None means choose random actions."""
    observation, _ = env.reset()
    total_reward = 0.0

    for steps in range(1, env.max_steps + 1):
        if model is None:
            action = env.action_space.sample()
        else:
            action, _ = model.predict(observation, deterministic=True)

        observation, reward, terminated, truncated, _ = env.step(action)
        total_reward += reward

        if terminated or truncated:
            return {
                "success": int(terminated),
                "steps": steps,
                "reward": total_reward,
            }

    return {"success": 0, "steps": env.max_steps, "reward": total_reward}


def main():
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Run python train.py before evaluation.")

    model = PPO.load(str(MODEL_PATH))
    env = MazeEnv()
    random_results = [run_episode(env) for _ in range(EPISODES)]
    ppo_results = [run_episode(env, model) for _ in range(EPISODES)]

    def report(label, results):
        success_rate = np.mean([item["success"] for item in results])
        mean_steps = np.mean([item["steps"] for item in results])
        mean_reward = np.mean([item["reward"] for item in results])
        print(
            f"{label}: success={success_rate:.1%}, "
            f"mean steps={mean_steps:.1f}, mean reward={mean_reward:.3f}"
        )

    report("Random baseline", random_results)
    report("PPO agent", ppo_results)

    RESULTS_PATH.parent.mkdir(exist_ok=True)
    np.savez(
        RESULTS_PATH,
        random_success=[x["success"] for x in random_results],
        random_steps=[x["steps"] for x in random_results],
        ppo_success=[x["success"] for x in ppo_results],
        ppo_steps=[x["steps"] for x in ppo_results],
    )
    print(f"Saved evaluation results to: {RESULTS_PATH}")
    env.close()


if __name__ == "__main__":
    main()
