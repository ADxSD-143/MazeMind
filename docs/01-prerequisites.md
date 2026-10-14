# 01 — Prerequisites: kya aana chahiye?

Is project ke liye advanced maths, deep learning ka prior experience ya GPU ki zaroorat nahi. Basic Python aur step-by-step practice enough hai.

## 1. Software requirements

- Python version jo installed Stable-Baselines3/PyTorch packages support karte hon. Python 3.11 ek sensible starting choice hai.
- PyCharm ya another Python IDE.
- Internet, initial package installation ke liye.
- Git/GitHub useful hai, lekin project code samajhne ke liye Git expert hona zaroori nahi.
- GPU required nahi. Training local CPU par chal sakti hai.

## 2. Python concepts jo project use karta hai

| Concept | Meaning | Project example |
|---|---|---|
| Variable | Value store karna | `self.steps = 0` |
| Integer/float | Numeric types | `50`, `-0.01`, `1.0` |
| Tuple | Fixed grouped values | `(0, 0)` coordinate |
| List | Ordered collection | Maze ki rows |
| Dictionary | Key se value lookup | Action number → movement |
| Condition | Decision/true-false check | Cell grid ke andar hai? |
| Function | Reusable instructions | `reset()`, `step()` |
| Class | Objects ka blueprint | `MazeEnv` |
| Object | Class se bana instance | `MazeEnv()` |
| Import | Library/code use karna | `import numpy as np` |
| NumPy array | Numeric grid/data | 5×5 maze |
| Return | Function ka result | `return observation, reward, ...` |
| Exception | Error signal | `FileNotFoundError` |

Har concept ko pehle master karne ki zaroorat nahi. Jab guide mein aaye, uska example run karo.

## 3. NumPy kya karta hai?

NumPy Python library hai jo numeric arrays banane aur un par operations karne mein help karti hai. Maze ko 5×5 numeric array mein store karne ke liye use hoti hai.

```python
import numpy as np

grid = np.zeros((5, 5), dtype=np.float32)
grid[1, 2] = 1.0
print(grid.shape)
print(grid[1, 2])
```

Expected output:

```text
(5, 5)
1.0
```

`zeros((5, 5))` 5 rows aur 5 columns ka array banata hai. `grid[1, 2]` row 1, column 2 ko access karta hai. Python index zero se start hota hai.

## 4. Reinforcement Learning ki minimum understanding

Tumhe abhi algorithm derive karna nahi hai. Bas ye samjho:
- Agent action leta hai.
- Environment next observation aur reward deta hai.
- Algorithm reward signal se policy improve karne ki koshish karta hai.
- Evaluation batata hai ki learned policy kaam kar rahi hai ya nahi.

Detailed definitions [05 — RL and PPO](05-reinforcement-learning.md) mein hain.

## 5. Python version check

PyCharm Terminal mein:

```bash
python --version
python -m pip --version
```

Example output (exact versions different ho sakte hain):

```text
Python 3.11.x
pip 24.x
```

Agar `python` command nahi chalti, Windows par `py --version` try karo. Project ko run karte waqt ensure karo ki PyCharm ka selected interpreter hi use ho raha ho.

## 6. Pehle kya padhna hai, aur kya skip kar sakte ho?

**Must understand at beginner level:** variables, functions, classes, tuples, dictionaries, conditions, imports, NumPy arrays, shapes, function return values.

**Abhi deeply padhne ki zaroorat nahi:** neural network backpropagation implementation, PPO ka full derivation, GPU programming, cloud deployment, databases, web frameworks. Ye project unki demand nahi karta.

## Official references

- [Python tutorial](https://docs.python.org/3/tutorial/)
- [Python classes](https://docs.python.org/3/tutorial/classes.html)
- [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html)
- [NumPy array indexing](https://numpy.org/doc/stable/user/basics.indexing.html)

## Beginner video searches

- [Python functions, classes and objects](https://www.youtube.com/results?search_query=python+functions+classes+objects+beginner+tutorial)
- [NumPy arrays and indexing](https://www.youtube.com/results?search_query=numpy+arrays+indexing+beginner+tutorial)
- [Python dictionaries and tuples](https://www.youtube.com/results?search_query=python+tuples+dictionaries+beginner+tutorial)

## Self-check

Apne words mein explain karo:
1. Variable aur function mein difference?
2. `(4, 4)` maze mein kya represent karta hai?
3. NumPy array kyun use kar rahe hain?
4. Agent aur environment alag kyun hain?
