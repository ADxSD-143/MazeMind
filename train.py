"""Train PPO on MazeEnv and save the trained policy."""

from pathlib import Path

from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.monitor import Monitor

from environment import MazeEnv


OUTPUT_DIR = Path("outputs")
MODEL_PATH = OUTPUT_DIR / "mazemind_ppo"


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    check_env(MazeEnv())

    env = Monitor(MazeEnv(), filename=str(OUTPUT_DIR / "training_monitor.csv"))
    model = PPO(
        "MlpPolicy",
        env,
        learning_rate=0.0003,
        n_steps=256,
        batch_size=64,
        gamma=0.99,
        verbose=1,
        seed=42,
    )

    # Small starting budget for this learning demo.
    model.learn(total_timesteps=20_000)
    model.save(str(MODEL_PATH))
    env.close()
    print(f"Saved model to: {MODEL_PATH}.zip")


if __name__ == "__main__":
    main()
