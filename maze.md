# Maze Module Documentation

## Overview
This module, `maze.py`, provides the `Maze` class to represent and generate a maze using depth-first traversal. It also includes methods to solve the maze by finding a path from the entrance to the exit. This class uses the `Cell` class from `cell.py` for managing each individual cell of the maze.

### Dependencies
- **`time`**: Used for creating animation delays.
- **`random`**: Used for generating random choices during maze creation.
- **`Cell`**: The `Cell` class from `cell.py` is used for representing each cell in the maze.

```python
import time
import random
from cell import Cell
```

## Class

### `Maze`
The `Maze` class is responsible for creating a visual representation of a maze with cells, breaking walls to generate the maze, and solving the maze. It utilizes random generation to determine the path between cells.

#### Attributes:
- **`_x1, _y1`**: Coordinates of the top-left corner of the maze.
- **`_num_rows`**: Number of rows in the maze.
- **`_num_cols`**: Number of columns in the maze.
- **`_cell_size_x, _cell_size_y`**: Size of each cell in the maze, in the x and y directions.
- **`_win`**: The window (`Window` instance) where the maze will be visualized.
- **`_cells`**: A 2D list that stores all the cells in the maze.

#### Methods:
- **`__init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None)`**: Initializes the maze with given parameters and generates the maze structure.
- **`_create_cells(self)`**: Creates all the cells for the maze and draws them on the canvas.
- **`_draw_cell(self, i, j)`**: Draws a cell at the specified position.
- **`_animate(self)`**: Animates the drawing process by refreshing the window.
- **`_break_entrance_and_exit(self)`**: Breaks the entrance at the top-left corner and the exit at the bottom-right corner of the maze.
- **`_break_walls_r(self, i, j)`**: Recursively breaks walls between cells to create the maze using depth-first search.
- **`_reset_cells_visited(self)`**: Resets the `visited` status of all cells.
- **`_solve_r(self, i, j)`**: Recursively attempts to solve the maze starting from a given cell.
- **`solve(self)`**: Starts solving the maze from the entrance and returns `True` if a solution is found.

## How to Use
To use the `Maze` class, create an instance of the `Window` class from the `graphics.py` module, then instantiate the `Maze` with appropriate parameters. You can use the `solve` method to visualize the maze solution.

#### Example Usage:
```python
from graphics import Window
from maze import Maze

# Create a window
window = Window(500, 500)

# Create a maze with 10 rows and 10 columns
maze = Maze(x1=20, y1=20, num_rows=10, num_cols=10, cell_size_x=40, cell_size_y=40, win=window, seed=42)

# Solve the maze
maze.solve()

# Wait for the window to close
window.wait_for_close()
```

## Methods in Detail

### `_create_cells(self)`
This method is responsible for creating the cells that make up the maze. It populates the `_cells` attribute with `Cell` instances and draws each one using `_draw_cell()`.

### `_break_walls_r(self, i, j)`
This method uses a recursive depth-first search to break walls between cells and create the maze. It marks each cell as visited and randomly selects the next cell to move to, ensuring a complete and connected maze.

### `_solve_r(self, i, j)`
This method is a recursive solver that finds a path through the maze by exploring available directions (left, right, up, down) and backtracking if a dead end is reached. It visually represents the path taken, including incorrect paths, which are drawn in gray.

### `solve(self)`
The `solve()` method calls `_solve_r()` from the starting cell (0, 0) to begin solving the maze. It returns `True` if the maze is successfully solved.

## Notes
- **Animation**: The `_animate()` method uses a small delay to visualize the maze generation and solving process in real-time, providing a clear and engaging view of the maze structure.
- **Entrance and Exit**: The entrance and exit of the maze are automatically created by breaking the top wall of the starting cell and the bottom wall of the ending cell, respectively.

