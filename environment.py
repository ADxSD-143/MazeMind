"""A small, fixed maze environment for learning reinforcement learning."""

import gymnasium as gym
import numpy as np
from gymnasium import spaces


class MazeEnv(gym.Env):
    """Navigate a 5x5 grid from start to goal."""

    def __init__(self, max_steps=50):
        super().__init__()
        self.rows = 5
        self.cols = 5
        self.max_steps = max_steps

        # 1 means wall; 0 means walkable.
        self.walls = np.array(
            [
                [0, 0, 1, 0, 0],
                [1, 0, 1, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [1, 0, 0, 0, 0],
            ],
            dtype=np.float32,
        )

        self.start = (0, 0)
        self.goal = (4, 4)
        self.agent = self.start
        self.steps = 0

        # Actions: 0=up, 1=right, 2=down, 3=left.
        self.action_space = spaces.Discrete(4)

        # Three layers: walls, goal, and agent position.
        # Flattened to 75 values for PPO's MlpPolicy.
        self.observation_space = spaces.Box(
            low=0.0,
            high=1.0,
            shape=(3 * self.rows * self.cols,),
            dtype=np.float32,
        )

        self.goal_layer = np.zeros((self.rows, self.cols), dtype=np.float32)
        self.goal_layer[self.goal] = 1.0
        self.moves = {
            0: (-1, 0),
            1: (0, 1),
            2: (1, 0),
            3: (0, -1),
        }

    def _get_obs(self):
        """Encode the maze, goal, and current agent position."""
        agent_layer = np.zeros_like(self.walls)
        agent_layer[self.agent] = 1.0
        stacked = np.stack([self.walls, self.goal_layer, agent_layer])
        return stacked.flatten().astype(np.float32)

    def reset(self, seed=None, options=None):
        """Start a new episode and return observation and info."""
        super().reset(seed=seed)
        self.agent = self.start
        self.steps = 0
        return self._get_obs(), {}

    def step(self, action):
        """Apply one action and return Gymnasium's five required values."""
        dr, dc = self.moves[int(action)]
        row, col = self.agent
        next_row, next_col = row + dr, col + dc
        self.steps += 1
        reward = -0.01

        inside_grid = (
            0 <= next_row < self.rows and 0 <= next_col < self.cols
        )
        if inside_grid and self.walls[next_row, next_col] == 0:
            self.agent = (next_row, next_col)

        terminated = self.agent == self.goal
        if terminated:
            reward = 1.0

        truncated = self.steps >= self.max_steps and not terminated
        return self._get_obs(), reward, terminated, truncated, {}

    def render(self):
        """Return a text maze: A=agent, G=goal, #=wall, .=free cell."""
        grid = np.full((self.rows, self.cols), ".", dtype="<U1")
        grid[self.walls == 1] = "#"
        grid[self.goal] = "G"
        grid[self.agent] = "A"
        return "\n".join(" ".join(row) for row in grid)
