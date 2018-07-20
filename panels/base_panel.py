import ttk

"""
BasePanel: A base panel class that all other panels should extend
"""

class BasePanel:

    def __init__(self, parent, text):
        self.content = ttk.Labelframe(parent, text=text)

    def grid(self, **kwargs):
        return self.content.grid(**kwargs)
