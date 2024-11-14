# Tests Module Documentation

## Overview
This module, `tests.py`, contains unit tests for the `Maze` class from the `maze.py` file. The tests are written using the `unittest` framework to ensure the correct creation, structure, and behavior of the maze cells.

### Dependencies
- **`unittest`**: Python's built-in module for writing and running tests.
- **`Maze`**: The `Maze` class from the `maze.py` module is used for testing.

```python
import unittest
from maze import Maze
```

## Class

### `Tests`
The `Tests` class extends `unittest.TestCase` and contains several methods to verify the functionality of the `Maze` class. Each method tests a specific part of the `Maze` behavior.

#### Test Methods:

- **`test_maze_create_cells(self)`**: Tests whether the maze creates the correct number of cells, based on the given number of rows and columns.
  - Asserts that the length of `_cells` matches `num_cols`.
  - Asserts that the length of `_cells[0]` matches `num_rows`.

- **`test_maze_create_cells_large(self)`**: Similar to `test_maze_create_cells`, but with larger dimensions. This ensures that the maze can handle more rows and columns without any issues.
  - Asserts that the length of `_cells` matches `num_cols`.
  - Asserts that the length of `_cells[0]` matches `num_rows`.

- **`test_maze_break_entrance_and_exit(self)`**: Tests that the entrance and exit walls are properly removed during the maze creation.
  - Asserts that the top wall of the first cell is removed (`has_top_wall` is `False`).
  - Asserts that the bottom wall of the last cell is removed (`has_bottom_wall` is `False`).

- **`test_maze_reset_cells_visited(self)`**: Tests that all cells in the maze are set to unvisited after initialization.
  - Asserts that each cell's `visited` attribute is `False`.

## Running the Tests
To run the tests, execute the script with Python. The `unittest` framework will automatically detect the tests and run them.

```bash
python tests.py
```

If all tests pass, you will see an output indicating success. If any test fails, `unittest` will show the details of the failed test.

## Example Usage
Below is an example of how to run the tests from the command line:

```bash
$ python tests.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.005s

OK
```

## Notes
- These tests ensure that the `Maze` class is correctly creating its cells, breaking entrance and exit walls as expected, and resetting the `visited` status of all cells.
- The tests provide good coverage for the initialization and structural aspects of the maze. Additional tests could be added to verify maze generation and solving behavior.

