#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pathlib


def unique_path(directory, name_pattern):
    counter = 0
    while True:
        counter += 1
        path = directory / name_pattern.format(counter)
        if not path.exists():
            return path


if __name__ == "__main__":
    path = unique_path(pathlib.Path.cwd().parent, "test_{:03d}.txt")
    print(path)
