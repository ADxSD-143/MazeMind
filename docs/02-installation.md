# 02 — PyCharm Setup and Installation (Windows)

Is guide ko PyCharm ke saath follow karo. Commands ko **ek-ek karke** run karna. Ek command ka output check kiye bina next command par jump mat karo.

## 1. GitHub se project lo

Repository: https://github.com/ADxSD-143/MazeMind

Agar Git use karna aata hai, terminal mein:

```bash
git clone https://github.com/ADxSD-143/MazeMind.git
cd MazeMind
```

- `git clone`: GitHub repository ki local copy banata hai.
- `cd MazeMind`: terminal ko project directory mein le jaata hai.

Agar Git use nahi karna, GitHub page par **Code → Download ZIP** use kar sakte ho, phir ZIP extract karke folder PyCharm mein open karo.

## 2. PyCharm mein folder open karo

1. PyCharm start karo.
2. **File → Open** select karo.
3. Jo `MazeMind` folder download/clone kiya hai, wahi select karo.
4. Ensure karo ki `requirements.txt`, `environment.py`, `train.py` aur `docs` project root mein dikh rahe hain. Ek extra nested `MazeMind/MazeMind` folder accidentally open mat karna.

## 3. Python interpreter / virtual environment

PyCharm mein **Settings → Project → Python Interpreter** (version ke hisaab se menu wording thodi different ho sakti hai) open karo.

Agar interpreter nahi hai:
- **Add Interpreter → Add Local Interpreter → Virtualenv** choose karo.
- Base Python 3.11 choose kar sakte ho, provided dependencies us version ko support karti hain.
- Environment ka folder project ke andar `.venv` ho sakta hai.

Virtual environment ka purpose: MazeMind ki packages ko doosre Python projects se alag rakhna. Isse project dependency conflicts kam hote hain.

## 4. PyCharm Terminal open karo

PyCharm ke bottom panel mein **Terminal** open karo. Current folder project root hona chahiye. Check:

```powershell
dir
```

Output mein `requirements.txt` aur `environment.py` dikhne chahiye. Agar nahi, terminal galat folder mein ho sakta hai.

## 5. Virtual environment create/activate (agar pehle se configured nahi)

PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Command Prompt use kar rahe ho to activation command:

```bat
.venv\Scripts\activate.bat
```

Agar PyCharm ne pehle hi `.venv` create aur select kiya hai, dobara create karne ki zaroorat nahi. Activation ke baad terminal prompt ke start mein aksar `(.venv)` dikh sakta hai.

PowerShell activation policy error de to project interpreter ko PyCharm se select karo ya Terminal dropdown se Command Prompt use karo. Security policy ko blindly disable mat karo.

## 6. Packages install karo

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Har part ka meaning:
- `python -m pip`: isi Python interpreter ka package installer run karo.
- `install`: packages download/install karo.
- `-r requirements.txt`: file se package list read karo.
- `--upgrade pip`: package installer update karne ki koshish karta hai.

Is project ki main libraries:
- **Gymnasium:** RL environment ka standard interface.
- **Stable-Baselines3:** PPO algorithm ki ready implementation.
- **NumPy:** maze aur numerical arrays.
- **Matplotlib:** evaluation charts.
- **PyTorch:** Stable-Baselines3 ki dependency; hum directly neural network code nahi likh rahe.

Install mein internet aur kuch minutes lag sakte hain. GPU configure karna required nahi.

## 7. Installation verify karo

```bash
python -c "import gymnasium, stable_baselines3, numpy, matplotlib; print('All imports OK')"
```

Expected output:

```text
All imports OK
```

Agar `ModuleNotFoundError` aata hai, likely packages selected interpreter mein install nahi hue. PyCharm interpreter aur terminal Python ko match karo, phir install command dobara chalao.

## 8. Environment checker

Code training se pehle Gymnasium interface validate karega:

```bash
python -c "from stable_baselines3.common.env_checker import check_env; from environment import MazeEnv; check_env(MazeEnv()); print('Environment OK')"
```

Expected final message:

```text
Environment OK
```

Checker warnings de sakta hai; agar exception/error aaye, uska complete traceback save karo aur training shuru mat karo. Checker ka purpose common interface mistakes ko early catch karna hai.

## 9. Run order

```bash
python train.py
python evaluate.py
python visualize.py
```

- Pehle `train.py`: trained model generate hota hai.
- Phir `evaluate.py`: saved model ko random actions se compare karta hai.
- Last `visualize.py`: saved evaluation numbers ka chart banata hai.

Output paths aur error troubleshooting [06 — Training and evaluation](06-training-and-evaluation.md) mein hain.

## 10. Common install issues

| Error/symptom | Kya check karna hai |
|---|---|
| `python is not recognized` | Python installation/PATH; Windows par `py --version` try karo. |
| `ModuleNotFoundError` | Correct PyCharm interpreter select hai? Usi terminal mein pip install hua? |
| `pip install` fails | Full error, Python version aur network/package compatibility check karo. |
| PowerShell activation blocked | PyCharm interpreter select karo ya Command Prompt use karo; policy blindly disable mat karo. |
| Packages install hue, imports fail | Terminal ka `python` aur PyCharm interpreter mismatch ho sakte hain. |
| Training slow | CPU par training expected hai; process ko complete hone do. |

## Official documentation

- [PyCharm: Configure Python interpreter](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)
- [Python virtual environments](https://docs.python.org/3/library/venv.html)
- [pip user guide](https://pip.pypa.io/en/stable/user_guide/)
- [Stable-Baselines3 installation](https://stable-baselines3.readthedocs.io/en/master/guide/install.html)

Videos:
- [PyCharm Python interpreter and virtualenv](https://www.youtube.com/results?search_query=PyCharm+configure+Python+interpreter+virtualenv+Windows)
- [pip install requirements.txt](https://www.youtube.com/results?search_query=python+pip+install+requirements.txt+beginner)
