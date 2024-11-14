# Cell Module Documentation

## Overview
This module, `cell.py`, defines the `Cell` class that represents a single cell in a grid, such as a maze. It uses the `graphics` module to handle drawing the cell and its components (walls). The class can manage and visualize the walls of the cell, making it useful for applications like maze generation and solving.

### Dependencies
- The `graphics` module, which contains the `Line` and `Point` classes used for drawing.

```python
from graphics import Line, Point
```

## Class

### `Cell`
This class represents a cell in a grid, typically used in a maze. It tracks the presence of walls and whether the cell has been visited. The `Cell` class can also draw itself and its movement connections on a given window.

#### Attributes:
- **`has_left_wall`**: Boolean indicating whether the cell has a left wall.
- **`has_right_wall`**: Boolean indicating whether the cell has a right wall.
- **`has_top_wall`**: Boolean indicating whether the cell has a top wall.
- **`has_bottom_wall`**: Boolean indicating whether the cell has a bottom wall.
- **`visited`**: Boolean indicating whether the cell has been visited.
- **`_x1, _x2, _y1, _y2`**: Coordinates of the cell used for drawing.
- **`_win`**: The window (`Window` instance) where the cell will be drawn.

#### Methods:
- **`__init__(self, win=None)`**: Initializes the cell. Takes an optional `win` parameter to specify the window for drawing.
- **`draw(self, x1, y1, x2, y2)`**: Draws the cell with the given coordinates. Walls are drawn based on the cell's attributes.
- **`draw_move(self, to_cell, undo=False)`**: Draws a line representing movement between the current cell and another cell (`to_cell`). The `undo` parameter changes the color of the line.

## How to Use
To use the `Cell` class, you should first create a `Window` instance from the `graphics` module. You can then create `Cell` instances and use the `draw` method to visualize them. The `draw_move` method can be used to illustrate movement between cells, which is useful for visualizing maze solutions.

#### Example Usage:
```python
from graphics import Window, Point, Line
from cell import Cell

# Create a window
window = Window(500, 500)

# Create a cell and draw it
cell = Cell(win=window)
cell.draw(50, 50, 100, 100)

# Create another cell
another_cell = Cell(win=window)
another_cell.draw(100, 50, 150, 100)

# Draw a move from the first cell to the second cell
cell.draw_move(another_cell)

# Wait for the window to close
window.wait_for_close()
```

## Methods in Detail

### `draw(self, x1, y1, x2, y2)`
This method draws the four walls of the cell on the canvas. Each wall is drawn depending on whether it exists (e.g., `has_left_wall`). The color of the wall can be modified, where removing a wall is visualized by drawing it in white.

### `draw_move(self, to_cell, undo=False)`
This method is used to visualize movement between two cells. It draws a line between the centers of the current cell and `to_cell`. By default, the line is red, but if `undo` is set to `True`, the line color changes to gray to indicate a backtrack or undo action.