from gui import LibraryGUI
from library import Library
import tkinter as tk

if __name__ == "__main__":
    library = Library()
    root = tk.Tk()
    gui = LibraryGUI(root, library)
    root.mainloop()
