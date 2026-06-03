# ML Snake (UC3M)

Academic Snake project for Machine Learning classes at Universidad Carlos III de Madrid.  
It combines:
- a **PyGame Snake game**
- **feature logging to ARFF**
- **Weka model inference** for autonomous movement

## Repository contents

- `./main_Assignment1.py`: main autonomous/ML-focused script.
- `./Assignment 2 - Phase 2` and `./Assignment 2 - Phase 3`: Assignment 2 implementation files (Q-learning Snake environment and training scripts).
- `./Assignment2-100499081-100499176.pdf`: Assignment 2 report/documentation.
- `./Phase 3/agente.py`: keyboard/manual version (useful for data generation).
- `./Phase 3/wekaI.py`: Python wrapper to load Weka models and predict.
- `./data_train_keyboard.arff` and `./data_test_keyboard.arff`: keyboard datasets.
- `./Phase 2`, `./Phase 3`, `./Phase 4`: project phases with ARFF files, experiment outputs, and trained `.model` files.
- `./Report-100499176-100499081.pdf`: project report.

## Requirements

1. **Python 3** (recommended 3.9+)
2. **Java JDK** (required by python-weka-wrapper/JVM)
3. Python packages:
   - `pygame`
   - `javabridge`
   - `python-weka-wrapper==0.3.0`

## Setup (recommended with virtual environment)

From the repository root:

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
cd "Phase 3"
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
cd "Phase 3/Goodmove"
PYTHONPATH="../..:.." \
python ../../main_Assignment1.py
```

## Project notes

- The codebase is academic/prototype-style and uses hardcoded relative paths in some places.
- There is no packaged dependency file (`requirements.txt`/`pyproject.toml`) in the repository.
- There are no automated lint/test scripts configured in the repository.
- `Phase 4` stores additional trained models and experimenter files for later project iterations.
