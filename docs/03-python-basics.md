# 03 — Python and NumPy concepts

You do not need to understand the libraries' internal implementation. Understand what each project line does.

## Imports

    import numpy as np

This imports NumPy and uses the conventional short name np.

## Tuples for coordinates

    start = (0, 0)
    goal = (4, 4)

A tuple groups values. Here, the first number is the row and the second is the column. Python indexing starts at zero, so (0, 0) is the top-left cell.

## NumPy arrays

    walls = np.zeros((5, 5), dtype=np.float32)
    walls[1, 2] = 1.0

This creates a 5-by-5 array of zeros and marks row 1, column 2 as a wall. In this project, 1 means wall and 0 means free cell. The shape is (5, 5).

We use float32 because the observation space declares that type; keeping types consistent avoids interface errors.

## Classes and objects

    class MazeEnv:
        def __init__(self):
            self.steps = 0

A class defines a type of object. __init__ runs when an object is created. self.steps stores data belonging to that object.

    env = MazeEnv()

This creates an object. MazeEnv inherits Gymnasium's environment interface.

## Conditions

    inside_grid = 0 <= row < 5 and 0 <= col < 5

This is true only when both coordinates are in range. Check bounds before indexing the array.

## Functions and return values

    def add_one(value):
        return value + 1

    print(add_one(2))

Output:

    3

A function accepts inputs and returns a result. Gymnasium's step() returns five values that the RL library uses.

## Stack and flatten

The observation contains three 5×5 layers: walls, goal, and agent position.

    stacked = np.stack([walls, goal_layer, agent_layer])
    observation = stacked.flatten()

The stacked shape is (3, 5, 5). Flattening turns it into a 75-value vector without removing information.

## References
- [Python tutorial](https://docs.python.org/3/tutorial/)
- [Python classes](https://docs.python.org/3/tutorial/classes.html)
- [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html)
- [NumPy stack](https://numpy.org/doc/stable/reference/generated/numpy.stack.html)

## Video
- [Python classes, functions and tuples — YouTube search](https://www.youtube.com/results?search_query=python+functions+classes+tuples+beginner)
- [NumPy stack and flatten — YouTube search](https://www.youtube.com/results?search_query=numpy+stack+flatten+reshape+tutorial)

## Checkpoint
What does (4, 4) represent? Why check bounds before indexing walls? Why is the observation length 75?
