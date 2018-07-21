import ttk

from Tkinter import Frame, BOTH

"""
BasePanel: A base panel class that all other panels should extend
"""

WIDTH = 300
HEIGHT = 250

class BasePanel:

    def __init__(self, parent, text, width=WIDTH, height=HEIGHT):
        self.parent = parent
        self.text = text
        self.frame = ttk.LabelFrame(self.parent, text=self.text)

        self.content = Frame(self.frame, width=width, height=height,
                padx=10, pady=10)
        self.content.grid_propagate(0)
        self.content.pack(fill=BOTH, expand=1)

    def grid(self, **kwargs):
        return self.frame.grid(**kwargs)


