# 05 — Reinforcement learning and PPO

## The idea

In supervised learning, models usually learn from examples with known answers. In reinforcement learning (RL), an agent interacts with an environment and receives rewards. It tries to learn actions that increase long-term reward.

    Observe maze → choose move → receive reward
          ↑                         ↓
          └──── next observation ───┘

- **Agent:** the PPO policy being trained.
- **Environment:** MazeEnv.
- **Observation:** the 75-number vector describing walls, goal, and agent position.
- **Action:** up, right, down, or left.
- **Reward:** -0.01 per ordinary step and +1 at the goal.
- **Episode:** one attempt, ending at the goal or step limit.
- **Policy:** the learned rule for choosing actions from observations.

## Why PPO?

PPO means Proximal Policy Optimization. It is a policy-gradient RL algorithm. Stable-Baselines3 provides its implementation, so this project focuses on environment design, experiment setup, and evaluation rather than reimplementing the algorithm.

PPO("MlpPolicy", env, ...) uses a neural network with fully connected layers to process the flat observation vector. PPO is not tabular Q-learning.

## Training settings

| Setting | Meaning |
|---|---|
| learning_rate=0.0003 | Size of optimizer updates |
| n_steps=256 | Steps collected before a PPO update |
| batch_size=64 | Samples per minibatch |
| gamma=0.99 | Importance of future rewards |
| total_timesteps=20,000 | Training interaction budget |
| seed=42 | Helps repeat the run |

These are starting values, not guaranteed optimal settings.

## Why compare a random baseline?

A trained model needs a reference point. The random baseline chooses actions randomly. If PPO does not outperform it, investigate observations, rewards, training, and maze reachability rather than claiming success.

## Limitations

We train on one fixed maze. This does not prove that the policy can solve unseen maze layouts.

## Official references
- [Stable-Baselines3 PPO](https://stable-baselines3.readthedocs.io/en/master/modules/ppo.html)
- [SB3 quickstart](https://stable-baselines3.readthedocs.io/en/master/guide/quickstart.html)
- [Spinning Up: PPO explanation](https://spinningup.openai.com/en/latest/algorithms/ppo.html)
- [Hugging Face Deep RL course](https://huggingface.co/learn/deep-rl-course/unit0/introduction)

## Video
- [PPO explained — YouTube search](https://www.youtube.com/results?search_query=PPO+reinforcement+learning+explained+beginner)
- [SB3 PPO and Gymnasium — YouTube search](https://www.youtube.com/results?search_query=Stable+Baselines3+PPO+Gymnasium+tutorial)

## Checkpoint
Explain the difference between agent, environment, observation, action, reward, and episode. Why compare PPO with random actions?
