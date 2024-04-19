# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from pathlib import Path


def tree(directory, spacer="", level=1, directory_only=False):
    if level == 0:
        return

    files = list(Path(directory).iterdir())

    for index, file in enumerate(files):
        connector = "└── " if index == len(files) - 1 else "├──"

        if file.is_dir():
            print(spacer + connector + file.name)
            tree(file, spacer + "|    ", level - 1, directory_only)
        elif file.is_file() and not directory_only:
            print(spacer + connector + file.name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Display directory tree structure"
    )
    parser.add_argument(
        "directory",
        nargs="?",
        type=str,
        default=".",
        help="The root directory path",
    )
    parser.add_argument(
        "-l",
        "--level",
        type=int,
        default=-1,
        help="Max display depth of the directory tree",
    )
    parser.add_argument(
        "-d",
        "--directory-only",
        action="store_true",
        help="Show directories only",
    )

    args = parser.parse_args()
    tree(args.directory, level=args.level, directory_only=args.directory_only)
