#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pathlib

__author__ = "Jonathan Haas"
__email__ = "jonathan.haas.ger@gmail.com"

# Define some "global" variables to be available upon import

# directory path in which this file is stored
HERE = pathlib.Path(__file__).absolute().parent

# directory path of project root
BASE_DIR = HERE.parents[1]

# directory path in which the Exercise directories are stored
BASE_EXERCISE_DIR = BASE_DIR / "Exercises"
assert BASE_EXERCISE_DIR.exists()


__exercise_dir_stem = "Exercises_"
# directory paths that contain exercises
EXERCISE_DIRS = sorted([p for p in BASE_EXERCISE_DIR.glob(__exercise_dir_stem + "*")])

# output directory to save exercise results
BASE_OUTPUT_DIR = BASE_DIR / "outputs"
assert BASE_OUTPUT_DIR.exists()
