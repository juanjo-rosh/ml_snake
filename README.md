# ML Snake (UC3M)

Academic Snake project for Machine Learning classes at Universidad Carlos III de Madrid.  
It combines:
- a **PyGame Snake game**
- **feature logging to ARFF**
- **Weka model inference** for autonomous movement

## Repository contents

- `/tmp/workspace/juanjo-rosh/ml_snake/main_Assignment1.py`: main autonomous/ML-focused script.
- `/tmp/workspace/juanjo-rosh/ml_snake/Phase 3/agente.py`: keyboard/manual version (useful for data generation).
- `/tmp/workspace/juanjo-rosh/ml_snake/Phase 3/wekaI.py`: Python wrapper to load Weka models and predict.
- `/tmp/workspace/juanjo-rosh/ml_snake/data_train_keyboard.arff` and `/tmp/workspace/juanjo-rosh/ml_snake/data_test_keyboard.arff`: keyboard datasets.
- `/tmp/workspace/juanjo-rosh/ml_snake/Phase 2`, `/tmp/workspace/juanjo-rosh/ml_snake/Phase 3`, `/tmp/workspace/juanjo-rosh/ml_snake/Phase 4`: project phases with ARFF files, experiment outputs, and trained `.model` files.
- `/tmp/workspace/juanjo-rosh/ml_snake/Report-100499176-100499081.pdf`: project report.

## Requirements

1. **Python 3** (recommended 3.9+)
2. **Java JDK** (required by python-weka-wrapper/JVM)
3. Python packages:
   - `pygame`
   - `javabridge`
   - `python-weka-wrapper==0.3.0`

## Setup (recommended with virtual environment)

From `/tmp/workspace/juanjo-rosh/ml_snake`:

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
# .venv\Scripts\activate       # Windows PowerShell

pip install --upgrade pip
pip install pygame javabridge "python-weka-wrapper==0.3.0"
```

> Note: `javabridge` needs Java installed and available in your PATH (`java -version` should work).

## How to run

### 1) Manual/keyboard mode (recommended first run)

```bash
cd "/tmp/workspace/juanjo-rosh/ml_snake/Phase 3"
python agente.py
```

Controls:
- Arrow keys or `W/A/S/D`: move snake
- `ESC`: quit

This mode appends gameplay data to `data_test.arff` in the same folder.

### 2) ML/autonomous mode (Weka-based)

`main_Assignment1.py` depends on:
- `wekaI.py` from `Phase 3`
- model/data paths expected relative to current working directory (`./j48_goodmove.model`, `./data_train_goodmove.arff`)

A working command with current repository layout is:

```bash
cd "/tmp/workspace/juanjo-rosh/ml_snake/Phase 3/Goodmove"
PYTHONPATH="/tmp/workspace/juanjo-rosh/ml_snake:/tmp/workspace/juanjo-rosh/ml_snake/Phase 3" \
python "/tmp/workspace/juanjo-rosh/ml_snake/main_Assignment1.py"
```

## Project notes

- The codebase is academic/prototype-style and uses hardcoded relative paths in some places.
- There is no packaged dependency file (`requirements.txt`/`pyproject.toml`) in the repository.
- There are no automated lint/test scripts configured in the repository.
- `Phase 4` stores additional trained models and experimenter files for later project iterations.
