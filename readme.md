# Maze Solver Project - README

## Overview
The Maze Solver project is a Python-based graphical application that generates and solves mazes. The project utilizes the Tkinter library for visualization and provides an interactive way to explore maze generation and solving techniques. The primary components of the project include classes for representing graphical elements, cells, and the maze itself, as well as a main script for running the complete program.

## Project Structure
The project consists of the following main modules:

1. **`graphics.py`**: Handles the creation of the graphical window and drawing elements such as lines.
2. **`cell.py`**: Represents individual cells in the maze. Each cell can have walls on its sides and knows its state, such as whether it has been visited.
3. **`maze.py`**: Defines the `Maze` class, which manages the entire maze, including generating the layout and solving the maze using depth-first search.
4. **`tests.py`**: Contains unit tests for validating the functionality of the maze generation and cell states.
5. **`main.py`**: The entry point of the program, responsible for setting up the window, creating the maze, solving it, and displaying the result.

## Dependencies
To run the Maze Solver project, the following dependencies are required:

- **Python 3.x**: The codebase is written in Python and uses features compatible with Python 3.
- **Tkinter**: A built-in Python module for GUI applications, used for visualization.

## Installation
1. **Clone the Repository**:
   Clone the repository to your local machine using the command:
   ```bash
   git clone <repository_url>
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd maze-solver-project
   ```

3. **Run the Project**:
   Execute the main script to visualize maze generation and solving:
   ```bash
   python main.py
   ```

## Usage
The program runs through the following steps:
1. A graphical window is created using the `Window` class from `graphics.py`.
2. A maze is generated with a specified number of rows and columns.
3. The maze is displayed, and an attempt to solve the maze is visualized.
4. Upon successful solving, the graphical representation remains open until the user closes it.

### Example
To create a maze with 12 rows and 16 columns and solve it:
```bash
python main.py
```
This command will open a window, create a maze, and solve it in real time.

## Modules Overview

### 1. `graphics.py`
This module provides the `Window`, `Point`, and `Line` classes to handle graphical operations.
- **`Window`**: Manages the graphical window and allows for drawing operations.
- **`Point`** and **`Line`**: Used to represent and draw points and lines within the window.

### 2. `cell.py`
The `Cell` class represents individual cells of the maze.
- **Attributes**: `has_left_wall`, `has_right_wall`, `has_top_wall`, and `has_bottom_wall` indicate the presence of walls in each direction.
- **`draw()` Method**: Draws the cell, including all walls.
- **`draw_move()` Method**: Draws a path from one cell to another, useful for visualizing the maze solution.

### 3. `maze.py`
The `Maze` class manages the generation and solving of the maze.
- **`_create_cells()` Method**: Initializes all cells in the maze.
- **`_break_entrance_and_exit()` Method**: Removes walls for the entrance and exit.
- **`solve()` Method**: Uses a recursive depth-first search algorithm to solve the maze and visualize the solution.

### 4. `tests.py`
The `tests.py` module uses Python's `unittest` framework to validate:
- Maze cell creation.
- Entrance and exit walls.
- Proper resetting of the visited status of cells.

### 5. `main.py`
The entry point script that initializes the maze, solves it, and displays the graphical representation.

## Running Unit Tests
To ensure the correctness of the code, the `tests.py` module provides unit tests. Run the tests using the following command:
```bash
python tests.py
```
This command will execute all tests, and if they pass, you will see an output similar to:
```
....
----------------------------------------------------------------------
Ran 4 tests in 0.005s

OK
```

## Customization
You can modify the maze dimensions or the visual parameters by adjusting the `num_rows`, `num_cols`, `screen_x`, `screen_y`, and `margin` values in `main.py`. For example, you can change the maze size by editing:
```python
num_rows = 15
num_cols = 20
```
This will create a larger maze for solving.

## Notes
- **Recursion Limit**: The script sets a high recursion limit (`sys.setrecursionlimit(10000)`) to avoid recursion depth errors when solving larger mazes.
- **Visualization**: The project is designed to provide a visual representation, so it's ideal for educational purposes to understand depth-first search and maze-solving algorithms.

## Contributions
If you'd like to contribute to this project, feel free to submit issues and pull requests on the GitHub repository. We welcome any improvements, such as optimizing the solving algorithm or adding new visual features.

## License
This project is open source and available under the MIT License. Feel free to use and modify it as needed.


