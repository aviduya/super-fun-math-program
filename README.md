# C++ Auto Builder (with Python + Watchfiles)

This tool automatically runs a build script (like `build.py`) whenever you modify your C++ source files (`.cpp`, `.h`). Works cross-platform (macOS, Linux, Windows) using a Python-based file watcher.

---

## Requirements

- Python 3.9+
- [watchfiles](https://pypi.org/project/watchfiles/)

---

## Setup

1. **Clone this repo**

```bash
git clone https://github.com/aviduya/super-fun-math-program.git
cd super-fun-math-program
```

2. **Create a virtual environment (optional but recommended)**

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows (cmd)
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install watchfiles
```

4. **Run the watcher**

```bash
python cpp_auto_build.py
```

---

## Options

You can pass custom arguments to the script:

```bash
python cpp_auto_build.py \
  --src src \
  --script build.py \
  --debounce 500
```

- `--src` – Directory to watch (default: `src`)
- `--script` – Python script to run on file change (default: `build.py`)
- `--debounce` – Delay between change detection and running (in milliseconds)

---

## Example Build Script (`build.py`)

```python
import os
import subprocess

print("🔨 Building...")

# Example: g++ compile command
subprocess.run(["g++", "-o", "main", "src/main.cpp"])

# Example: run tests or the built binary
subprocess.run(["./main"])
```

---

## Stop Program

Just hit `Ctrl+C` in the terminal.

---

## Windows Notes

- Use `python` instead of `python3`
- Use `venv\Scripts\activate` for activating virtual environments
