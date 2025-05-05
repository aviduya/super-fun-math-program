#!/usr/bin/env python3

import argparse
from watchfiles import run_process

def main():
    parser = argparse.ArgumentParser(
        description="Watch C++ source files and run a build script on change."
    )
    parser.add_argument(
        "--src", "-s",
        type=str,
        default="src",
        help="Directory to watch for .cpp and .h changes (default: ./src)"
    )
    parser.add_argument(
        "--script", "-b",
        type=str,
        default="build.py",
        help="Build script to run (default: build.py)"
    )
    parser.add_argument(
        "--debounce", "-d",
        type=int,
        default=300,
        help="Debounce time in milliseconds (default: 300ms)"
    )

    args = parser.parse_args()

    print(f"Watching '{args.src}' for .cpp and .h changes...")
    print(f"Will run: python3 {args.script}")
    print(f"Debounce delay: {args.debounce}ms\n")

    run_process(
       args.src,
       target=f"python3 {args.script}",
       target_type='command',
       watch_filter=lambda change, f: f.endswith(('.cpp', '.h')),
       grace_period=args.debounce / 1000
    )


if __name__ == "__main__":
    main()
