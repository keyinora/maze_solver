# Graphics Module Documentation

## Overview

This module, `graphics.py`, provides a simple graphical interface for drawing using the Tkinter library in Python. It includes a `Window` class to manage the graphical window, and two shape classes, `Point` and `Line`, to facilitate drawing basic geometric shapes.

### Dependencies

- Python's `tkinter` library is used to create and manage the graphical window and canvas.

```python
from tkinter import Tk, BOTH, Canvas
```

## Classes

### 1. `Window`

This class is responsible for creating and managing a graphical window, which allows for drawing lines and managing the application's lifecycle.

#### Methods:

- **`__init__(self, width, height)`**: Initializes the window with a specified width and height.
- **`redraw(self)`**: Refreshes the graphical interface.
- **`wait_for_close(self)`**: Keeps the window running until it is closed by the user.
- **`draw_line(self, line, fill_color='black')`**: Draws a given line object on the canvas with the specified color.
- **`close(self)`**: Closes the window.

#### Example Usage:

```python
window = Window(500, 500)
line = Line(Point(50, 50), Point(450, 450))
window.draw_line(line)
window.wait_for_close()
```

### 2. `Point`

Represents a point in a 2D space.

#### Attributes:

- **`x`**: The x-coordinate of the point.
- **`y`**: The y-coordinate of the point.

#### Example Usage:

```python
point = Point(100, 200)
```

### 3. `Line`

Represents a line connecting two points.

#### Attributes:

- **`p1`**: The starting point (`Point`) of the line.
- **`p2`**: The ending point (`Point`) of the line.

#### Methods:

- **`draw(self, canvas, fill_color='black')`**: Draws the line on the provided `canvas` using the specified color.

#### Example Usage:

```python
p1 = Point(50, 50)
p2 = Point(450, 450)
line = Line(p1, p2)
```

## How to Use

To use the module, create a `Window` instance, then create `Point` and `Line` instances as needed, and use `Window` methods to draw them on the canvas.

## Example

```python
from graphics import Window, Point, Line

# Create a window
window = Window(500, 500)

# Define two points
p1 = Point(100, 100)
p2 = Point(400, 400)

# Create a line from the points
line = Line(p1, p2)

# Draw the line in the window
window.draw_line(line, fill_color="blue")

# Wait for the window to be closed by the user
window.wait_for_close()
```

