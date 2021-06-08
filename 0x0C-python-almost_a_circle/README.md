# 0x0C-python-almost_a_circle

## Introduction
This project is meant to show how working on a large project would like, from creating classes and building on them through inheritance as well as testing your code by using a test-driven development approach using the unittest module.

## models/

### base.py
This file contains a class ``` Base ```. It is the '*base*' of all other classes in this project. Main goal is to manage ``` id ``` attribute to avoid code duplication.

###  __init__.py
This makes the folder a python module.

## tests/
This folder contains the test files and folders of this project.

### test_models/
Test folder contains unittests for the model folder.

#### test_base.py
Unit test for ```base.py```.

#### test_rectangle.py
Unit test for '''rectangle.py'''.

#### test_square.py
Unit test for '''square.py'''.
