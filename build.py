#!/usr/bin/env python3

import subprocess
import os
import sys

compiler = "g++"
build_dir = "build"
executable = os.path.join(build_dir, "test_executable")
source_files = [
    "src/math_functions.cpp",
    "tests/test.cpp"
]
compile_flags = ["-std=c++17"]

# Build folder exists
os.makedirs(build_dir, exist_ok=True)

def compile():
    print("Compiling...")
    cmd = [compiler] + compile_flags + source_files + ["-o", executable]
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print("Compilation failed!")
        sys.exit(1)
    print("Compilation succeeded!")

def run_tests():
    print("Running tests...")
    result = subprocess.run([executable])
    if result.returncode != 0:
        print("Tests failed!")
        sys.exit(1)
    else:
        print("All tests passed!")

if __name__ == "__main__":
    compile()
    run_tests()
