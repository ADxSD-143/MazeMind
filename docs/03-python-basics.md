# 03 — Python, NumPy aur Project ki Basic Maths

Is guide ka goal Python ki poori language sikhana nahi hai. Sirf wahi concepts cover kar rahe hain jo MazeMind ke code ko padhne ke liye zaroori hain.

## 1. Imports

```python
import numpy as np
from pathlib import Path
```

- `import numpy as np`: NumPy library import hoti hai; `np` uska short alias hai.
- `from pathlib import Path`: file/folder paths ko handle karne wali Python class import hoti hai.

Import ka matlab library ka code dobara likhna nahi; uski available functionality use karna.

## 2. Variables and types

```python
steps = 0
reward = -0.01
goal_reached = False
```

- `steps` integer hai.
- `reward` floating-point number hai.
- `goal_reached` Boolean hai: True ya False.

Variables naam ke containers jaise hain jahan program values rakhta hai.

## 3. Coordinates: tuple and zero-based indexing

```python
start = (0, 0)
goal = (4, 4)
```

Tuple do values ko ek saath rakhta hai. MazeMind mein pehli value row aur doosri column hai. Python indexing 0 se start hoti hai; isliye 5×5 grid ka last coordinate `(4, 4)` hai, `(5, 5)` nahi.

## 4. NumPy array: maze ka numeric form

```python
import numpy as np

walls = np.array([
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
], dtype=np.float32)
print(walls.shape)
print(walls[0, 2])
```

Expected output:

```text
(2, 5)
1.0
```

Array mein 2 rows aur 5 columns hain. `walls[0, 2]` first row, third column ko access karta hai. MazeMind mein `1` wall aur `0` free cell represent karta hai.

## 5. Shape and observation math

Environment teen 5×5 layers banata hai:
1. Wall layer.
2. Goal layer.
3. Agent-position layer.

Har layer mein 5 × 5 = 25 values. Total values:

```text
3 layers × 5 rows × 5 columns = 75 values
```

Code:

```python
stacked = np.stack([walls, goal_layer, agent_layer])
observation = stacked.flatten()
print(stacked.shape)
print(observation.shape)
```

Expected shapes:

```text
(3, 5, 5)
(75,)
```

`stack` arrays ko new dimension ke saath combine karta hai. `flatten` unko ek one-dimensional vector banata hai. Data order change hota hai, values remove nahi hoti.

## 6. Class and object

```python
class Counter:
    def __init__(self):
        self.steps = 0

counter = Counter()
print(counter.steps)
```

Expected output: `0`.

- Class blueprint hai.
- Object us blueprint se bana instance hai.
- `__init__` object create hone par initial setup karta hai.
- `self.steps` us object ka apna variable hai.

MazeMind mein `MazeEnv` class environment ka blueprint hai, aur `MazeEnv()` actual environment object banata hai.

## 7. Function, argument and return

```python
def add_one(value):
    return value + 1

answer = add_one(2)
print(answer)
```

Expected output: `3`.

Function input leta hai, operation karta hai aur `return` se result deta hai. Gymnasium ka `step(action)` bhi function hai, lekin woh ek saath 5 values return karta hai.

## 8. Dictionary se actions map karna

```python
moves = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1),
}
print(moves[1])
```

Output: `(0, 1)`. Action 1 means right: row unchanged, column one increase.

## 9. Conditions and bounds

```python
inside_grid = 0 <= next_row < 5 and 0 <= next_col < 5
```

Condition tab True hoti hai jab row aur column dono 0 se 4 ke beech hon. Array index karne se pehle bounds check karna zaroori hai, warna invalid index error ya wrong movement ho sakti hai.

## 10. Mean and success rate ki maths

Maan lo 5 test episodes mein success values hain:

```text
[1, 0, 1, 1, 0]
```

Yahan 1 success aur 0 failure hai. Success rate:

```text
success rate = successful episodes / total episodes
             = 3 / 5
             = 0.60 = 60%
```

Agar steps `[8, 12, 10]` hon, mean steps:

```text
(8 + 12 + 10) / 3 = 10
```

Python/NumPy mein `np.mean([1, 0, 1, 1, 0])` returns `0.6`.

## 11. File paths

```python
from pathlib import Path

output_dir = Path("outputs")
model_path = output_dir / "mazemind_ppo"
```

`Path` file paths ko readable aur OS-compatible way mein build karta hai. `model_path` ka base path `outputs/mazemind_ppo` hai; Stable-Baselines3 save karte waqt `.zip` extension add karta hai.

## Official references

- [Python tutorial](https://docs.python.org/3/tutorial/)
- [Python classes](https://docs.python.org/3/tutorial/classes.html)
- [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html)
- [NumPy stack](https://numpy.org/doc/stable/reference/generated/numpy.stack.html)
- [NumPy mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html)

Videos: [Python basics](https://www.youtube.com/results?search_query=python+variables+functions+classes+beginner), [NumPy array shapes](https://www.youtube.com/results?search_query=numpy+array+shape+stack+flatten+beginner).

## Self-check

1. Why is `(4, 4)` last cell of a 5×5 grid?
2. Why are 75 values in the observation?
3. `step()` return values ko ek variable mein kyun nahi rakhte?
4. 12 successes out of 30 ka success rate kya hoga?
