# image_processing_exercises
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


## Description

This repository contains the exercises for the Course "Image Processing, Analysis and Classification" at UPM, Spring Semester 2021.

## Requirements
Create a conda environment to run this project in isolation and install the necessary dependencies.
```[bash]
cd image_processing_exercises
conda env create -f environment.yml
conda activate image_processing_exercises 
```

## Installation
```[bash]
pip install --editable .
```
This install this package into the active environment.


## Exercises 0X
These are the relevant files:
* `utils.py` contains the low-level image processing. Most of the relevant functionality is implemented here. This module is also unit-tested and the tests can be found under `tests/test_utils.py`.  To run these tests call `pytest ./tests/test_utils.py` . Note: These tests do not create any output for manual inspection.
* `exercises.py` are mostly wrapper functions around low-level functions to have functions named as required in the exercise pdfs.
* `main.py` is a convenience script to run all exercises in `exercises.py` at once and create output files under `outputs/`. To run this script call `python ./src/image_processing_exercises/main.py`

## Image Segmentation | Professor Alonso
The image segmentation exercises are implemented in the `segmentation.ipynb` jupyter notebook. In case the the jupyter notebook cannot be executed, the file `segmentation.html` contains the jupyter notebook rendered as html. I have implemented all exercises in the the same notebook, therefore I also have uploaded two times the identical code base to the moodle assignment. 

## Notes on Implementation
The pixel manipulating functions in `utils.py` can calculate the results in two different ways which is specified with the `method` parameter. `method="mask"` uses numpy boolean indexing or higher functionality while `method="loop"` computes the result by accessing each pixel explicitly. Both methods are unit-tested where needed.