# 0x03. Unittests and Integration Tests

## Unit Testing
Unit testing is the process of testing that a particular function returns expected results 
for different sets of inputs.
A unit test is supposed to test standard inputs and corner cases.
It should focus on testing the logic defined inside the tested function.
To isolate the unit under test and ensure a consistent test environment, 
most calls to additional functions should be mocked, especially if they make network 
or database calls. The goal of a unit test is to answer the question:
"If everything defined outside this function works as expected, does this function work 
as expected?"

## Table of Contents

- [Introduction](#introduction)
- [Unit Tests vs. Integration Tests](#unit-tests-vs-integration-tests)
- [Testing Patterns](#testing-patterns)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project aims to demonstrate the concepts of unit testing and integration testing, 
along with some common testing patterns, such as mocking, parametrization, and fixtures. 
It provides examples of how to use the `unittest` framework and the `unittest.mock` library 
in Python to perform these types of tests.

## Resources

Read or watch:

- [unittest - Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock - mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [How to mock a readonly property with mock?](https://stackoverflow.com/questions/25396818/how-to-mock-a-readonly-property-with-mock)
- [parameterized](https://pypi.org/project/parameterized/)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)



## Unit Tests vs. Integration Tests
### Unit Tests

Unit testing is the process of testing individual units or components of code in isolation 
to ensure that they produce the expected output for various inputs. 
The key characteristics of unit tests are:

- They focus on testing the logic defined inside a single function or method.
- External dependencies, such as network or database calls, are typically mocked 
 to isolate the unit under test.
- Unit tests are used to answer the question: "If everything defined outside this function 
works as expected, does this function work as expected?"

### Integration Tests

Integration tests, on the other hand, aim to test the interactions between different parts of the code, often end-to-end. The key characteristics of integration tests are:

- They test the code paths that involve multiple units or components working together.
- Low-level functions that make external calls, such as HTTP requests, file I/O, and database 
I/O, are sometimes mocked, but other parts of the code interact as they would in a real-world 
scenario.
- Integration tests are used to validate that different parts of the code can work together 
as expected.

## Testing Patterns

### Mocking

Mocking involves creating fake versions of external dependencies to control their behavior 
during testing. It allows you to isolate the unit under test from external factors, 
ensuring a consistent and predictable test environment.

### Parametrization

Parametrization allows you to run the same test with different sets of inputs. 
This can be useful for testing a function with multiple test cases or corner cases 
without writing separate test functions for each case.

### Fixtures

Fixtures are reusable objects or data that can be set up before running tests and 
cleaned up afterward. They help in organizing common test setup and teardown tasks, 
promoting code reusability and maintainability.

# Requirements

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7).
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the pycodestyle style (version 2.5).
- All your files must be executable.
- All your modules should have a documentation:
  - `python3 -c 'print(__import__("my_module").__doc__)'`
- All your classes should have a documentation:
  - `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
- All your functions (inside and outside a class) should have a documentation:
  - `python3 -c 'print(__import__("my_module").my_function.__doc__)'`
  - `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
- A documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method (the length of it will be verified).
- All your functions and coroutines must be type-annotated.


## Requirements

- Python 3.7 or higher
- Ubuntu 18.04 LTS

## Required Files

Click the links below to download the required files:

- [utils.py (Download)](https://intranet-projects-files.s3.amazonaws.com/webstack/utils.py)
  Click to show/hide file contents

- [client.py (Download)](https://intranet-projects-files.s3.amazonaws.com/webstack/client.py)
  Click to show/hide file contents

- [fixtures.py (Download)](https://intranet-projects-files.s3.amazonaws.com/webstack/fixtures.py)
  Click to show/hide file contents

