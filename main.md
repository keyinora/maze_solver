# Main Module Documentation

## Overview
This module, `main.py`, serves as the entry point for running the maze solver program. It creates a graphical window, generates a maze using the `Maze` class, and then attempts to solve it while visualizing the process in the window. The module makes use of the `graphics`, `maze`, and `sys` libraries.

### Dependencies
- **`graphics`**: Used for creating and managing the graphical window.
- **`Maze`**: The `Maze` class from the `maze.py` module is used to generate and solve the maze.
- **`sys`**: Used for setting the recursion limit to allow deeper recursion during maze solving.

```python
from graphics import Window
from maze import Maze
import sys
```

## Main Function

### `main()`
The `main()` function is responsible for setting up the graphical window, initializing the maze, and solving it. It provides a visual representation of the maze generation and the solution process.

#### Steps Involved:
1. **Setup Parameters**:
   - Defines the number of rows and columns for the maze (`num_rows` and `num_cols`).
   - Defines the margin, screen dimensions (`screen_x` and `screen_y`), and calculates the size of each cell (`cell_size_x` and `cell_size_y`).

2. **Set Recursion Limit**:
   - Uses `sys.setrecursionlimit(10000)` to ensure that the recursive depth-first search can handle larger mazes without hitting the default recursion limit.

3. **Create Window and Maze**:
   - Creates a `Window` instance with the specified screen size.
   - Initializes a `Maze` instance with the specified parameters.

4. **Solve the Maze**:
   - Calls `maze.solve()` to solve the maze and prints whether the maze can be solved or not.

5. **Wait for User Interaction**:
   - Calls `win.wait_for_close()` to keep the window open until the user closes it.

#### Example Usage
To run the program, simply execute `main.py` using Python.

```bash
python main.py
```

### Code Highlights
- **Recursion Limit**: The `sys.setrecursionlimit(10000)` line is critical because maze solving is done recursively, and deeper recursion may be required for larger mazes.
- **Graphical Output**: The graphical representation of the maze and its solution is created using the `Window` class from the `graphics` module, providing a clear visual output of the maze-solving process.

## Example Output
Upon running the program, the following messages will be printed to indicate the progress:

```
maze created
maze solved!
```

If the maze is unsolvable, it will output:

```
maze created
maze cannot be solved!
```

## Notes
- The commented-out sections in the code provide examples of incremental updates made during the development process, such as drawing individual cells or generating different mazes with varying parameters.
- This main script provides an excellent demonstration of how the `Maze` and `Window` classes work together to create a visual and interactive maze-solving application.

