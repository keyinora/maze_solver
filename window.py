from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        # Create the root widget
        self.__root = Tk()
        # Set the window title
        self.__root.title("TKinter Window")
        # Set the dimensions of the window
        self.__root.geometry(f"{width}x{height}")
        # Create a canvas widget
        self.__canvas = Canvas(self.__root)
        # Pack the canvas widget so it's ready to be drawn
        self.__canvas.pack(fill=BOTH, expand=True)
        # Data member to track if the window is running
        self.__running = False
        # Connect the close method to the "delete window" action
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False