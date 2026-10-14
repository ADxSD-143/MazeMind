"""Plot success rates and episode lengths from evaluate.py."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


RESULTS_PATH = Path("outputs/evaluation.npz")
PLOT_PATH = Path("outputs/evaluation.png")


def main():
    if not RESULTS_PATH.exists():
        raise FileNotFoundError("Run python evaluate.py before plotting.")

    data = np.load(RESULTS_PATH)
    labels = ["Random baseline", "PPO agent"]
    success_rates = [
        np.mean(data["random_success"]),
        np.mean(data["ppo_success"]),
    ]
    mean_steps = [
        np.mean(data["random_steps"]),
        np.mean(data["ppo_steps"]),
    ]

    fig, axes = plt.subplots(1, 2, figsize=(9, 4))
    axes[0].bar(labels, success_rates)
    axes[0].set_ylim(0, 1)
    axes[0].set_ylabel("Success rate")
    axes[0].set_title("Goal reached")

    axes[1].bar(labels, mean_steps)
    axes[1].set_ylabel("Mean steps per episode")
    axes[1].set_title("Episode length")

    fig.tight_layout()
    PLOT_PATH.parent.mkdir(exist_ok=True)
    fig.savefig(PLOT_PATH, dpi=150)
    print(f"Saved plot to: {PLOT_PATH}")
    plt.show()


if __name__ == "__main__":
    main()
