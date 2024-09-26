# Pytest Tutorial

Welcome to the Pytest Tutorial project! This repository contains examples and exercises to help you learn and master the `pytest` framework for testing Python code.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Writing Tests](#writing-tests)
- [Advanced Features](#advanced-features)
- [Contributing](#contributing)
- [License](#license)

## Introduction

`pytest` is a powerful testing framework for Python that makes it easy to write simple and scalable test cases. This tutorial will guide you through the basics of `pytest`, as well as some of its more advanced features.

## Installation

To get started, you need to have Python installed on your machine. You can install `pytest` using `pip`:

```bash
pip install pytest
```

## Project Structure
Here is the structure of the project
pytest-tutorial/
├── src/
│   └── example.py
├── tests/
│   ├── test_example.py
│   └── test_rectangle.py
├── .gitignore
├── .github/
│   └── workflows/
│       └── citest.yaml
└── README.md

- src/: Contains the source code for the examples.
- tests/: Contains the test cases.
- .github/workflows/: Contains the GitHub Actions workflow for continuous integration.
- README.md: This file

## Running Tests
To run the tests, navigate to the root directory of the project and execute
```bash
pytest
```
This will discover and run all the test cases in the tests/ directory.

## Writing Tests
Here is an example of a simple test case in tests/test_example.py:
```python
def test_addition():
    assert 1 + 1 == 2
```

You can run this specific test file using:
```python
pytest tests/test_example.py
```
## Advanced Features
pytest offers many advanced features such as fixtures, parameterized tests, and plugins. Here are a few examples:  
### Fixtures
Fixtures are used to set up and tear down test environments. Here is an example:
```python
import pytest

@pytest.fixture
def sample_data():
    return {"key": "value"}

def test_sample_data(sample_data):
    assert sample_data["key"] == "value"
```
## Parameterized Tests
Parameterized tests allow you to run the same test with different inputs:
```python
import pytest

@pytest.mark.parametrize("input,expected", [(1, 2), (2, 3), (3, 4)])
def test_increment(input, expected):
    assert input + 1 == expected
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Make sure to follow the coding standards and write tests for your code.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.