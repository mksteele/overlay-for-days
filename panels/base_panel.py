import ttk

from Tkinter import Frame, BOTH
"""
BasePanel: A base panel class that all other panels should extend
"""

class BasePanel:

    def __init__(self, parent, text):
        self.parent = parent
        self.text = text
        self.frame = ttk.LabelFrame(self.parent, text=self.text)
        self.create_content_frame()

    def create_content_frame(self):
        self.content = Frame(self.frame, width=400, height=400,
                padx=10, pady=10)
        self.content.grid_propagate(0)
        self.content.pack(fill=BOTH, expand=1)

    def grid(self, **kwargs):
        return self.frame.grid(**kwargs)


